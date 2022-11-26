# Qt components
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtCore import QTimer
# My components
from sellers import SingleSeller
# API interaction
from apiGetters import getSellersList


class Sellers(QWidget):

    def __init__(self):
        global stopUpdateThread
        super().__init__()

        layout = QGridLayout()

        # get sellers list from API
        sellerBundles = getSellersList()
        self.sellersList = sellerBundles['sellers']
        self.bundlesList = sellerBundles['shareBundles']
        # iterate over sellers list and display in two columns
        companyPosX = 0
        companyPosY = 0
        for seller in self.sellersList:
            print(seller)
            seller["sellerWidget"] = SingleSeller(seller, self.bundlesList)
            layout.addWidget(seller["sellerWidget"])
            # update pos for next company
            if companyPosY == 2:
                companyPosX = companyPosX + 1
                companyPosY = 0
            else:
                companyPosY = 2
        # display layout
        self.setLayout(layout)