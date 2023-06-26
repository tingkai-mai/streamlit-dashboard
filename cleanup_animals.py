import pymongo

db_connection_string = "mongodb+srv://Mai:f3ROO53l@cluster0.pjzokgh.mongodb.net/"
client = pymongo.MongoClient(db_connection_string)
animals_client = client["sample_database"]["animals_collection"]
animals_client.delete_many({})
