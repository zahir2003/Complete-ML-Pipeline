import os
import pandas as pd
from sklearn.model_selection import train_test_split
import logging

# Ensure the "logs" directory exists
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
log_file_path = os.path.join(log_dir, 'Data_injection.log')

# --- FIX: Corrected the formatter string ---
# The original format '%(asctime)%' was incorrect.
# The correct syntax is '%(asctime)s' to specify the placeholder and its type (string).
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('Data_injection')
logger.setLevel('DEBUG')

# Setup console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Setup file handler
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_data(data_url: str) -> pd.DataFrame:
    """load data from a CSV file."""
    try:
        df = pd.read_csv(data_url)
        logger.debug(f'Data loaded from {data_url}')
        return df
    except pd.errors.ParserError as e:
        logger.error(f"Failed to parse the CSV file: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error occurred while loading the data: {e}")
        raise


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data."""
    try:
        df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)
        df.rename(columns={'v1': 'Target', 'v2': 'Text'}, inplace=True)
        logger.debug('Data preprocessing completed')
        return df
    except KeyError as e:
        logger.error(f'Missing column in the dataframe: {e}')
        raise
    except Exception as e:
        logger.error(f'Unexpected error during preprocessing: {e}')
        raise


def save_data(train_data: pd.DataFrame, test_data: pd.DataFrame, output_path: str) -> None:
    """Save the train and test datasets."""
    try:
        raw_data_path = os.path.join(output_path, 'raw')
        os.makedirs(raw_data_path, exist_ok=True)
        train_data.to_csv(os.path.join(raw_data_path, "train.csv"), index=False)
        test_data.to_csv(os.path.join(raw_data_path, "test.csv"), index=False)
        logger.debug(f"Train and test data saved to {raw_data_path}")
    except Exception as e:
        logger.error(f"Unexpected error occurred while saving the data: {e}")
        raise


def main():
    try:
        test_size = 0.2
        # --- IMPROVEMENT: Using more descriptive variable names ---
        data_url = 'https://raw.githubusercontent.com/zahir2003/Datasets/refs/heads/main/spam%202.csv'
        output_path = './data'
        
        df = load_data(data_url=data_url)
        final_df = preprocess_data(df)
        train_data, test_data = train_test_split(final_df, test_size=test_size, random_state=42)
        save_data(train_data, test_data, output_path=output_path)
    except Exception as e:
        logger.error(f"Failed to complete the data ingestion process: {e}")
        print(f"Error : {e}")


if __name__ == '__main__':
    main()