from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QColor


class StockDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('green'))
        self.setPalette(palette)
