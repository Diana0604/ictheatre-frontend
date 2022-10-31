#constants
from constants import mainConstants
#Qt components
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget
from PyQt5.QtCore import Qt
#my components
from tabs import Market


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # set window title
        self.setWindowTitle(mainConstants.WINDOWTITLE)

        # create tabs object
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        # add stock market
        market = Market()
        tabs.addTab(market, "market")

        # set tabs as central widget
        self.setCentralWidget(tabs)

def init():
    #start app
    app = QApplication([])

    #create main window
    window = MainWindow()
    window.show()

    #start exec loop
    app.exec()
