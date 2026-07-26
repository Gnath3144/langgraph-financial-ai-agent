import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
USE_MOCK_LLM = os.getenv("USE_MOCK_LLM", "True").lower() in ("true", "1", "yes")
DB_PATH = "state_db.sqlite"
