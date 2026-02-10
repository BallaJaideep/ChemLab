# # pages/upload.py

# import os
# import pandas as pd

# from PyQt5.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QLabel,
#     QPushButton,
#     QFileDialog,
# )
# from PyQt5.QtCore import Qt

# from app_state import AppState
# from db.database import insert_dataset, get_connection


# # ================= REQUIRED CSV COLUMNS =================
# REQUIRED_COLUMNS = [
#     "Equipment Name",
#     "Type",
#     "Flowrate",
#     "Pressure",
#     "Temperature",
# ]


# class UploadPage(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.build_ui()

#     # =====================================================
#     # UI
#     # =====================================================
#     def build_ui(self):
#         layout = QVBoxLayout(self)
#         layout.setAlignment(Qt.AlignCenter)
#         layout.setSpacing(20)

#         title = QLabel("Upload CSV Dataset")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size:22px; font-weight:800;")

#         self.status = QLabel("")
#         self.status.setAlignment(Qt.AlignCenter)

#         btn = QPushButton("Select CSV File")
#         btn.setFixedHeight(42)
#         btn.clicked.connect(self.open_file)

#         layout.addWidget(title)
#         layout.addWidget(btn)
#         layout.addWidget(self.status)

#     # =====================================================
#     # CSV PROCESSING + DATABASE SAVE
#     # =====================================================
#     def open_file(self):
#         path, _ = QFileDialog.getOpenFileName(
#             self,
#             "Select CSV File",
#             "",
#             "CSV Files (*.csv)",
#         )

#         if not path:
#             return

#         try:
#             # ---------- READ CSV ----------
#             df = pd.read_csv(path)
#             df.columns = [c.strip() for c in df.columns]

#             # ---------- VALIDATE ----------
#             for col in REQUIRED_COLUMNS:
#                 if col not in df.columns:
#                     raise ValueError(f"Missing column: {col}")

#             # ---------- CONVERT NUMERIC ----------
#             for col in ["Flowrate", "Pressure", "Temperature"]:
#                 df[col] = pd.to_numeric(df[col], errors="coerce")

#             df.dropna(inplace=True)

#             if df.empty:
#                 raise ValueError("No valid rows found in CSV")

#             # ---------- SAVE DATASET META ----------
#             dataset_id = insert_dataset(
#                 filename=os.path.basename(path),
#                 records=len(df),
#             )

#             # ---------- SAVE ROWS ----------
#             conn = get_connection()
#             cur = conn.cursor()

#             for _, row in df.iterrows():
#                 cur.execute(
#                     """
#                     INSERT INTO dataset_rows (
#                         dataset_id,
#                         equipment_name,
#                         type,
#                         flowrate,
#                         pressure,
#                         temperature
#                     )
#                     VALUES (?, ?, ?, ?, ?, ?)
#                     """,
#                     (
#                         dataset_id,
#                         row["Equipment Name"],
#                         row["Type"],
#                         float(row["Flowrate"]),
#                         float(row["Pressure"]),
#                         float(row["Temperature"]),
#                     ),
#                 )

#             conn.commit()
#             conn.close()

#             # =================================================
#             # UPDATE APP STATE (IMPORTANT PART)
#             # =================================================
#             AppState.dataset = df

#             AppState.summary = {
#                 "total_records": len(df),
#                 "average_flowrate": round(df["Flowrate"].mean(), 2),
#                 "average_pressure": round(df["Pressure"].mean(), 2),
#                 "average_temperature": round(df["Temperature"].mean(), 2),
#                 "type_distribution": df["Type"].value_counts().to_dict(),
#             }

#             # ---------- UI FEEDBACK ----------
#             self.status.setText(
#                 f"Loaded and stored {len(df)} records successfully"
#             )
#             self.status.setStyleSheet(
#                 "color: #16a34a; font-weight:600;"
#             )

#         except Exception as e:
#             self.status.setText(str(e))
#             self.status.setStyleSheet(
#                 "color: #dc2626; font-weight:600;"
#             )


# pages/upload.py

# pages/upload.py

