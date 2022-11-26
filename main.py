#constants
from constants import mainConstants
#Qt components
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QScrollArea
from PyQt5.QtCore import Qt
#my components
from tabs import Market, Sellers, CompanyInformation


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
        sellersInformation = Sellers()
        scrollArea = QScrollArea()
        scrollArea.setWidget(sellersInformation)
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #scrollArea.setWidgetResizable(True)
        tabs.addTab(scrollArea, "general information")
        #add score tab
        companyInformation = CompanyInformation()
        tabs.addTab(companyInformation, "score")

        # set tabs as central widget
        self.setCentralWidget(tabs)

        self.setMaximumWidth(500)
        self.setMaximumHeight(500)


def init():
    #start app
    app = QApplication([])

    #create main window
    window = MainWindow()
    window.show()

    #start exec loop
    app.exec()
