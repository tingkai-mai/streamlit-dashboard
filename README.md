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

# Additional Information for Developers

## Frontend

Currently, Streamlit serves as the frontend library for rendering components. It's possible to create [custom components](https://docs.streamlit.io/library/components/create).

## Authentication

Authentication is currently being provided by [Google's OAuth2 authentication](https://developers.google.com/identity/protocols/oauth2).
