from flask_pymongo import MongoClient
import os




def get_db():
    mongo_uri = os.environ.get("MONGO_URI")
    mongo_client = MongoClient(mongo_uri)
    return mongo_client.get_database()
