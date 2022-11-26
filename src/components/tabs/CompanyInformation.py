#Qt components
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer
from apiGetters import getPlayerInfo
from labels import Title, RegularLabel


class CompanyInformation(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        companyInformation = getPlayerInfo()
        #name widget
        self.nameWidget = Title(f'{companyInformation["name"]}')
        print(companyInformation)
        self.liquidAssetsWidget = RegularLabel(
            f'Liquid Assets: {companyInformation["liquidAssets"]}')
        #stock value score
        self.stockValueScoreWidget = RegularLabel(
            f'Stock Value Score: {companyInformation["stockValueScore"]}')
        #PRI
        newPRI = float(companyInformation["publicRelationsIndex"]) * 100
        self.publicRelationsIndexWidget = RegularLabel(
            f'Public Relations Index: {newPRI}')

        verticalLayout = QVBoxLayout()

        verticalLayout.addWidget(self.nameWidget)
        verticalLayout.addWidget(self.liquidAssetsWidget)
        verticalLayout.addWidget(self.stockValueScoreWidget)
        verticalLayout.addWidget(self.publicRelationsIndexWidget)

        self.setMaximumHeight(200)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateInfo)
        self.timer.start(2000)

        self.setLayout(verticalLayout)

    def updateInfo(self):
        # get new player info
        companyInformation = getPlayerInfo()
        #update self.companyInformation
        self.nameWidget.setText(str(companyInformation['name']))
        self.liquidAssetsWidget.setText(
            f'Liquid Assets: {companyInformation["liquidAssets"]}')
        self.stockValueScoreWidget.setText(
            f'Stock Value Score: {companyInformation["stockValueScore"]}')
        newPRI = str(float(companyInformation['publicRelationsIndex']) * 100)
        self.publicRelationsIndexWidget.setText(
            f'Public Relations Index: {newPRI}')
