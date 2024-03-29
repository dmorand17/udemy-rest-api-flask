from werkzeug.security import safe_str_cmp
from user import User
from app_logging import AppLogger

logger = AppLogger.get_logger(__name__)


def authenticate(email, password):
    user = User.find_by_email(email)
    if user and safe_str_cmp(user.password, password):
        return user
    else:
        logger.error("Incorrect password")


def identity(payload):
    user_id = payload["identity"]
    return User.find_by_id(user_id)
