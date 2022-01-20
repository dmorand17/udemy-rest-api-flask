import yaml
from app_logging import AppLogger

logger = AppLogger.get_logger(__name__)

DEFAULT_CONFIG = "conf/config.yaml"


class ConfigManager:
    __instance = None

    def __init__(self, config_file=DEFAULT_CONFIG):
        if ConfigManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            logger.info("Initializing ConfigManager")
            ConfigManager.__instance = self
            self.config_file = config_file

            with open(self.config_file, "r") as yml:
                cfg = yaml.safe_load(yml)
            self.cfg = cfg

    @staticmethod
    def getInstance():
        if not ConfigManager.__instance:
            logger.info("No ConfigManager found, creating new...")
            ConfigManager()
        return ConfigManager.__instance

    @staticmethod
    def get(name, default=None):
        return ConfigManager.getInstance().cfg.get(name, default)

    @staticmethod
    def print_config():
        logger.info("Configuration options:")
        cfg = ConfigManager.getInstance().cfg
        for k, v in cfg.items():
            logger.info(f"    {k}: {v}")

    def __getattr__(self, name):
        return getattr(self._instance)
