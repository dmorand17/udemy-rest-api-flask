import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from app_logging import AppLogger
from models.item import ItemModel
from models.user import UserModel

logger = AppLogger.get_logger(__name__)

if __name__ == "__main__":
    # Create Users
    ItemModel(None, "chair", "12.99").insert()
    ItemModel(None, "desk", "199.99").insert()
    ItemModel(None, "lamp", "29.99").insert()

    # Create Items
