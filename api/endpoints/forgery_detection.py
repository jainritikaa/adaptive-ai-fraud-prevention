import os
import cv2
import numpy as np
import warnings
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Force TensorFlow to use the CPU
import tensorflow as tf
from tensorflow.keras.models import load_model  # Import load_model function

# Suppress specific warnings related to cuDNN, cuBLAS, and cuFFT
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*cudnn.*")
warnings.filterwarnings("ignore", category=UserWarning, message=".*cuDNN.*")
warnings.filterwarnings("ignore", category=UserWarning, message=".*cuBLAS.*")
warnings.filterwarnings("ignore", category=UserWarning, message=".*cuFFT.*")


# Load the forgery detection model
model_path = "/home/mrigank/Documents/GitHub/adaptive-ai-fraud-prevention/models/forgery-detection-model.h5"  # Update with actual model path
model = load_model(model_path)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

def preprocess_image(image_path):
    """
    Preprocess the input image for model prediction.
    """
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Resize the image to the model's input size
    image = cv2.resize(image, (224, 224))  # Adjust based on model input
    image = image / 255.0  # Normalize to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    
    return image

def detect_forgery(image_path):
    """
    Detect forgery in the given image.
    """
    preprocessed_image = preprocess_image(image_path)
    forgery_score = model.predict(preprocessed_image)[0][0]  # Assuming single output
    status = "Forged" if forgery_score > 0.5 else "Authentic"
    
    return {
        "forgery_score": forgery_score,
        "status": status
    }
