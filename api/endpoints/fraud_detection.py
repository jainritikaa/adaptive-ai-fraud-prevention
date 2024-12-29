import joblib
import numpy as np

# Load the fraud detection model
fraud_detection_model = joblib.load('../models/fraud-detection-model.joblib')

# Define a mapping between fraud category index and fraud category string
fraud_categories = {
    0: "Claims Fraud",
    1: "Signature Forgery",
    2: "Document Tampering",
    3: "Misappropriating Funds",
    4: "Misrepresentation",
    5: "Misselling",
    6: "Miscellaneous"
    # Add your additional fraud categories
}

def predict_fraud_category(processed_features):
    """
    Predict the fraud category using the fraud detection model.
    Args:
    - processed_features: Preprocessed feature array.
    
    Returns:
    - The fraud category string and probability.
    """
    try:
        # Get the probabilities for all fraud categories
        fraud_probabilities = fraud_detection_model.predict_proba(processed_features)[0]

        # Find the category with the highest probability
        fraud_category_index = np.argmax(fraud_probabilities)
        fraud_category_string = fraud_categories.get(fraud_category_index, "Unknown Category")

        # Get the probability of the most likely fraud category
        fraud_probability = fraud_probabilities[fraud_category_index]

        return fraud_category_string, fraud_probability
    except Exception as e:
        print(f"Error during fraud detection: {e}")
        return None, None
