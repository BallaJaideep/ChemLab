# layout/protected.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget

from layout.navbar import Navbar
from pages.home import HomePage
from pages.upload import UploadPage
from pages.history import HistoryPage
from pages.dataset_view import DatasetViewPage
from pages.charts import ChartsPage


class ProtectedLayout(QWidget):
    def __init__(self, on_logout):
        super().__init__()
        self.on_logout = on_logout
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # -------- NAVBAR --------
        self.navbar = Navbar(self.navigate, self.on_logout)
        layout.addWidget(self.navbar)

        # -------- STACK --------
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # -------- PAGES --------
        self.pages = {
            "home": HomePage(self.navigate),
            "upload": UploadPage(),
            "history": HistoryPage(self.navigate),  # ✅ PASS CALLBACK
            "dataset_view": DatasetViewPage(self.navigate),
            "charts": ChartsPage(),
        }

        for page in self.pages.values():
            self.stack.addWidget(page)

        self.navigate("home")

    def navigate(self, page_name):
        page = self.pages.get(page_name)
        if not page:
            return

        self.stack.setCurrentWidget(page)

        if hasattr(page, "on_show"):
            page.on_show()
