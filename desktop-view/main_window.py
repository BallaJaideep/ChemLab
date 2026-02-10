# main_window.py

from PyQt5.QtWidgets import QMainWindow, QStackedWidget

from auth.login import LoginPage
from auth.register import RegisterPage
from layout.protected import ProtectedLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ChemLab Analytics")
        self.setMinimumSize(1200, 800)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # ✅ PASS BOTH CALLBACKS (THIS WAS MISSING BEFORE)
        self.login_page = LoginPage(
            self.on_login_success,
            self.show_register
        )

        self.register_page = RegisterPage(self.show_login)
        self.protected_layout = ProtectedLayout(self.show_login)

        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.register_page)
        self.stack.addWidget(self.protected_layout)

        self.show_login()

    def show_login(self):
        self.stack.setCurrentWidget(self.login_page)

    def show_register(self):
        self.stack.setCurrentWidget(self.register_page)

    def on_login_success(self):
        self.stack.setCurrentWidget(self.protected_layout)
