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

@dataclass(frozen=True)
class ModelTrainingConfig:
    trained_model_path: str
    root_dir: str
    train_data_path: str
    sms_embeddings_filename: str
    labels_filename: str
    report_path: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    trained_model_path: str
    test_data_path: str
    sms_embeddings_filename: str
    labels_filename: str
    all_params: dict
    mlflow_experiment_name: str