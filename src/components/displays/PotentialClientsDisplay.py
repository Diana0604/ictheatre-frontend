#Qt components
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class PotentialClientsDisplay(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        verticalLayout = QVBoxLayout()

        verticalLayout.addWidget(QLabel("Bill Gates - Microsoft"))
        verticalLayout.addWidget(QLabel("Steve Jobs - Apple"))
        verticalLayout.addWidget(QLabel("Elon Musk - X. Com / Paypal"))
        verticalLayout.addWidget(QLabel("Jeff Bezos - Amazon"))

        self.setLayout(verticalLayout)
