import yaml
from app_logging import AppLogger

logger = AppLogger.get_logger(__name__)
DEFAULT_CONFIG = "conf/config.yaml"


class ConfigManager:
    __instance = None

    def __init__(self, config_file):
        if ConfigManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            logger.info("Initializing ConfigManager")
            ConfigManager.__instance = self
            self.config_file = config_file

            with open(self.config_file, "r") as yml:
                self.config = yaml.safe_load(yml)

    @staticmethod
    def init(config_file=DEFAULT_CONFIG):
        ConfigManager(config_file)

    @staticmethod
    def getInstance(config_file=None):
        return ConfigManager.__instance

    @staticmethod
    def get(name, default=None):
        return ConfigManager.getInstance().config.get(name, default)

    @staticmethod
    def print_config():
        logger.info("Configuration options:")
        config = ConfigManager.getInstance().config
        for k, v in config.items():
            logger.info(f"    {k}: {v}")

    def __getattr__(self, name):
        return getattr(self._instance)
