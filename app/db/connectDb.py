from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

client = MongoClient(getenv("MONGO_URI"))

authDB = client["Authorization"]


def test_db():
    try:
        client.admin.command("ping")
        return "ok"
    except:
        return "Error"
