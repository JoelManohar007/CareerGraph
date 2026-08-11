import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")


def create_driver():
    if not URI or not USERNAME or not PASSWORD:
        raise RuntimeError("CognoDB environment variables are missing.")

    return GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD),
    )