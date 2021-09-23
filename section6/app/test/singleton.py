import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# Import parent libs
from app_logging import AppLogger
from config_manager import ConfigManager
import logging
from user import User

logger = AppLogger.get_logger(__name__, level=logging.INFO, log_file="test.log")

if __name__ == "__main__":
    logger.info("info statement")
    logger.debug("debug statement")

    jwt_secret = ConfigManager.get("jwt_secret", "jose")

    logger.info(f"jwt_secret: {jwt_secret}")
    user = User.find_by_username("douglas")
    logger.info(f"user: {user}")

    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    logger.info(f"currentdir: {currentdir}, parentdir: {parentdir}")
