import streamlit as st
import pymongo
from dotenv import load_dotenv
import os


@st.cache_resource
def init_connection():
    load_dotenv()
    db_connection_string = os.environ["MONGO_DEV_URL"]
    return pymongo.MongoClient(db_connection_string)


client = init_connection()


@st.cache_data(ttl=600)
def get_data():
    print("Calling data")
    db = client["PolymerizeLab"]
    items = db["company"].find()
    items = list(items)
    return items


items = get_data()


@st.cache_data
def print_data():
    print(f"Printing data of length {len(items)}")
    for item in items:
        st.write(item)


print_data()
