import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
from src.agent.config import DB_PATH

def get_sqlite_checkpointer():
    # Persistence checkpointer using local SQLite database
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return SqliteSaver(conn)
