import pymongo
from dotenv import load_dotenv
import os
from bson.json_util import dumps
import pandas as pd

import streamlit as st


def init_connection():
    load_dotenv()
    db_connection_string = "mongodb+srv://Mai:f3ROO53l@cluster0.pjzokgh.mongodb.net/"
    return pymongo.MongoClient(db_connection_string)


def cleanup_collection(client):
    client.delete_many({})


def get_initial_data(client):
    data = list(client.find())
    res = []
    for d in data:
        res.append(
            {"col1": int(d["col1"]), "col2": int(d["col2"]), "col3": int(d["col3"])}
        )
    return res


def convert_row(data):
    return pd.DataFrame(
        [
            {
                "col1": data["col1"],
                "col2": data["col2"],
                "col3": data["col3"],
            }
        ]
    )


df = pd.DataFrame(
    [
        {
            "col1": "col1",
            "col2": "col2",
            "col3": "col3",
        }
    ]
)

try:
    client = init_connection()
    collection = client["sample_database"]["collection_1"]
    cleanup_collection(collection)

    st.markdown("# Table Data")
    table = st.dataframe(df)
    change_stream = collection.watch()
    for change in change_stream:
        print("Change observed")
        new_row = convert_row(change["fullDocument"])
        print("Appending new row:", new_row)
        table.add_rows(new_row)

except Exception as e:
    print(e)
