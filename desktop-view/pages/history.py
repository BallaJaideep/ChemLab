# # pages/history.py

# from PyQt5.QtWidgets import (
#     QWidget, QVBoxLayout, QLabel,
#     QTableWidget, QTableWidgetItem,
#     QPushButton, QFileDialog, QHBoxLayout
# )

# from app_state import AppState
# from utils.pdf_report import generate_pdf_report


# class HistoryPage(QWidget):
#     def __init__(self, on_navigate):
#         super().__init__()
#         self.on_navigate = on_navigate
#         self.build_ui()

#     def build_ui(self):
#         layout = QVBoxLayout(self)
#         layout.setSpacing(16)

#         title = QLabel("Dataset History")
#         title.setStyleSheet("font-size:22px; font-weight:800;")
#         layout.addWidget(title)

#         self.table = QTableWidget()
#         self.table.setColumnCount(5)
#         self.table.setHorizontalHeaderLabels(
#             ["#", "Dataset", "Records", "Status", "Actions"]
#         )
#         self.table.verticalHeader().setVisible(False)
#         layout.addWidget(self.table)

#     def on_show(self):
#         self.refresh()

#     def refresh(self):
#         history = AppState.load_history()
#         self.table.setRowCount(len(history))

#         for row, item in enumerate(history):
#             self.table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
#             self.table.setItem(row, 1, QTableWidgetItem(item["filename"]))
#             self.table.setItem(row, 2, QTableWidgetItem(str(item["records"])))
#             self.table.setItem(row, 3, QTableWidgetItem(item["status"]))

#             actions = QWidget()
#             btn_layout = QHBoxLayout(actions)
#             btn_layout.setContentsMargins(0, 0, 0, 0)

#             view_btn = QPushButton("View")
#             pdf_btn = QPushButton("PDF")

#             dataset_id = item["id"]

#             view_btn.clicked.connect(
#                 lambda _, d=dataset_id: self.view_dataset(d)
#             )
#             pdf_btn.clicked.connect(
#                 lambda _, d=dataset_id: self.export_pdf(d)
#             )

#             btn_layout.addWidget(view_btn)
#             btn_layout.addWidget(pdf_btn)
#             self.table.setCellWidget(row, 4, actions)

#     def view_dataset(self, dataset_id):
#         AppState.load_dataset_by_id(dataset_id)
#         self.on_navigate("dataset_view")  # ✅ FIXED

#     def export_pdf(self, dataset_id):
#         meta = AppState.get_dataset_meta(dataset_id)
#         if not meta or not AppState.summary:
#             return

#         path, _ = QFileDialog.getSaveFileName(
#             self,
#             "Save PDF",
#             meta["filename"].replace(".csv", "_report.pdf"),
#             "PDF Files (*.pdf)"
#         )

#         if path:
#             generate_pdf_report(
#                 meta["filename"],
#                 AppState.summary,
#                 path
#             )


# pages/history.py

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem,
    QPushButton, QFileDialog,
    QHBoxLayout, QFrame
)
from PyQt5.QtCore import Qt

from app_state import AppState
from utils.pdf_report import generate_pdf_report


class HistoryPage(QWidget):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate
        self.build_ui()

    # =====================================================
    def build_ui(self):
        root = QVBoxLayout(self)
        root.setSpacing(24)
        root.setContentsMargins(36, 30, 36, 24)

        # ================= HEADER =================
        header = QVBoxLayout()
        header.setSpacing(6)

        title = QLabel("Dataset History")
        title.setStyleSheet("""
            font-size:26px;
            font-weight:900;
            color:#0f172a;
        """)

        subtitle = QLabel(
            "Previously processed datasets and exported reports"
        )
        subtitle.setStyleSheet("""
            font-size:14px;
            color:#64748b;
        """)

        header.addWidget(title)
        header.addWidget(subtitle)
        root.addLayout(header)

        # ================= TABLE CARD =================
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background:white;
                border-radius:16px;
                border:1px solid #e5e7eb;
            }
        """)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(14, 14, 14, 14)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["#", "Dataset", "Records", "Status", "Actions"]
        )

        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionMode(QTableWidget.NoSelection)
        self.table.setAlternatingRowColors(True)

        self.table.setStyleSheet("""
            QTableWidget {
                border:none;
                font-size:13px;
            }
            QHeaderView::section {
                background:#f8fafc;
                padding:8px;
                font-weight:800;
                border:none;
                border-bottom:1px solid #e5e7eb;
            }
            QTableWidget::item {
                padding:6px;
            }
        """)

        card_layout.addWidget(self.table)
        root.addWidget(card)

    # =====================================================
    def on_show(self):
        self.refresh()

    # =====================================================
    def refresh(self):
        # ✅ SHOW ONLY LAST 5 DATASETS
        history = AppState.load_history()[:5]

        self.table.setRowCount(len(history))

        for row, item in enumerate(history):
            self.table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.table.setItem(row, 1, QTableWidgetItem(item["filename"]))
            self.table.setItem(row, 2, QTableWidgetItem(str(item["records"])))
            self.table.setItem(row, 3, QTableWidgetItem(item["status"]))

            # ---------- ACTION BUTTONS ----------
            actions = QWidget()
            btn_layout = QHBoxLayout(actions)
            btn_layout.setContentsMargins(0, 0, 0, 0)
            btn_layout.setSpacing(8)

            view_btn = QPushButton("View")
            pdf_btn = QPushButton("PDF")

            view_btn.setFixedHeight(28)
            pdf_btn.setFixedHeight(28)

            view_btn.setStyleSheet("""
                QPushButton {
                    background:#eff6ff;
                    color:#1d4ed8;
                    font-weight:700;
                    border-radius:6px;
                    padding:0 14px;
                    border:1px solid #bfdbfe;
                }
                QPushButton:hover {
                    background:#dbeafe;
                }
            """)

            pdf_btn.setStyleSheet("""
                QPushButton {
                    background:#f8fafc;
                    color:#0f172a;
                    font-weight:700;
                    border-radius:6px;
                    padding:0 14px;
                    border:1px solid #e5e7eb;
                }
                QPushButton:hover {
                    background:#f1f5f9;
                }
            """)

            dataset_id = item["id"]

            view_btn.clicked.connect(
                lambda _, d=dataset_id: self.view_dataset(d)
            )
            pdf_btn.clicked.connect(
                lambda _, d=dataset_id: self.export_pdf(d)
            )

            btn_layout.addWidget(view_btn)
            btn_layout.addWidget(pdf_btn)

            self.table.setCellWidget(row, 4, actions)

        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(4, 170)

    # =====================================================
    def view_dataset(self, dataset_id):
        AppState.load_dataset_by_id(dataset_id)
        self.on_navigate("dataset_view")

    # =====================================================
    def export_pdf(self, dataset_id):
        meta = AppState.get_dataset_meta(dataset_id)
        if not meta or not AppState.summary:
            return

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save PDF",
            meta["filename"].replace(".csv", "_report.pdf"),
            "PDF Files (*.pdf)"
        )

        if path:
            generate_pdf_report(
                meta["filename"],
                AppState.summary,
                path
            )
