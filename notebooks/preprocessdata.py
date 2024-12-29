import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import joblib

def preprocess_data(df):
    """
    Preprocesses the dataset for model training or inference.

    Args:
    df (pd.DataFrame): Raw dataset.

    Returns:
    pd.DataFrame: Processed dataset ready for modeling.
    """
    # Step 1: Clean financial columns
    financial_columns = ['POLICY SUMASSURED', 'Premium', 'Annual Income']
    for col in financial_columns:
        df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

    # Step 2: Drop irrelevant columns
    columns_to_drop = [
        'Dummy Policy No', 'CORRESPONDENCECITY', 'CORRESPONDENCESTATE', 'CORRESPONDENCEPOSTCODE',
        'POLICYRISKCOMMENCEMENTDATE', 'Date of Death', 'INTIMATIONDATE', 'STATUS', 'SUB_STATUS'
    ]
    df = df.drop(columns=columns_to_drop)

    # Step 3: Handle missing values
    df['Bank code'] = df['Bank code'].fillna(-1)  # Replace NaNs with -1 in 'Bank code'
    df = df.fillna(df.median(numeric_only=True))  # Replace other NaNs in numerical columns with median

    # Step 4: Encode categorical columns
    categorical_columns = [
        'NOMINEE_RELATION', 'OCCUPATION', 'PREMIUMPAYMENTMODE',
        'HOLDERMARITALSTATUS', 'INDIV_REQUIREMENTFLAG',
        'Product Type', 'CHANNEL', 'Fraud Category'
    ]
    label_encoders = {}
    for col in categorical_columns:
        label_encoders[col] = LabelEncoder()
        df[col] = label_encoders[col].fit_transform(df[col].astype(str))
    
    # Save label encoders for later use
    joblib.dump(label_encoders, 'label_encoders.pkl')

    # Step 5: Normalize numerical features
    numerical_columns = ['ASSURED_AGE', 'POLICY SUMASSURED', 'Premium', 'Annual Income',
                         'Policy Term', 'Policy Payment Term', 'Bank code']
    scaler = MinMaxScaler()
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    # Save scaler for later use
    joblib.dump(scaler, 'scaler.pkl')

    return df


# Load raw data from a CSV file
raw_df = pd.read_csv('data/raw/fraud-dataset-raw.csv')

# Call preprocess_data function
processed_df = preprocess_data(raw_df)

# Display processed data
print(processed_df.head())
raw_df