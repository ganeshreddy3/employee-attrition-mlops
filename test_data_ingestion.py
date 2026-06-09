from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion


config = ConfigurationManager()

data_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(data_config)

print(
    data_ingestion.initiate_data_ingestion()
)
