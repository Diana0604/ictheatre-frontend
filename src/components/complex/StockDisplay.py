from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

class StockDisplay(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        layout.addWidget(QLabel('Company Name'))
        layout.addWidget(QLabel('$000.0'))
        layout.addWidget(QLabel('UP'))


        self.setLayout(layout)
