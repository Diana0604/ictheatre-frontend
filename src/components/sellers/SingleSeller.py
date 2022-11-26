from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
#from stringHelpers import numberToTwoDecimals, removeAfterN


class SingleSeller(QWidget):

    def __init__(self, seller, bundlesList):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel(seller['name']))
        self.id = seller['id']
        #print(seller['id'])
        self.bundlesWidgets = []
        for bundle in bundlesList:
            #print(bundle)
            if (bundle['ownerId'] == self.id):
                newLabel = QLabel(
                    f"has {bundle['quantity']} shares in company {bundle['companyName']}"
                )
                self.bundlesWidgets.append(newLabel)
                layout.addWidget(newLabel)

        self.setLayout(layout)