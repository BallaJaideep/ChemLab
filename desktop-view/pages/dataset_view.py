
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton,
    QFrame
)
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from app_state import AppState



class BarChart(FigureCanvasQTAgg):
    def __init__(self, distribution):
        fig = Figure(figsize=(5, 3))
        super().__init__(fig)

        ax = fig.add_subplot(111)

        labels = list(distribution.keys())
        values = list(distribution.values())

        ax.bar(labels, values, color="#2563eb")
        ax.set_ylabel("Count")
        ax.set_xlabel("Equipment Type")
        ax.grid(axis="y", linestyle="--", alpha=0.4)
        ax.tick_params(axis="x", rotation=30)

        fig.tight_layout()


class DatasetViewPage(QWidget):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate
        self.build_ui()

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setSpacing(24)
        root.setContentsMargins(36, 30, 36, 24)

        header = QHBoxLayout()

        self.title = QLabel("Dataset Summary")
        self.title.setStyleSheet("""
            font-size:26px;
            font-weight:900;
            color:#0f172a;
        """)

        back_btn = QPushButton("← Back to History")
        back_btn.setFixedHeight(36)
        back_btn.setCursor(Qt.PointingHandCursor)
        back_btn.setStyleSheet("""
            QPushButton {
                background:#f1f5f9;
                border:1px solid #e5e7eb;
                border-radius:8px;
                padding:0 16px;
                font-weight:700;
            }
            QPushButton:hover {
                background:#e2e8f0;
            }
        """)
        back_btn.clicked.connect(lambda: self.on_navigate("history"))

        header.addWidget(self.title)
        header.addStretch()
        header.addWidget(back_btn)

        root.addLayout(header)

        self.summary_layout = QHBoxLayout()
        self.summary_layout.setSpacing(16)
        root.addLayout(self.summary_layout)

        mid = QHBoxLayout()
        mid.setSpacing(20)

        self.dist_card = QFrame()
        self.dist_card.setStyleSheet("""
            QFrame {
                background:white;
                border-radius:16px;
                border:1px solid #e5e7eb;
            }
        """)

        self.dist_box = QVBoxLayout(self.dist_card)
        self.dist_box.setContentsMargins(18, 16, 18, 16)
        self.dist_box.setSpacing(8)

        self.chart_card = QFrame()
        self.chart_card.setStyleSheet("""
            QFrame {
                background:white;
                border-radius:16px;
                border:1px solid #e5e7eb;
            }
        """)

        self.chart_box = QVBoxLayout(self.chart_card)
        self.chart_box.setContentsMargins(18, 16, 18, 16)

        mid.addWidget(self.dist_card, 1)
        mid.addWidget(self.chart_card, 2)

        root.addLayout(mid)

        
        table_card = QFrame()
        table_card.setStyleSheet("""
            QFrame {
                background:white;
                border-radius:16px;
                border:1px solid #e5e7eb;
            }
        """)

        table_layout = QVBoxLayout(table_card)
        table_layout.setContentsMargins(14, 14, 14, 14)

        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("""
            QTableWidget {
                border:none;
                font-size:13px;
            }
            QHeaderView::section {
                background:#f8fafc;
                padding:6px;
                font-weight:700;
                border: none;
                border-bottom:1px solid #e5e7eb;
            }
        """)

        table_layout.addWidget(self.table)
        root.addWidget(table_card)


    def on_show(self):
        df = AppState.dataset
        summary = AppState.summary

        if df is None or df.empty:
            return

        self._clear_layout(self.summary_layout)
        self._clear_layout(self.dist_box)
        self._clear_layout(self.chart_box)

        stats = {
            "Total Records": summary["total_records"],
            "Average Flowrate": round(df["Flowrate"].mean(), 2),
            "Average Pressure": round(df["Pressure"].mean(), 2),
            "Average Temperature": round(df["Temperature"].mean(), 2),
        }

        for label, value in stats.items():
            self.summary_layout.addWidget(
                self._stat_card(label, value)
            )

        dist_title = QLabel("Equipment Type Distribution")
        dist_title.setStyleSheet("""
            font-size:18px;
            font-weight:800;
            color:#0f172a;
        """)
        self.dist_box.addWidget(dist_title)

        for k, v in summary["type_distribution"].items():
            lbl = QLabel(f"{k} — {v}")
            lbl.setStyleSheet("""
                font-size:14px;
                color:#475569;
            """)
            self.dist_box.addWidget(lbl)

        self.dist_box.addStretch()

        chart = BarChart(summary["type_distribution"])
        self.chart_box.addWidget(chart)

        
        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns.tolist())

        for r in range(len(df)):
            for c in range(len(df.columns)):
                self.table.setItem(
                    r, c,
                    QTableWidgetItem(str(df.iat[r, c]))
                )

        self.table.resizeColumnsToContents()

    
    def _stat_card(self, title, value):
        box = QFrame()
        box.setFixedHeight(96)
        box.setStyleSheet("""
            QFrame {
                background:white;
                border-radius:14px;
                border:1px solid #e5e7eb;
            }
        """)

        layout = QVBoxLayout(box)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(4)

        t = QLabel(title)
        t.setStyleSheet("""
            font-size:12px;
            font-weight:600;
            color:#64748b;
        """)

        v = QLabel(str(value))
        v.setStyleSheet("""
            font-size:22px;
            font-weight:900;
            color:#0f172a;
        """)

        layout.addWidget(t)
        layout.addWidget(v)
        layout.addStretch()

        return box

    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
