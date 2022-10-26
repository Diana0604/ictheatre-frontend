import sys
sys.path.append('./src/constants')
sys.path.append('./src/components/displays')
sys.path.append('./src/components/complex')
from displays import TimeDisplay
from constants import mainConstants
from complex import StockDisplay
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(mainConstants.WINDOWTITLE)

        layout = QGridLayout()

        layout.addWidget(TimeDisplay(), 0, 1)
        layout.addWidget(StockDisplay(), 1,0)
        layout.addWidget(StockDisplay(), 1,2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
