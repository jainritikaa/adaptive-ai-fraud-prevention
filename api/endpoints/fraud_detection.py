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
def predict_fraud(df):
    """
    Predict the fraud category and calculate the fraud risk score.
    """
    try:
        # Ensure input is a 2D array
        if len(df.shape) == 1:
            df = df.reshape(1, -1)

        # Get probabilities
        fraud_probabilities = fraud_detection_model.predict_proba(df)[0]
        print(f"Fraud probabilities: {fraud_probabilities}")

        # Convert any float32 to Python float (float64)
        fraud_probabilities = fraud_probabilities.astype(float)

        # Calculate fraud risk score
        fraud_risk_score = sum(prob * fraud_class_weights.get(i, 0) for i, prob in enumerate(fraud_probabilities))

        # Convert fraud risk score to Python float
        fraud_risk_score = float(fraud_risk_score)

        # Determine category
        fraud_category_index = np.argmax(fraud_probabilities)
        fraud_category_string = fraud_categories.get(fraud_category_index, "Unknown Category")
        fraud_probability = fraud_probabilities[fraud_category_index]

        # Convert fraud_probability to Python float
        fraud_probability = float(fraud_probability)

        return fraud_category_string, fraud_probability, fraud_risk_score
    except Exception as e:
        print(f"Error in predict_fraud: {e}")
        return None, None, None