import os
import pandas as pd

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QFrame,
)
from PyQt5.QtCore import Qt

from app_state import AppState
from db.database import insert_dataset, get_connection


REQUIRED_COLUMNS = [
    "Equipment Name",
    "Type",
    "Flowrate",
    "Pressure",
    "Temperature",
]


class UploadPage(QWidget):
    def __init__(self):
        super().__init__()
        self.build_ui()

    # =====================================================
    # UI
    # =====================================================
    def build_ui(self):
        root = QVBoxLayout(self)
        root.setAlignment(Qt.AlignCenter)
        root.setContentsMargins(0, 0, 0, 0)

        # ================= CARD =================
        card = QFrame()
        card.setFixedWidth(480)
        card.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 16px;
                border: 1px solid #e5e7eb;
            }
        """)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(32, 30, 32, 28)
        layout.setSpacing(14)

        # ================= TITLE =================
        title = QLabel("Upload Dataset")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:24px;
            font-weight:900;
            color:#0f172a;
        """)

        hint = QLabel("CSV format only")
        hint.setAlignment(Qt.AlignCenter)
        hint.setStyleSheet("""
            font-size:12px;
            color:#64748b;
        """)

        # ================= BUTTON =================
        btn = QPushButton("Choose CSV File")
        btn.setCursor(Qt.PointingHandCursor)
        btn.setFixedHeight(44)
        btn.setStyleSheet("""
            QPushButton {
                background:#2563eb;
                color:white;
                font-weight:800;
                font-size:14px;
                border-radius:10px;
            }
            QPushButton:hover {
                background:#1d4ed8;
            }
        """)
        btn.clicked.connect(self.open_file)

        # ================= STATUS =================
        self.status = QLabel("")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setWordWrap(False)
        self.status.setStyleSheet("""
            font-size:13px;
        """)

        # ================= ADD =================
        layout.addWidget(title)
        layout.addWidget(hint)
        layout.addSpacing(8)
        layout.addWidget(btn)
        layout.addSpacing(6)
        layout.addWidget(self.status)

        root.addWidget(card)

    # =====================================================
    # CSV PROCESSING + DATABASE SAVE
    # =====================================================
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select CSV File",
            "",
            "CSV Files (*.csv)",
        )

        if not path:
            return

        try:
            df = pd.read_csv(path)
            df.columns = [c.strip() for c in df.columns]

            for col in REQUIRED_COLUMNS:
                if col not in df.columns:
                    raise ValueError(f"Missing column: {col}")

            for col in ["Flowrate", "Pressure", "Temperature"]:
                df[col] = pd.to_numeric(df[col], errors="coerce")

            df.dropna(inplace=True)

            if df.empty:
                raise ValueError("No valid rows found in CSV")

            dataset_id = insert_dataset(
                filename=os.path.basename(path),
                records=len(df),
            )

            conn = get_connection()
            cur = conn.cursor()

            for _, row in df.iterrows():
                cur.execute(
                    """
                    INSERT INTO dataset_rows (
                        dataset_id,
                        equipment_name,
                        type,
                        flowrate,
                        pressure,
                        temperature
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        dataset_id,
                        row["Equipment Name"],
                        row["Type"],
                        float(row["Flowrate"]),
                        float(row["Pressure"]),
                        float(row["Temperature"]),
                    ),
                )

            conn.commit()
            conn.close()

            AppState.dataset = df
            AppState.summary = {
                "total_records": len(df),
                "average_flowrate": round(df["Flowrate"].mean(), 2),
                "average_pressure": round(df["Pressure"].mean(), 2),
                "average_temperature": round(df["Temperature"].mean(), 2),
                "type_distribution": df["Type"].value_counts().to_dict(),
            }

            self.status.setText(
                f"✔ {len(df)} records uploaded successfully"
            )
            self.status.setStyleSheet("""
                font-size:13px;
                color:#16a34a;
                font-weight:700;
            """)

        except Exception as e:
            self.status.setText(f"✖ {str(e)}")
            self.status.setStyleSheet("""
                font-size:13px;
                color:#dc2626;
                font-weight:700;
            """)

