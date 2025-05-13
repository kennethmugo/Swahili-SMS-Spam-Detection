import os
from swahili_spam_detector.constants import *
from swahili_spam_detector.utils.common import create_directories, read_yaml
from swahili_spam_detector.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        data_ingestion_config = DataIngestionConfig(source=config.source, file_name=config.file_name)

        return data_ingestion_config