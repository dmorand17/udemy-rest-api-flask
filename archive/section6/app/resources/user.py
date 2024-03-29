from typing import Text
from flask_restful import Resource, reqparse
from models.user import UserModel
from app_logger import AppLogger

logger = AppLogger.get_logger(__name__)

#
# External representation of User
#
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field cannot be left blank!",
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field cannot be left blank!",
    )
    parser.add_argument(
        "email",
        type=str,
        required=True,
        help="This field cannot be left blank!",
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message": "User already exists"}, 409

        user = UserModel(**data)
        user.upsert()

        return {"message": "User created successfully"}, 201
