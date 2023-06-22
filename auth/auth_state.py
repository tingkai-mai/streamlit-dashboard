import streamlit as st
import webbrowser
import os

from dotenv import load_dotenv


class AuthState:
    """This class manages the authentication state of the dashboard."""

    def __init__(self):
        if "token" not in st.session_state:
            st.session_state["token"] = None
        if "user_email" not in st.session_state:
            st.session_state["user_email"] = None
        if "user_id" not in st.session_state:
            st.session_state["user_id"] = None

    def get_token(self):
        return st.session_state["token"]

    def set_token(self, token):
        st.session_state["token"] = token

    def set_user_email(self, email):
        st.session_state["user_email"] = email

    def set_user_id(self, id):
        st.session_state["user_id"] = id

    def get_user_email(self):
        return st.session_state["user_email"]

    def get_user_id(self):
        return st.session_state["user_id"]

    def is_authenticated(self):
        """A method that checks if the user is authenticated. This should be run at the top of each page!"""
        return st.session_state["token"] != None

    def logout_user(self):
        load_dotenv()
        st.session_state["token"] = None
        st.session_state["user_email"] = None
        st.session_state["user_id"] = None
