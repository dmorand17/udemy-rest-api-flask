from flask.config import Config
import yaml
from app_logging import AppLogger

logger = AppLogger(__name__).get_logger()
DEFAULT_CONFIG = "config.yaml"

class ConfigManager:
    _instance = None

    def __init__(self, config_file=DEFAULT_CONFIG):
        if ConfigManager._instance != None:
            raise Exception("This class is a singleton!")
        else:
            logger.info("Initialized ConfigManager")
            self.config_file = config_file
            with open(self.config_file, "r") as yml:
                cfg = yaml.safe_load(yml)
            self.cfg = cfg
            ConfigManager._instance = self

    @staticmethod
    def getInstance():
        if ConfigManager._instance is None:
            ConfigManager()
            # Put any initialization here.
        return ConfigManager._instance

    @staticmethod
    def get(name, default=None):
        return ConfigManager.getInstance().cfg.get(name, default)
