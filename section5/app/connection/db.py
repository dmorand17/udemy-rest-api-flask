import sqlite3
import argparse
from app_logging import AppLogger
from config_manager import ConfigManager
from utils import AppUtils
import sys
import os
import yaml

logger = AppLogger(__name__).get_logger()

DEFAULT_DB = "resources/data.db"
DATABASE = os.getcwd() + "/" + ConfigManager.get("database", DEFAULT_DB)

if not AppUtils.path_exists(DATABASE):
    logger.error("Unable to resolve database at {}, exiting.".format(DATABASE))
    sys.exit(1)
else:
    logger.info("Database resolved: {}".format(DATABASE))

class DbInit:
    @staticmethod
    def users():
        with DbConnection() as db:
            logger.info("Initializing users")
            create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"  # INTEGER PRIMARY KEY allows Auto incrementing id
            db.cursor.execute(create_table)

    @staticmethod
    def all():
        logger.info("Running full initialization")
        DbInit.users()


class DbConnection:
    def __init__(self):
        self.db_file = DATABASE

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

def parse_args():
    parser = argparse.ArgumentParser(description="Database utility")
    parser.add_argument(
        "-i",
        "--init",
        help="Initialize options",
        choices=["users", "all"],
        required=True,
    )
    return parser.parse_args()


init_functions = {
    "all": DbInit.all,
    "users": DbInit.users,
}

if __name__ == "__main__":
    args = parse_args()
    init = args.init
    init_functions[init]()
