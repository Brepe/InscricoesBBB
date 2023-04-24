from pymongo import mongo_client, ASCENDING
import pymongo
#from app.config import settings
MONGO_url = "mongodb://localhost:27017"
client = mongo_client.MongoClient(MONGO_url)
print('Conectando ao MongoDB...')

db = client["inscricoesbbb"]
User = db.users
User.create_index([("email", ASCENDING)], unique=True)