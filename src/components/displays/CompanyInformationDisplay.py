#Qt components
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class CompanyInformationDisplay(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        verticalLayout = QVBoxLayout()

        verticalLayout.addWidget(QLabel("Stock Value: $00.00"))
        verticalLayout.addWidget(QLabel("Liquid Assets: $00.00"))
        verticalLayout.addWidget(QLabel("PR Index: 100%"))

        self.setLayout(verticalLayout)
