import os
import shutil
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

            #  The data isn't in the project directory, it is cached in the path. Move it to the project directory.
            #  First create the directory if it doesn't exist
            os.makedirs(self.config.root_dir, exist_ok=True)

            # Move the downloaded data to the project directory
            for file in os.listdir(path):
                source_file = os.path.join(path, file)
                destination_file = os.path.join(self.config.root_dir, file)
                shutil.copy2(source_file, destination_file)
                logger.info(f"Moved {source_file} to {destination_file}")

        except Exception as e:
            logger.error(f"Error downloading data: {e}")
            raise e