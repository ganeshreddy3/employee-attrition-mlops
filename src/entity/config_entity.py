from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: str
    train_data_path: str
    test_data_path: str
    raw_data_path: str
from dataclasses import dataclass

@dataclass
class DataValidationConfig:
    root_dir: str
    status_file: str
    train_data_path: str
@dataclass
class DataTransformationConfig:
    root_dir: str
    train_data_path: str
    test_data_path: str
    preprocessor_obj_file_path: str
