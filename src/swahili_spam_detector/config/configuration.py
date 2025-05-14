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

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(source=config.source, raw_data_path=config.raw_data_path, root_dir=config.root_dir)

        return data_ingestion_config