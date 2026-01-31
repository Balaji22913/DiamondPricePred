import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method started")

        try:
            # ✅ FIX 1: Correct path (verify folder name!)
            data_path = os.path.join('notebook', 'data', 'gemstone.csv')
            df = pd.read_csv(data_path)

            logging.info("Dataset read as pandas DataFrame")

            os.makedirs(
                os.path.dirname(self.ingestion_config.raw_data_path),
                exist_ok=True
            )

            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(
                df, test_size=0.30, random_state=42
            )

            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )
            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info("Data ingestion completed successfully")

            # ✅ FIX 2: Proper return
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # ✅ FIX 3: RAISE the exception
            logging.error("Error occurred in Data Ingestion")
            raise CustomException(e, sys)
