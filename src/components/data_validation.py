import os
import sys

import pandas as pd

from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataValidationConfig


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self):

        try:

            validation_status = True

            logging.info("Data Validation Started")

            # Check if train file exists
            if not os.path.exists(self.config.train_data_path):

                validation_status = False

            else:

                df = pd.read_csv(
                    self.config.train_data_path
                )

                # Dataset should not be empty
                if df.empty:
                    validation_status = False

                # Target column should exist
                if "Attrition" not in df.columns:
                    validation_status = False

            # Create validation directory
            os.makedirs(
                self.config.root_dir,
                exist_ok=True
            )

            # Write validation status
            with open(
                self.config.status_file,
                "w"
            ) as f:

                f.write(
                    f"Validation status: {validation_status}"
                )

            logging.info(
                "Data Validation Completed"
            )

            return validation_status

        except Exception as e:
            raise CustomException(e, sys)
