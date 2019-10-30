import os
from pymongo import MongoClient

mongodb_host = os.environ["MONGO_HOST"]
mongodb_port = int(os.environ["MONGO_PORT"])
mongo_database = os.environ["MONGO_DATABASE"]
mongo_collection = os.environ["MONGO_COLLECTION"]
mongo_username = os.environ["MONGO_NON_ROOT_USERNAME"]
mongo_password = os.environ["MONGO_NON_ROOT_PASSWORD"]

mongo_client = MongoClient(mongodb_host, mongodb_port, username=mongo_username, password=mongo_password, authSource=mongo_database)

def getConfig():
    config = mongo_client[mongo_database][mongo_collection].find_one()
    if config is not None:
        del config["_id"]
    return config

def putConfig(body):
    return mongo_client[mongo_database][mongo_collection].replace_one({}, body, upsert=True).modified_count

            
        
