# Qt components
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtCore import QTimer
# My components
from stock import SingleStock
# API interaction
from apiGetters import getCompaniesArray

class StockList(QWidget):

    def __init__(self):
        global stopUpdateThread
        super().__init__()

        layout = QGridLayout()

        # get companies list from API
        self.companiesArray = getCompaniesArray()
        # iterate over companies list and display in two columns
        companyPosX = 0
        companyPosY = 0
        for company in self.companiesArray:
            company["singleStockWidget"] = SingleStock(
                company["name"], company["currentPricePerShare"])
            layout.addWidget(company["singleStockWidget"], companyPosX,
                             companyPosY)
            # update pos for next company
            if companyPosY == 2:
                companyPosX = companyPosX + 1
                companyPosY = 0
            else:
                companyPosY = 2
        # display layout
        self.setLayout(layout)

        # init the updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.updatePrice)
        self.timer.start(30000)

    def updatePrice(self):
        # get new list of companies
        newCompaniesArray = getCompaniesArray()
        # iterate over list of companies
        for i in range(len(self.companiesArray)):
            newStockPrice = newCompaniesArray[i]["currentPricePerShare"]
            # first -> update price in our list
            self.companiesArray[i]["currentPricePerShare"] = newStockPrice
            # second -> update price that is displayed
            self.companiesArray[i]["singleStockWidget"].updatePriceDisplay(
                newStockPrice)
