import os
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)
LANDING_URL = os.environ.get("LANDING_URL", None)
MONGO_DB_USER = os.environ.get("MONGO_DB_USER", None)
MONGO_DB_PASSWORD = os.environ.get("MONGO_DB_PASSWORD", None)
MONGO_DB_DATABASE = os.environ.get("MONGO_DB_DATABASE", None)
MONGO_DB_HOST = os.environ.get("MONGO_DB_HOST", None)
PROJECT_PATH = os.environ.get("PROJECT_PATH", None)