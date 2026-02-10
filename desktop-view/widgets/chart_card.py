# widgets/chart_card.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtChart import (
    QChart, QChartView, QBarSeries,
    QBarSet, QBarCategoryAxis
)
from PyQt5.QtGui import QPainter


class ChartCard(QWidget):
    def __init__(self, title, data):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(title))

        series = QBarSeries()
        bar = QBarSet("Units")
        categories = []

        for key, value in data.items():
            bar << value
            categories.append(key)

        series.append(bar)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().hide()

        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.addAxis(axis, chart.AlignBottom)
        series.attachAxis(axis)

        view = QChartView(chart)
        view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(view)
