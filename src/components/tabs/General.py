#Qt components
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout
#my components
from displays import CompanyInformationDisplay, PotentialClientsDisplay, PotentialSellersDisplay


class General(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()



        mainLayout = QGridLayout()

        leftLayout = QVBoxLayout()

        leftLayout.addWidget(CompanyInformationDisplay())
        leftLayout.addWidget(PotentialClientsDisplay())
        leftWidget = QWidget()
        leftWidget.setLayout(leftLayout)

        mainLayout.addWidget(leftWidget, 0, 0)
        mainLayout.addWidget(PotentialSellersDisplay(), 0, 1)

        # set layout
        self.setLayout(mainLayout)