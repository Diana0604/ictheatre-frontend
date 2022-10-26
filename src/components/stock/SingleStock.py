from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from apiGetters import getStockPrice

class SingleStock(QWidget):
    def __init__(self, companyName):
        super().__init__()

        layout = QHBoxLayout()

        layout.addWidget(QLabel(companyName))
        layout.addWidget(QLabel(getStockPrice(companyName)))
        layout.addWidget(QLabel('UP'))


        self.setLayout(layout)
