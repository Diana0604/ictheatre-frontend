#constants
from constants import mainConstants
#Qt components
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from PyQt5.QtCore import Qt
#my components
from tabs import Market
from tabs import General


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # set window title
        self.setWindowTitle(mainConstants.WINDOWTITLE)

        # create tabs object
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        # add stock market tab
        market = Market()
        tabs.addTab(market, "market")
        # add general information tab
        generalInformation = General()
        tabs.addTab(generalInformation, "general information")

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
