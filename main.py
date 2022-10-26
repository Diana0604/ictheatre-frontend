#constants
from constants import mainConstants
#Qt components
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
#my components
from displays import TimeDisplay
from stock import StockList


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(mainConstants.WINDOWTITLE)

        pageLayout = QVBoxLayout()

        # top middle we display time as it passes
        pageLayout.addWidget(TimeDisplay(), alignment=Qt.AlignCenter)

        # display list of stock in market
        pageLayout.addWidget(StockList())

        # prepare and display main widget
        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)

def init():
    #start app
    app = QApplication([])

    #create main window
    window = MainWindow()
    window.show()

    #start exec loop
    app.exec()
