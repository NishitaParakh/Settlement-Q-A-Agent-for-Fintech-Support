import sqlite3
from pathlib import Path

db_path = Path("database\database.py").parent / "settlement.db"

def get_connection():
    return sqlite3.connect(db_path)



