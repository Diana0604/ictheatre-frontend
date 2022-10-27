# Qt components
from PyQt5.QtWidgets import QWidget, QGridLayout
# My components
from stock import SingleStock
# API interaction
from apiGetters import getCompaniesArray

import time
import threading

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
            company["singleStockWidget"] = SingleStock(
                company["name"], company["currentPricePerShare"])
            layout.addWidget(company["singleStockWidget"], companyPosX, companyPosY)
            # update pos for next company
            if companyPosY == 2:
                companyPosX = companyPosX + 1
                companyPosY = 0
            else:
                companyPosY = 2

        self.setLayout(layout)

        start_time = time.time()
        interval = 1
        def updateMethod(i):
            timeToSleep = start_time + i*interval - time.time()
            if(timeToSleep) > 0:
                time.sleep(timeToSleep)
            newCompaniesArray = getCompaniesArray()
            for i in range(len(companiesArray)):
                print('new price')
                print(newCompaniesArray[i]["currentPricePerShare"])
                companiesArray[i]["currentPricePerShare"] = newCompaniesArray[i]["currentPricePerShare"]
                companiesArray[i]["singleStockWidget"].updatePriceDisplay(companiesArray[i]["currentPricePerShare"])


        for i in range(100):
            newThread = threading.Thread(target=updateMethod, args=[i])
            newThread.start()
