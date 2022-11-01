#Qt components
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class PotentialSellersDisplay(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        verticalLayout = QVBoxLayout()

        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))
        verticalLayout.addWidget(QLabel("Charlotte Mead"))

        self.setLayout(verticalLayout)
