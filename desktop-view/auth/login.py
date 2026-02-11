

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame,
)
from PyQt5.QtCore import Qt


class LoginPage(QWidget):
    def __init__(self, on_login_success, on_register):
        super().__init__()
        self.on_login_success = on_login_success
        self.on_register = on_register
        self.build_ui()

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setAlignment(Qt.AlignCenter)
        root.setContentsMargins(0, 0, 0, 0)

        card = QFrame()
        card.setFixedWidth(420)
        card.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 18px;
                border: 1px solid #e5e7eb;
            }
        """)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(36, 32, 36, 28)
        layout.setSpacing(18)

        title = QLabel("ChemLab Login")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:26px;
            font-weight:900;
            color:#0f172a;
        """)

        subtitle = QLabel("Chemical Equipment Analytics Portal")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
            font-size:13px;
            color:#64748b;
        """)

        
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setFixedHeight(42)
        self.username.setStyleSheet(self.input_style())

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedHeight(42)
        self.password.setStyleSheet(self.input_style())
        login_btn = QPushButton("Authorize Access")
        login_btn.setFixedHeight(44)
        login_btn.setCursor(Qt.PointingHandCursor)
        login_btn.setStyleSheet("""
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
        login_btn.clicked.connect(self.handle_login)

        register_btn = QPushButton("Create Account")
        register_btn.setCursor(Qt.PointingHandCursor)
        register_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                color:#2563eb;
                font-weight:700;
                font-size:13px;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """)
        register_btn.clicked.connect(self.on_register)

        footer = QLabel("© ChemLab Analytics")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("""
            font-size:11px;
            color:#94a3b8;
        """)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(10)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(login_btn)
        layout.addWidget(register_btn)
        layout.addSpacing(6)
        layout.addWidget(footer)

        root.addWidget(card)


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

    def handle_login(self):
        # NO CHECKS — DIRECT ENTRY
        self.on_login_success()
