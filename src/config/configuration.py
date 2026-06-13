import os
import yaml

from src.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

from src.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
)


class ConfigurationManager:

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ):

        with open(config_filepath) as config_file:
            self.config = yaml.safe_load(config_file)

        with open(params_filepath) as params_file:
            self.params = yaml.safe_load(params_file)

        os.makedirs(
            self.config["artifacts_root"],
            exist_ok=True,
        )

    def get_data_ingestion_config(self):

        config = self.config["data_ingestion"]

        os.makedirs(
            config["root_dir"],
            exist_ok=True,
        )

        return DataIngestionConfig(
            root_dir=config["root_dir"],
            source_URL=config["source_URL"],
            local_data_file=config["local_data_file"],
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"],
            raw_data_path=config["raw_data_path"],
        )

    def get_data_validation_config(self):

        config = self.config["data_validation"]

        os.makedirs(
            config["root_dir"],
            exist_ok=True,
        )

        return DataValidationConfig(
            root_dir=config["root_dir"],
            status_file=config["status_file"],
            train_data_path=config["train_data_path"],
        )

    def get_data_transformation_config(self):

        config = self.config["data_transformation"]

        os.makedirs(
            config["root_dir"],
            exist_ok=True,
        )

        return DataTransformationConfig(
            root_dir=config["root_dir"],
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"],
            preprocessor_obj_file_path=config[
                "preprocessor_obj_file_path"
            ],
        )
