
from pymongo import MongoClient
import json

class DbService:
    dbName = "yaohaoDB"
    mongoClient = None
    collection = "yaohao"

    def __init__(self):
        self.client = MongoClient("localhost", 27017)

    def get_collection(self):
        db = self.client.yaohaoDB
        col = db.data
        return col

    def insert_data(self):
        pass

