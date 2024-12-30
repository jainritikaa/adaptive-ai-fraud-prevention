import joblib
import numpy as np
import os
import pandas as pd

# Print the current working directory to debug the file path issue
print("Current working directory:", os.getcwd())

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
    # Add your additional fraud categories as needed
}

# Assign weights to each fraud class based on severity
fraud_class_weights = {
    0: 0.8,  # Claims Fraud (High Risk)
    1: 0.7,  # Signature Forgery (High Risk)
    2: 0.6,  # Document Tampering (Medium Risk)
    3: 0.9,  # Misappropriating Funds (High Risk)
    4: 0.5,  # Misrepresentation (Medium Risk)
    5: 0.4,  # Misselling (Low Risk)
    6: 0.3   # Miscellaneous (Low Risk)
}

# Updated predict_fraud_category function in fraud_detection.py
def predict_fraud(df):
    """
    Predict the fraud category using the fraud detection model and calculate the fraud risk score.
    Args:
    - df: Preprocessed DataFrame with feature columns (should be a single row or multiple rows).
    
    Returns:
    - The fraud category string, the probability of that category, and the fraud risk score.
    """
    try:
        # Ensure df is a 2D array (1 row, n_features columns)
        if len(df.shape) == 1:  # If it's a 1D array, reshape it to (1, n_features)
            df = df.reshape(1, -1)
        elif len(df.shape) == 2:  # If it's already 2D, ensure it's (n_samples, n_features)
            pass
        else:
            raise ValueError("Input data is not in a valid shape")

        # Get the probabilities for all fraud categories
        fraud_probabilities = fraud_detection_model.predict_proba(df)[0]

        # Calculate the fraud risk score using the weighted sum of probabilities
        fraud_risk_score = 0
        for i, prob in enumerate(fraud_probabilities):
            fraud_risk_score += prob * fraud_class_weights.get(i, 0)

        # Find the category with the highest probability
        fraud_category_index = np.argmax(fraud_probabilities)
        fraud_category_string = fraud_categories.get(fraud_category_index, "Unknown Category")

        # Get the probability of the most likely fraud category
        fraud_probability = fraud_probabilities[fraud_category_index]

        return fraud_category_string, fraud_probability, fraud_risk_score
    except Exception as e:
        print(f"Error during fraud detection: {e}")
        return None, None, None
