import sqlite3
import argparse
import yaml
import pathlib
from pathlib import Path

import os, sys

# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)

# Import parent libs
from app_logger import AppLogger
from config_manager import ConfigManager
from utils import AppUtils

logger = AppLogger.get_logger(__name__)

DEFAULT_DB = "data.db"


class DbInit:
    @staticmethod
    def users():
        with DbConnection() as db:
            logger.info("Initializing users")
            create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text, email text)"  # INTEGER PRIMARY KEY allows Auto incrementing id
            db.cursor.execute(create_table)

    @staticmethod
    def items():
        with DbConnection() as db:
            logger.info("Initializing items")
            create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"  # INTEGER PRIMARY KEY allows Auto incrementing id
            db.cursor.execute(create_table)

    @staticmethod
    def all():
        logger.info("Running full initialization")
        DbInit.users()
        DbInit.items()


class DbConnection:
    def __init__(self):
        self.db_file = ConfigManager.get("database", Path(__file__).parent / DEFAULT_DB)

        # if not AppUtils.path_exists(DATABASE):
        #    logger.error("Unable to resolve database at {}, exiting.".format(DATABASE))
        #    sys.exit(1)
        #    pass
        # else:
        #    # logger.info("Database resolved: {}".format(DATABASE))
        #    pass

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
        choices=["users", "items", "all"],
        default="all",
    )
    return parser.parse_args()


if __name__ == "__main__":
    init_functions = {"all": DbInit.all, "users": DbInit.users, "items": DbInit.items}

    args = parse_args()
    init = args.init
    init_functions[init]()
