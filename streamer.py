import pymongo
from dotenv import load_dotenv
from time import sleep


def init_connection():
    load_dotenv()
    db_connection_string = "mongodb+srv://Mai:f3ROO53l@cluster0.pjzokgh.mongodb.net/"
    return pymongo.MongoClient(db_connection_string)


client = init_connection()

id = 0
while True:
    print(f"Streaming item into database with ID {id}")
    client["sample_database"]["collection_1"].insert_one(
        {f"col1": f"value{id}", "col2": f"value{id}", "col3": f"value{id}"}
    )
    id += 1
    # if id == 1:
    # break
    # sleep(2)
