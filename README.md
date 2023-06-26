# Introduction

This dashboard was created with the [streamlit.io](https://streamlit.io/) Python package. A future repository built by FastAPI is planned to be added in the future.

# Getting Started

Firstly, create a virtual environment:

`python3 -m venv venv`

Activate it by executing

`source venv/bin/activate`

After that, install required packages by calling

`pip install -r requirements.txt`

**Note**: Remember to update requirements by calling `pip freeze > requirements.txt` when new packages are added.

Finally, in the root directory, run the command `streamlit run Login.py`.

# Testing Changestreams

There are two files of interest:

- `test_data_editor.py` allows you to edit a dataframe
- `test_data_viewer.py` allows you to view changes to the dataframe in real-time, receiving changes made from `test_data_editor.py`

The other files that are prefixed with `test` were created while testing Streamlit's compatability with MongoDB.

# Additional Information for Developers

## Frontend

Currently, Streamlit serves as the frontend library for rendering components. It's possible to create [custom components](https://docs.streamlit.io/library/components/create).

## Authentication

Authentication is currently being provided by [Google's OAuth2 authentication](https://developers.google.com/identity/protocols/oauth2).
