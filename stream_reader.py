import pymongo
from dotenv import load_dotenv
import os
from bson.json_util import dumps


def init_connection():
    load_dotenv()
    db_connection_string = "mongodb+srv://Mai:f3ROO53l@cluster0.pjzokgh.mongodb.net/"
    return pymongo.MongoClient(db_connection_string)


def print_initial_data(client):
    print("Printing initial data...")
    print(list(client.find()))


try:
    client = init_connection()
    collection = client["sample_database"]["collection_1"]
    print_initial_data(collection)
    change_stream = collection.watch()
    for change in change_stream:
        print(dumps(change))
        print("")  # for readability only
except Exception as e:
    print("Error occured")
