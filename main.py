import sys
sys.path.append('./src/constants')
sys.path.append('./src/components/displays')
sys.path.append('./src/components/complex')
sys.path.append('./src/api')
from apiGetters import getCompaniesArray
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
        companiesArray = getCompaniesArray()
        companyPosX = 1
        companyPosY = 0
        for company in companiesArray:
            layout.addWidget(StockDisplay(company), companyPosX, companyPosY)
            if companyPosY == 2:
                companyPosX = companyPosX + 1
                companyPosY = 0
            else:
                companyPosY = 2

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
