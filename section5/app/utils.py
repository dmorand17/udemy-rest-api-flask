from app_logging import AppLogger
import os.path
import sys

logger = AppLogger(__name__).get_logger()

class AppUtils():
    @staticmethod
    def path_exists(path):
        if not os.path.exists(path):
            logger.error("Path does not exist: {}".format(path))
            return False
        return True
