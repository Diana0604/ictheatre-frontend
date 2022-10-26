# Qt components
from PyQt5.QtWidgets import QWidget, QGridLayout
# My components
from stock import SingleStock
# API interaction
from apiGetters import getCompaniesArray


class StockList(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        # get companies list from API
        companiesArray = getCompaniesArray()
        # iterate over companies list and display in two columns
        companyPosX = 0
        companyPosY = 0
        for company in companiesArray:
            layout.addWidget(SingleStock(
                company["name"], company["currentPricePerShare"]), companyPosX, companyPosY)
            # update pos for next company
            if companyPosY == 2:
                companyPosX = companyPosX + 1
                companyPosY = 0
            else:
                companyPosY = 2

        self.setLayout(layout)
