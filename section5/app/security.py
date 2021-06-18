from werkzeug.security import safe_str_cmp
from user import User
from app_logging import AppLogger

logger = AppLogger(__name__).get_logger()


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    else:
        logger.error("Incorrect password")


def identity(payload):
    user_id = payload["identity"]
    return User.find_by_id(user_id)
