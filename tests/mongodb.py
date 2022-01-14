from pymongo import MongoClient
import re
import settings


class MongoDB():
    COLLECTION_PARENTS = 'parents'

    def __init__(self):
        client = MongoClient(f'mongodb+srv://{settings.MONGO_DB_USER}:{settings.MONGO_DB_PASSWORD}@{settings.MONGO_DB_HOST}/?retryWrites=true&w=majority', 27017, maxPoolSize=50)  
        self.db = client[settings.MONGO_DB_DATABASE]

    def clean_test_parents(self):
        collection = self.db[self.COLLECTION_PARENTS]
        collection.delete_many({'email': re.compile("^test.*", re.IGNORECASE)})    
