import pymongo
import pandas as pd
import json
from bson import json_util
from bson.objectid import ObjectId
from saved_state import SavedState

import streamlit as st


@st.cache_resource
def init_connection():
    db_connection_string = "mongodb+srv://Mai:f3ROO53l@cluster0.pjzokgh.mongodb.net/"
    client = pymongo.MongoClient(db_connection_string)
    animals_client = client["sample_database"]["animals_collection"]
    return animals_client


def cleanup_data(client):
    client.delete_many({})


def load_data(_client):
    json_data = list(_client.find())
    df = pd.DataFrame(json_data)
    return df


def get_json(data):
    json_objects = []
    for index, row in data.iterrows():
        row_dict = row.to_dict()
        row_dict["index"] = index
        json_data = json.loads(json_util.dumps(row_dict))
        json_objects.append(json_data)
    return json_objects


def get_updated_json(data, new_values):
    for k, v in new_values.items():
        if k in data:
            data[k] = v
    return data


def handle_change(data, table, df):
    st.experimental_rerun()
    opType = data["operationType"]
    if opType == "update":
        print("Update observed")
    elif opType == "insert":
        print("Insert observed")
    elif opType == "delete":
        print("Delete observed")
    else:
        print("Unhandled operation observed:", opType)


def main():
    client = init_connection()
    df = load_data(client)
    table = st.dataframe(df)

    change_stream = client.watch()
    for change in change_stream:
        handle_change(change, table, df)


main()
