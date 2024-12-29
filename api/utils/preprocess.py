import os
import pandas as pd
import logging
import importlib.util

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

def preprocess_data_pipeline(csv_file_path, preprocessdata_path):
    """
    Preprocess raw data from a CSV file using the preprocess_data function.
    
    Args:
        csv_file_path (str): Path to the raw CSV data file.
        preprocessdata_path (str): Path to the preprocessdata.py file.
    
    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    try:
        # Check if preprocessdata.py exists
        if not os.path.exists(preprocessdata_path):
            raise FileNotFoundError(f"preprocessdata.py not found at {preprocessdata_path}")

        # Dynamically load preprocessdata.py
        spec = importlib.util.spec_from_file_location("preprocessdata", preprocessdata_path)
        preprocessdata = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(preprocessdata)

        # Access the preprocess_data function
        preprocess_data = preprocessdata.preprocess_data

        # Load and preprocess the raw data
        raw_df = pd.read_csv(csv_file_path)
        logging.debug(f"Loaded raw data: {raw_df.head()}")
        processed_df = preprocess_data(raw_df)
        logging.debug(f"Processed data: {processed_df.head()}")

        return processed_df

    except Exception as e:
        logging.error(f"Error in preprocessing: {e}")
        raise
