#Qt components
import threading
import time
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from apiGetters import getPlayerInfo

stopUpdateThread = False


class CompanyInformation(QWidget):

    def __init__(self):
        global stopUpdateThread
        super(QWidget, self).__init__()

        self.companyInformation = getPlayerInfo()

        self.companyInformation['publicRelationsIndex'] = float(self.companyInformation['publicRelationsIndex'])*100

        verticalLayout = QVBoxLayout()

        verticalLayout.addWidget(QLabel(f"{self.companyInformation['name']}"))
        verticalLayout.addWidget(QLabel(f"Liquid Assets: ${self.companyInformation['liquidAssets']}"))
        verticalLayout.addWidget(QLabel(f"Stock Value:{self.companyInformation['stockValueScore']}"))
        verticalLayout.addWidget(QLabel(f"PR Index: {self.companyInformation['publicRelationsIndex']}%"))

        self.setLayout(verticalLayout)

        
        # init the updates
        # stopThread -> let's the thread know when the class is destroyed
        stopUpdateThread = False
        # start new thread that updates every second
        updateThread = threading.Thread(target=self.updateInfo, args=[])
        updateThread.start()

        
    def __del__(self):
        global stopUpdateThread
        print('deleting!!!!')
        stopUpdateThread = True

    def updateInfo(self):
        global stopUpdateThread
        while True:
            #print(stopUpdateThread)
            time.sleep(2)
            if stopUpdateThread:
                return

            # get new player info
            newCompanyInformation = getPlayerInfo()
            newCompanyInformation['publicRelationsIndex'] = float(newCompanyInformation['publicRelationsIndex'])*100
            #update self.companyInformation
            self.companyInformation = newCompanyInformation
            

            