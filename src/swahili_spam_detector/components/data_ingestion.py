import kagglehub
from swahili_spam_detector import logger
from swahili_spam_detector.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        """
        The data is downloaded from the Kaggle API and saved to a cache.
        """
        try:
            path = kagglehub.dataset_download(self.config.source)
            logger.info(f"Data downloaded and saved to {path}")
        except Exception as e:
            logger.error(f"Error downloading data: {e}")
            raise e