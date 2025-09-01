import os
import pandas as pd
from dotenv import load_dotenv
from typing import List
from langchain_core.documents import Document
from langchain_astradb import AstraDBVectorStore
from prod_assistant.utils.model_loader import ModelLoader
from prod_assistant.utils.config_loader import load_config


class DataIngestion:
    """
    Class to handle data transformation and ingestion into AstraDB vector store.
    """

    def __init__(self):
        """
        Initialize environment variables, embedding model, and set CSV file path.
        """
        print("Initializing DataIngestion pipeline...")
        self.model_loader = ModelLoader()
        self._load_env_variables()
        self.csv_path = self._get_csv_path()
        self.product_data = self._load_csv()
        self.config = load_config()

    def _load_env_variables(self):
        """
        Load and validate required environment variables.
        """
        pass

    def _get_csv_path(self):
        """
        Get path to the CSV file located inside 'data' folder.
        """
        pass

    def _load_csv(self):
        """
        Load product data from CSV.
        """
        pass

    def transform_data(self):
        """
        Transform product data into list of LangChain Document objects.
        """
        pass

    def store_in_vector_db(self, documents: List[Document]):
        """
        Store documents into AstraDB vector store.
        """
        pass

    def run_pipeline(self):
        """
        Run the full data ingestion pipeline: transform data and store into vector DB.
        """
        pass
