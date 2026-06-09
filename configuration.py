from src.entity.config_entity import DataValidationConfig
def get_data_validation_config(self):

    config = self.config["data_validation"]

    os.makedirs(
        config["root_dir"],
        exist_ok=True
    )

    return DataValidationConfig(
        root_dir=config["root_dir"],
        status_file=config["status_file"],
        train_data_path=config["train_data_path"]
    )
