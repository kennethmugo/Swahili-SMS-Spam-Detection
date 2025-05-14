import os
from swahili_spam_detector.constants import *
from swahili_spam_detector.utils.common import create_directories, read_yaml
from swahili_spam_detector.entity.config_entity import DataIngestionConfig, DataProcessingConfig

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
    
    def get_data_processing_config(self) -> DataProcessingConfig:
        config = self.config.data_processing

        create_directories([config.root_dir, config.train_data_path, config.test_data_path])

        data_processing_config = DataProcessingConfig(train_data_path=config.train_data_path, 
                                                      test_data_path=config.test_data_path, 
                                                      root_dir=config.root_dir,
                                                      sms_embeddings_filename=config.sms_embeddings_filename,
                                                      labels_filename=config.labels_filename,
                                                      raw_data_path=self.config.data_ingestion.raw_data_path,
                                                      embedding_model=self.params.EMBEDDING_MODEL)

        return data_processing_config
