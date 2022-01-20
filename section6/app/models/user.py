from connection.db import DbConnection, db
from app_logger import AppLogger

logger = AppLogger.get_logger(__name__)

#
# Internal representation of User
#
class UserModel(db.Model):

    # sqlalchemy configuration
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, _id, username, password, email):
        self.id = _id
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def find_by_username(cls, username):
        with DbConnection() as db:
            query = "SELECT * FROM users WHERE username = ?"
            result = db.cursor.execute(query, (username,))
            row = result.fetchone()
            if row:
                user = cls(*row)
            else:
                logger.error("No user found!")
                user = None

            return user

    @classmethod
    def find_by_email(cls, email):
        with DbConnection() as db:
            query = "SELECT * FROM users WHERE email = ?"
            result = db.cursor.execute(query, (email,))
            row = result.fetchone()
            if row:
                user = cls(*row)
            else:
                logger.error("No user found!")
                user = None

            return user

    @classmethod
    def find_by_id(cls, _id):
        with DbConnection() as db:
            query = "SELECT * FROM users WHERE id = ?"

            result = db.cursor.execute(query, (_id,))
            row = result.fetchone()
            if row:
                user = cls(*row)
            else:
                user = None

            return user

    def __repr__(self) -> str:
        return f"id: {self.id}, username: {self.username}, email: {self.email}, password: {self.password}"
