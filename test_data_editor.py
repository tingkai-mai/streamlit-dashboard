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
    initialize_data(animals_client)
    return animals_client


def initialize_data(client):
    data = [
        {
            "species": "Lion",
            "weight": 190,
            "is_endangered": True,
            "classification": "Mammal",
            "average_lifespan": 12,
            "habitat": "Grassland",
        },
        {
            "species": "Crocodile",
            "weight": 430,
            "is_endangered": True,
            "classification": "Reptile",
            "average_lifespan": 70,
            "habitat": "Water",
        },
        {
            "species": "Elephant",
            "weight": 5000,
            "is_endangered": True,
            "classification": "Mammal",
            "average_lifespan": 70,
            "habitat": "Savannah",
        },
        {
            "species": "Giraffe",
            "weight": 800,
            "is_endangered": False,
            "classification": "Mammal",
            "average_lifespan": 25,
            "habitat": "Savannah",
        },
        {
            "species": "Penguin",
            "weight": 4,
            "is_endangered": False,
            "classification": "Bird",
            "average_lifespan": 20,
            "habitat": "Antarctica",
        },
    ]
    for animal in data:
        client.insert_one(animal)


def cleanup_data(client):
    client.delete_many({})


@st.cache_data
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


def get_changes(operation: str, df: pd.DataFrame, client):
    """Returns a list of affected rows after a specific operation
    An operation can be three states:
    - "edited_rows"
    - "added_rows"
    - "deleted_rows"
    """
    target_data = st.session_state["data_editor"][operation]
    if operation == "edited_rows":
        indexes = list(target_data.keys())
        current_data = get_json(df.loc[list(map(lambda x: int(x), indexes))])
        new_data = []
        for _, data in enumerate(current_data):
            new_data.append(get_updated_json(data, target_data[data["index"]]))
        perform_edit(new_data, client)
        return new_data

    elif operation == "added_rows":
        # Only add the row once ALL data in every column is filled up
        columns = set(df.columns)
        columns.remove("_id")
        for data in target_data:
            if set(data.keys()) == columns:
                perform_add(data, client)
        return target_data

    elif operation == "deleted_rows":
        for data in target_data:
            perform_delete(df.loc[data], client)
        return target_data

    raise Exception("Invalid operation")


def perform_edit(edited_data, client):
    for data in edited_data:
        document_id_string = data["_id"]["$oid"]
        document_id = ObjectId(document_id_string)

        # Perform change
        new_data = json.loads(
            json.dumps({key: value for key, value in data.items() if key != "_id"})
        )
        update_op = {"$set": new_data}
        client.update_one({"_id": document_id}, update_op)


def perform_add(new_data, client):
    new_data = json.loads(
        json.dumps({key: value for key, value in new_data.items() if key != "_id"})
    )
    client.insert_one(new_data)


def perform_delete(deleted_data, client):
    document_id = ObjectId(deleted_data["_id"])
    client.delete_one({"_id": document_id})


def main():
    client = init_connection()
    df = load_data(client)
    st.data_editor(df, key="data_editor", num_rows="dynamic")

    edited_rows = get_changes("edited_rows", df, client)
    added_rows = get_changes("added_rows", df, client)
    deleted_rows = get_changes("deleted_rows", df, client)

    st.write("Here's the session state:")
    st.write(st.session_state["data_editor"])

    st.write("Edited rows:")
    st.write(edited_rows)

    st.write("Added rows:")
    st.write(added_rows)

    st.write("Deleted rows:")
    st.write(deleted_rows)
    print("=====================================================")


main()
