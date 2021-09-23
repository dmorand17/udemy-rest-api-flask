from connection.db import DbConnection
from app_logging import AppLogger

logger = AppLogger.get_logger(__name__)

#
# Internal representation of Item
#
class ItemModel:
    def __init__(self, name, price, _id=None):
        self.id = _id
        self.name = name
        self.price = price

    def json(self):
        return {"id": self.id, "name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name):
        with DbConnection() as db:
            query = "SELECT name, price, id FROM items WHERE name = ?"
            result = db.cursor.execute(query, (name,))
            row = result.fetchone()

            if row:
                logger.info(f"row: {row}")
                return cls(*row)

    @classmethod
    def find_by_id(cls, _id):
        with DbConnection() as db:
            query = "SELECT name, price, id FROM items WHERE id = ?"
            result = db.cursor.execute(query, (_id,))
            row = result.fetchone()

            if row:
                return cls(*row)

    def insert(self):
        with DbConnection() as db:
            query = "INSERT INTO items VALUES (NULL, ?, ?)"
            db.cursor.execute(query, (self.name, self.price))

    def update(self):
        with DbConnection() as db:
            query = "UPDATE items SET price=? WHERE name=?"
            db.cursor.execute(query, (self.name, self.price))

    def __repr__(self) -> str:
        return f"id: {self.id}, name: {self.name}, price: {self.price}"
