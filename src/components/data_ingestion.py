import os
import sys
from src.exception import logging
import pandas as pd

from sklearn.model_selecion import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def inititate_data_ingestion(self):
        logging.info("Entered the data ingestion method of component")
        try:
            df = pd.read_csv('')
