#Qt components
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from labels import Title


class PotentialClientsDisplay(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        verticalLayout = QVBoxLayout()

        verticalLayout.addWidget(Title("Bill Gates - Microsoft"))
        verticalLayout.addWidget(Title("Steve Jobs - Apple"))
        verticalLayout.addWidget(Title("Elon Musk - X. Com / Paypal"))
        verticalLayout.addWidget(Title("Jeff Bezos - Amazon"))

        self.setLayout(verticalLayout)
