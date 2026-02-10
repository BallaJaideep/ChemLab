# main.py
import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from db.database import init_db


def load_styles(app):
    try:
        with open("styles/theme.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    load_styles(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
