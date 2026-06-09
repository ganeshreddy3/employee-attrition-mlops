from src.entity.config_entity import DataIngestionConfig


config = DataIngestionConfig(
    train_data_path="artifacts/train.csv",
    test_data_path="artifacts/test.csv",
    raw_data_path="artifacts/raw.csv"
)

print(config)
