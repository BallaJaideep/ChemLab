
import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path("data.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS datasets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                records INTEGER NOT NULL,
                uploaded_at TEXT NOT NULL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS dataset_rows (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dataset_id INTEGER,
                equipment_name TEXT,
                type TEXT,
                flowrate REAL,
                pressure REAL,
                temperature REAL
            )
        """)

        conn.commit()


def insert_dataset(filename, records):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO datasets (filename, records, uploaded_at)
            VALUES (?, ?, ?)
            """,
            (filename, records,
             datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        conn.commit()
        return cur.lastrowid
