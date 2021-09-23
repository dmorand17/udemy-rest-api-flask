import yaml
import os, sys
from app_logger import AppLogger

logger = AppLogger.get_logger(__name__)


class ConfigManager:
    __instance = None

    def __init__(self):
        if ConfigManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.config_file = os.environ.get("UDEMY_RESTAPI_CONFIG")
            if self.config_file is None:
                print(
                    "No configuration found.  Ensure that 'UDEMY_RESTAPI_CONFIG' environment variable is set"
                )
                sys.exit(1)
            ConfigManager.__instance = self
            logger.info("Initializing ConfigManager")
            with open(self.config_file, "r") as yml:
                self.config = yaml.safe_load(yml)

    @staticmethod
    def init():
        ConfigManager()

    @staticmethod
    def getInstance():
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
