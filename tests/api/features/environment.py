import os
from dotenv import load_dotenv

def before_all(context):
    # Load .env file
    load_dotenv()  # loads from root .env by default

    context.base_url = os.getenv("BASE_URL")
    context.token = os.getenv("TOKEN")

    context.headers = {
        "Content-Type": "application/json"
    }

    if context.token:
        context.headers["Authorization"] = f"Bearer {context.token}"