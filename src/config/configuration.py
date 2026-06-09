import os
import yaml

from src.constants import CONFIG_FILE_PATH
from src.constants import PARAMS_FILE_PATH

from src.entity.config_entity import DataIngestionConfig


class ConfigurationManager:

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):

        with open(config_filepath) as config_file:
            self.config = yaml.safe_load(config_file)

        with open(params_filepath) as params_file:
            self.params = yaml.safe_load(params_file)

        os.makedirs(
            self.config["artifacts_root"],
            exist_ok=True
        )

    def get_data_ingestion_config(self):

        config = self.config["data_ingestion"]

        os.makedirs(
            config["root_dir"],
            exist_ok=True
        )

        data_ingestion_config = DataIngestionConfig(
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"],
            raw_data_path=config["raw_data_path"]
        )

        return data_ingestion_config
