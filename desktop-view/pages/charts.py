# # pages/charts.py

# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
# from PyQt5.QtCore import Qt

# from widgets.mpl_canvas import MplCanvas
# from app_state import AppState


# class ChartsPage(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.build_ui()

#     def build_ui(self):
#         layout = QVBoxLayout(self)

#         title = QLabel("Equipment Analytics (Live Data)")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size:22px; font-weight:800;")
#         layout.addWidget(title)

#         self.bar_canvas = MplCanvas()
#         self.pie_canvas = MplCanvas()

#         charts_row = QHBoxLayout()
#         charts_row.addWidget(self.bar_canvas)
#         charts_row.addWidget(self.pie_canvas)

#         layout.addLayout(charts_row)

#         # Initial placeholder
#         self.show_empty()

#     # 🔁 CALLED WHEN PAGE IS SHOWN
#     def on_show(self):
#         self.refresh()

#     def refresh(self):
#         dist = AppState.summary.get("type_distribution", {})

#         if not dist:
#             self.show_empty()
#             return

#         self.plot_bar(dist)
#         self.plot_pie(dist)

#     def show_empty(self):
#         for canvas in (self.bar_canvas, self.pie_canvas):
#             ax = canvas.axes
#             ax.clear()
#             ax.text(
#                 0.5, 0.5,
#                 "Upload CSV to view charts",
#                 ha="center",
#                 va="center",
#                 fontsize=12
#             )
#             ax.set_axis_off()
#             canvas.draw()

#     def plot_bar(self, dist):
#         ax = self.bar_canvas.axes
#         ax.clear()
#         ax.bar(dist.keys(), dist.values(), color="#2563eb")
#         ax.set_title("Equipment Distribution")
#         ax.grid(axis="y", linestyle="--", alpha=0.6)
#         self.bar_canvas.draw()

#     def plot_pie(self, dist):
#         ax = self.pie_canvas.axes
#         ax.clear()
#         ax.pie(
#             dist.values(),
#             labels=dist.keys(),
#             autopct="%1.1f%%",
#             startangle=90
#         )
#         ax.set_title("Equipment Share")
#         self.pie_canvas.draw()

# pages/charts.py

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QHBoxLayout, QFrame
)
from PyQt5.QtCore import Qt

from widgets.mpl_canvas import MplCanvas
from app_state import AppState


class ChartsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.build_ui()

    # =====================================================
    def build_ui(self):
        root = QVBoxLayout(self)
        root.setSpacing(24)
        root.setContentsMargins(36, 30, 36, 24)

        # ================= HEADER =================
        header = QVBoxLayout()
        header.setSpacing(6)

        title = QLabel("Equipment Analytics")
        title.setStyleSheet("""
            font-size:26px;
            font-weight:900;
            color:#0f172a;
        """)

        subtitle = QLabel("Live distribution insights from uploaded datasets")
        subtitle.setStyleSheet("""
            font-size:14px;
            color:#64748b;
        """)

        header.addWidget(title)
        header.addWidget(subtitle)
        root.addLayout(header)

        # ================= CHARTS ROW =================
        charts_row = QHBoxLayout()
        charts_row.setSpacing(20)

        self.bar_canvas = MplCanvas()
        self.pie_canvas = MplCanvas()

        bar_card = self.chart_card(
            "Equipment Distribution",
            self.bar_canvas
        )

        pie_card = self.chart_card(
            "Equipment Share",
            self.pie_canvas
        )

        charts_row.addWidget(bar_card)
        charts_row.addWidget(pie_card)

        root.addLayout(charts_row)
        root.addStretch()

        # Initial placeholder
        self.show_empty()

    # =====================================================
    def chart_card(self, title_text, canvas):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background:white;
                border-radius:16px;
                border:1px solid #e5e7eb;
            }
        """)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 18, 20, 20)
        layout.setSpacing(12)

        title = QLabel(title_text)
        title.setStyleSheet("""
            font-size:18px;
            font-weight:800;
            color:#0f172a;
        """)

        layout.addWidget(title)
        layout.addWidget(canvas)

        return card

    # 🔁 CALLED WHEN PAGE IS SHOWN
    def on_show(self):
        self.refresh()

    # =====================================================
    def refresh(self):
        dist = AppState.summary.get("type_distribution", {})

        if not dist:
            self.show_empty()
            return

        self.plot_bar(dist)
        self.plot_pie(dist)

    # =====================================================
    def show_empty(self):
        for canvas in (self.bar_canvas, self.pie_canvas):
            ax = canvas.axes
            ax.clear()
            ax.text(
                0.5, 0.5,
                "Upload CSV to view charts",
                ha="center",
                va="center",
                fontsize=12,
                color="#64748b"
            )
            ax.set_axis_off()
            canvas.draw()

    # =====================================================
    def plot_bar(self, dist):
        ax = self.bar_canvas.axes
        ax.clear()

        ax.bar(
            dist.keys(),
            dist.values(),
            color="#2563eb"
        )

        ax.grid(axis="y", linestyle="--", alpha=0.5)
        ax.set_ylabel("Count")
        ax.set_xlabel("Equipment Type")

        self.bar_canvas.draw()

    # =====================================================
    def plot_pie(self, dist):
        ax = self.pie_canvas.axes
        ax.clear()

        ax.pie(
            dist.values(),
            labels=dist.keys(),
            autopct="%1.1f%%",
            startangle=90
        )

        self.pie_canvas.draw()
