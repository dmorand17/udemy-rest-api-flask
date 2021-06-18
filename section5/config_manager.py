import yaml

DEFAULT_CONFIG = "config.yaml"


class ConfigManager:
    def __init__(self, config_file=DEFAULT_CONFIG):
        self.config_file = config_file
        with open(self.config_file, "r") as yml:
            self.cfg = yaml.load(yml)

    def get(self, name, default=None):
        return self.cfg.get(name, default)
