# widgets/stat_card.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class StatCard(QWidget):
    def __init__(self, label, value, unit=""):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        layout.addWidget(QLabel(label.upper()))
        layout.addWidget(QLabel(str(value)))

        if unit:
            layout.addWidget(QLabel(unit))
