import pandas as pd
import joblib
import numpy as np

def preprocess(data):
    """
    Preprocesses the raw data using pre-saved encoders and scaler.

    Args:
        data (list): Raw input data as a list of lists.

    Returns:
        np.ndarray: Processed dataset in NumPy array format.
    """
    try:
        # Column names as per your data structure
        columns = [
            'Dummy Policy No', 'ASSURED_AGE', 'NOMINEE_RELATION', 'OCCUPATION', 'POLICY SUMASSURED',
            'Premium', 'PREMIUMPAYMENTMODE', 'Annual Income', 'HOLDERMARITALSTATUS', 'INDIV_REQUIREMENTFLAG',
            'Policy Term', 'Policy Payment Term', 'CORRESPONDENCECITY', 'CORRESPONDENCESTATE',
            'CORRESPONDENCEPOSTCODE', 'Product Type', 'CHANNEL', 'Bank code', 'POLICYRISKCOMMENCEMENTDATE',
            'Date of Death', 'INTIMATIONDATE', 'STATUS', 'SUB_STATUS'
        ]

        # Step 1: Convert the raw data (list of lists) to a DataFrame
        df = pd.DataFrame([data], columns=columns)  # Ensure it's a list of lists for a single sample

        # Step 2: Clean financial columns
        financial_columns = ['POLICY SUMASSURED', 'Premium', 'Annual Income']
        for col in financial_columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

        # Step 3: Drop irrelevant columns
        columns_to_drop = [
            'Dummy Policy No', 'CORRESPONDENCECITY', 'CORRESPONDENCESTATE', 'CORRESPONDENCEPOSTCODE',
            'POLICYRISKCOMMENCEMENTDATE', 'Date of Death', 'INTIMATIONDATE', 'STATUS', 'SUB_STATUS'
        ]
        df = df.drop(columns=columns_to_drop, errors='ignore')

        # Step 4: Handle missing values
        df.replace("", pd.NA, inplace=True)
        df['Bank code'] = df['Bank code'].fillna(-1)  # Replace NaNs with -1 in 'Bank code'
        df = df.fillna(df.median(numeric_only=True))  # Replace other NaNs in numerical columns with median

        # Step 5: Encode categorical columns using saved label encoders
        label_encoders = joblib.load('../models/label_encoders.pkl')  # Load saved label encoders
        categorical_columns = [
            'NOMINEE_RELATION', 'OCCUPATION', 'PREMIUMPAYMENTMODE',
            'HOLDERMARITALSTATUS', 'INDIV_REQUIREMENTFLAG',
            'Product Type', 'CHANNEL'
        ]
        for col in categorical_columns:
            if col in df.columns:
                if col in label_encoders:  # Ensure the column exists in the encoders
                    df[col] = label_encoders[col].transform(df[col].astype(str))
                else:
                    raise ValueError(f"Label encoder for column '{col}' not found.")

        # Step 6: Normalize numerical features using saved scaler
        numerical_columns = ['ASSURED_AGE', 'POLICY SUMASSURED', 'Premium', 'Annual Income',
                             'Policy Term', 'Policy Payment Term', 'Bank code']
        scaler = joblib.load('../models/scaler.pkl')  # Load saved scaler
        df[numerical_columns] = scaler.transform(df[numerical_columns])

        # Step 7: Convert the DataFrame to a NumPy array
        processed_data = df.values  # This will give you a 2D array with shape (1, 23) for a single input sample

        # Debug: Print the shape of processed data
        print(f"Processed data shape: {processed_data.shape}")
        
        return processed_data  # Return the processed data as a numpy array

    except Exception as e:
        print(f"Error in preprocessing: {e}")
        raise

# Sample input data
input_data = [
    1, 20, "Mother", "Service", 1200000, 120000, "Quarterly", 420000, "Single", "Non Medical",
    10, 10, "Sahibganj", "Jharkhand", 816115, "ULIP", "Retail Agency", "", "30-08-2023", "26-10-2023", "12-12-2023", "Claim", "Death Claim Repudiated"
]

# Call the preprocess function
processed_data = preprocess(input_data)
print(processed_data)
