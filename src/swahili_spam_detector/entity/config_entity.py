from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    source: str
    raw_data_path: str
    root_dir: str

@dataclass(frozen=True)
class DataProcessingConfig:
    train_data_path: str
    test_data_path: str
    sms_embeddings_filename: str
    labels_filename: str
    root_dir: str
    raw_data_path: str
    embedding_model: str