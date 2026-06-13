from src.config.configuration import ConfigurationManager

config = ConfigurationManager()

data_transformation_config = (
    config.get_data_transformation_config()
)

print(data_transformation_config)
