# app_state.py

import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("data.db")


class AppState:
    dataset = None
    summary = {}

    # =====================================================
    @staticmethod
    def _connect():
        return sqlite3.connect(DB_PATH)

    # =====================================================
    # LOAD DATASET HISTORY (LIST VIEW)
    # =====================================================
    @staticmethod
    def load_history():
        conn = AppState._connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, filename, records
            FROM datasets
            ORDER BY id DESC
        """)

        rows = cur.fetchall()
        conn.close()

        return [
            {
                "id": r[0],
                "filename": r[1],
                "records": r[2],
                "status": "Verified",  # UI-only
            }
            for r in rows
        ]

    # =====================================================
    # LOAD DATASET + COMPUTE FULL SUMMARY
    # =====================================================
    @staticmethod
    def load_dataset_by_id(dataset_id):
        conn = AppState._connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT
                equipment_name,
                type,
                flowrate,
                pressure,
                temperature
            FROM dataset_rows
            WHERE dataset_id = ?
        """, (dataset_id,))

        rows = cur.fetchall()
        conn.close()

        if not rows:
            AppState.dataset = None
            AppState.summary = {}
            return

        df = pd.DataFrame(
            rows,
            columns=[
                "Equipment Name",
                "Type",
                "Flowrate",
                "Pressure",
                "Temperature",
            ],
        )

        # -------- STORE DATAFRAME --------
        AppState.dataset = df

        # -------- 🔥 FULL SUMMARY --------
        AppState.summary = {
            "total_records": len(df),
            "average_flowrate": round(df["Flowrate"].mean(), 2),
            "average_pressure": round(df["Pressure"].mean(), 2),
            "average_temperature": round(df["Temperature"].mean(), 2),
            "type_distribution": df["Type"].value_counts().to_dict(),
        }

    # =====================================================
    # DATASET META (FOR PDF / HISTORY)
    # =====================================================
    @staticmethod
    def get_dataset_meta(dataset_id):
        conn = AppState._connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT filename, records
            FROM datasets
            WHERE id = ?
        """, (dataset_id,))

        row = cur.fetchone()
        conn.close()

        if not row:
            return None

        return {
            "filename": row[0],
            "records": row[1],
            "status": "Verified",
        }
