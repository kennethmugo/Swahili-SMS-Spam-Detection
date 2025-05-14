from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    source: str
    raw_data_path: str
    root_dir: str