import joblib
import numpy as np

# Load the preprocessing model
preprocessing_model = joblib.load('models/data_preprocessing_model.joblib')

def preprocess(features):
    """
    Preprocess the input features using the trained preprocessing model.
    Args:
    - features: List of raw input feature values.
    
    Returns:
    - Processed feature array.
    """
    try:
        # Wrapping the features in a 2D array as the model expects this format
        features_2d = [features]  # Convert to a 2D array for the model
        processed_features = preprocessing_model.transform(features_2d)  # Apply preprocessing
        return processed_features
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        return None
