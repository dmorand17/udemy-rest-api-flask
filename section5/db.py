import sqlite3
import argparse
from app_logging import AppLogger
from config_manager import ConfigManager
import sys
import yaml

DEFAULT_DB = "data.db"
DATABASE = ConfigManager.get("database", DEFAULT_DB)
logger = AppLogger(__name__).get_logger()

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
        logger.info("Establishing database connection")
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()
        logger.info("Database connection closed")


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
