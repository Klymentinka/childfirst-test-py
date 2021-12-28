import os
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)
LANDING_URL = os.environ.get("LANDING_URL", None)