#Qt components
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
#my components
from displays import TimeDisplay
from stock import StockList


class Market(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        pageLayout = QVBoxLayout()

        # top middle we display time as it passes
        pageLayout.addWidget(TimeDisplay(), alignment=Qt.AlignCenter)

        # display list of stock in market
        pageLayout.addWidget(StockList())

        # set layout
        self.setLayout(pageLayout)