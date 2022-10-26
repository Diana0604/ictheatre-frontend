import sys
sys.path.append('./src/constants')
sys.path.append('./src/components/displays')
sys.path.append('./src/components/stock')
sys.path.append('./src/api')
from apiGetters import getCompaniesArray
from displays import TimeDisplay
from constants import mainConstants
from stock import SingleStock
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(mainConstants.WINDOWTITLE)

        layout = QGridLayout()

        #top middle we display time as it passes
        layout.addWidget(TimeDisplay(), 0, 1)

        #get companies list from API and display in two rows below
        companiesArray = getCompaniesArray()
        companyPosX = 1
        companyPosY = 0
        for company in companiesArray:
            layout.addWidget(SingleStock(company), companyPosX, companyPosY)
            if companyPosY == 2:
                companyPosX = companyPosX + 1
                companyPosY = 0
            else:
                companyPosY = 2

        #prepare and display main widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
