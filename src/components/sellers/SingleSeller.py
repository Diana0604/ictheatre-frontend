from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from labels import Title, RegularLabel
#from stringHelpers import numberToTwoDecimals, removeAfterN


class SingleSeller(QWidget):

    def __init__(self, seller, bundlesList):
        super().__init__()

        layout = QVBoxLayout()

        self.titleWidget = QWidget()
        titleWidgetLayout = QHBoxLayout()
        titleWidgetLayout.addWidget(Title(seller['name']))
        self.hideButton = QPushButton("click")
        self.hideButton.clicked.connect(self.toggleSharesView)
        self.hideButton.setFixedWidth(50)
        titleWidgetLayout.addWidget(self.hideButton)
        self.titleWidget.setLayout(titleWidgetLayout)

        layout.addWidget(self.titleWidget)

        self.sharesWidget = QWidget()
        sharesLayout = QVBoxLayout()
        self.id = seller['id']
        #print(seller['id'])
        self.bundlesWidgets = []
        for bundle in bundlesList:
            #print(bundle)
            if (bundle['ownerId'] == self.id):
                newLabel = RegularLabel(
                    f"has {bundle['quantity']} shares in company {bundle['companyName']}"
                )
                self.bundlesWidgets.append(newLabel)
                sharesLayout.addWidget(newLabel)
        self.sharesWidget.setLayout(sharesLayout)
        layout.addWidget(self.sharesWidget)
        self.setLayout(layout)

    def toggleSharesView(self):
        if (self.sharesWidget.isHidden()):
            self.sharesWidget.show()
        else:
            self.sharesWidget.hide()