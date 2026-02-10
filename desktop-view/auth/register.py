# # auth/register.py

# from PyQt5.QtWidgets import (
#     QWidget,
#     QVBoxLayout,
#     QLabel,
#     QLineEdit,
#     QPushButton,
# )
# from PyQt5.QtCore import Qt


# class RegisterPage(QWidget):
#     def __init__(self, on_success):
#         super().__init__()
#         self.on_success = on_success
#         self.build_ui()

#     def build_ui(self):
#         layout = QVBoxLayout(self)
#         layout.setAlignment(Qt.AlignCenter)
#         layout.setSpacing(16)

#         title = QLabel("Create Account")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size:24px; font-weight:800;")

#         self.username = QLineEdit()
#         self.username.setPlaceholderText("Username")

#         self.email = QLineEdit()
#         self.email.setPlaceholderText("Email")

#         self.password = QLineEdit()
#         self.password.setPlaceholderText("Password")
#         self.password.setEchoMode(QLineEdit.Password)

#         btn = QPushButton("Register")
#         btn.setFixedHeight(42)
#         btn.clicked.connect(self.handle_register)

#         layout.addWidget(title)
#         layout.addWidget(self.username)
#         layout.addWidget(self.email)
#         layout.addWidget(self.password)
#         layout.addWidget(btn)

#     def handle_register(self):
#         self.on_success()

# auth/register.py

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame,
)
from PyQt5.QtCore import Qt


class RegisterPage(QWidget):
    def __init__(self, on_success):
        super().__init__()
        self.on_success = on_success
        self.build_ui()

    # =====================================================
    def build_ui(self):
        root = QVBoxLayout(self)
        root.setAlignment(Qt.AlignCenter)
        root.setContentsMargins(0, 0, 0, 0)

        # ================= CARD =================
        card = QFrame()
        card.setFixedWidth(440)
        card.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 18px;
                border: 1px solid #e5e7eb;
            }
        """)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(36, 32, 36, 30)
        layout.setSpacing(18)

        # ================= TITLE =================
        title = QLabel("Create Account")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:26px;
            font-weight:900;
            color:#0f172a;
        """)

        subtitle = QLabel("Initialize analytics workstation profile")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
            font-size:13px;
            color:#64748b;
        """)

        # ================= INPUTS (VISUAL ONLY) =================
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setFixedHeight(42)
        self.username.setStyleSheet(self.input_style())

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.email.setFixedHeight(42)
        self.email.setStyleSheet(self.input_style())

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedHeight(42)
        self.password.setStyleSheet(self.input_style())

        # ================= BUTTON =================
        btn = QPushButton("Create Account")
        btn.setFixedHeight(44)
        btn.setCursor(Qt.PointingHandCursor)
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
        btn.clicked.connect(self.handle_register)

        footer = QLabel("© ChemLab Analytics")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("""
            font-size:11px;
            color:#94a3b8;
        """)

        # ================= ADD =================
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(8)
        layout.addWidget(self.username)
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(btn)
        layout.addSpacing(6)
        layout.addWidget(footer)

        root.addWidget(card)

    # =====================================================
    def input_style(self):
        return """
            QLineEdit {
                border: 1px solid #e5e7eb;
                border-radius: 10px;
                padding: 0 14px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #2563eb;
                background: #f8fafc;
            }
        """

    # =====================================================
    # STRICT BYPASS REGISTER
    # =====================================================
    def handle_register(self):
        # NO STORAGE — DIRECT NAVIGATION
        self.on_success()
