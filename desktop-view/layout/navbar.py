# # layout/navbar.py

# from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


# class Navbar(QWidget):
#     def __init__(self, on_nav_click, on_logout):
#         super().__init__()

#         self.on_nav_click = on_nav_click
#         self.on_logout = on_logout

#         self.build_ui()

#     def build_ui(self):
#         layout = QHBoxLayout(self)
#         layout.setContentsMargins(12, 8, 12, 8)
#         layout.setSpacing(12)

#         # ---------- NAV BUTTONS ----------
#         btn_home = QPushButton("Home")
#         btn_upload = QPushButton("Upload")
#         btn_history = QPushButton("History")
#         btn_charts = QPushButton("Charts")
#         btn_logout = QPushButton("Logout")

#         # ---------- STYLING ----------
#         for btn in [btn_home, btn_upload, btn_history, btn_charts]:
#             btn.setFixedHeight(32)

#         btn_logout.setFixedHeight(32)
#         btn_logout.setStyleSheet(
#             "background:#fee2e2; color:#991b1b; font-weight:600;"
#         )

#         # ---------- CONNECTIONS ----------
#         btn_home.clicked.connect(lambda: self.on_nav_click("home"))
#         btn_upload.clicked.connect(lambda: self.on_nav_click("upload"))
#         btn_history.clicked.connect(lambda: self.on_nav_click("history"))
#         btn_charts.clicked.connect(lambda: self.on_nav_click("charts"))
#         btn_logout.clicked.connect(self.on_logout)

#         # ---------- LAYOUT ----------
#         layout.addWidget(btn_home)
#         layout.addWidget(btn_upload)
#         layout.addWidget(btn_history)
#         layout.addWidget(btn_charts)
#         layout.addStretch()
#         layout.addWidget(btn_logout)

# layout/navbar.py

from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
)
from PyQt5.QtCore import Qt


class Navbar(QWidget):
    def __init__(self, on_nav_click, on_logout):
        super().__init__()
        self.on_nav_click = on_nav_click
        self.on_logout = on_logout
        self.build_ui()

    # =====================================================
    def build_ui(self):
        self.setFixedHeight(56)
        self.setStyleSheet("""
            QWidget {
                background: #ffffff;
                border-bottom: 1px solid #e5e7eb;
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 8, 20, 8)
        layout.setSpacing(10)

        # ================= BRAND =================
        brand = QLabel("⬢ ChemLab")
        brand.setStyleSheet("""
            font-size:18px;
            font-weight:900;
            color:#0f172a;
        """)

        # ================= NAV BUTTONS =================
        btn_home = self.nav_btn("Home", lambda: self.on_nav_click("home"))
        btn_upload = self.nav_btn("Upload", lambda: self.on_nav_click("upload"))
        btn_history = self.nav_btn("History", lambda: self.on_nav_click("history"))
        btn_charts = self.nav_btn("Charts", lambda: self.on_nav_click("charts"))

        # ================= LOGOUT =================
        logout_btn = QPushButton("Logout")
        logout_btn.setFixedHeight(34)
        logout_btn.setCursor(Qt.PointingHandCursor)
        logout_btn.setStyleSheet("""
            QPushButton {
                background:#fef2f2;
                color:#991b1b;
                font-weight:700;
                border-radius:8px;
                padding: 0 16px;
                border: 1px solid #fecaca;
            }
            QPushButton:hover {
                background:#fee2e2;
            }
        """)
        logout_btn.clicked.connect(self.on_logout)

        # ================= LAYOUT =================
        layout.addWidget(brand)
        layout.addSpacing(20)
        layout.addWidget(btn_home)
        layout.addWidget(btn_upload)
        layout.addWidget(btn_history)
        layout.addWidget(btn_charts)
        layout.addStretch()
        layout.addWidget(logout_btn)

    # =====================================================
    def nav_btn(self, text, callback):
        btn = QPushButton(text)
        btn.setFixedHeight(34)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                font-size:14px;
                font-weight:700;
                color:#475569;
                padding: 0 14px;
                border-radius:8px;
            }
            QPushButton:hover {
                background:#f1f5f9;
                color:#0f172a;
            }
        """)
        btn.clicked.connect(callback)
        return btn
