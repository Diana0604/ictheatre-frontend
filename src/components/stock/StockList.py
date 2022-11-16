# Qt components
from PyQt5.QtWidgets import QWidget, QGridLayout
# My components
from stock import SingleStock
# API interaction
from apiGetters import getCompaniesArray
import time

import time
import threading

stopUpdateThread = False


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
            layout.addWidget(company["singleStockWidget"],
                             companyPosX, companyPosY)
            # update pos for next company
            if companyPosY == 2:
                companyPosX = companyPosX + 1
                companyPosY = 0
            else:
                companyPosY = 2
        # display layout
        self.setLayout(layout)

        # init the updates
        # stopThread -> let's the thread know when the class is destroyed
        stopUpdateThread = False
        # start new thread that updates every second
        updateThread = threading.Thread(target=self.updatePrice, args=[])
        updateThread.start()

    def __del__(self):
        global stopUpdateThread
        print('deleting!!!!')
        stopUpdateThread = True

    def updatePrice(self):
        global stopUpdateThread
        while True:
            print(stopUpdateThread)
            time.sleep(0.2)
            if stopUpdateThread:
                return
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
