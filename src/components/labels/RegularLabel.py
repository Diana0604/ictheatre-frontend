from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


class RegularLabel(QLabel):

    def __init__(self, text):
        super(QLabel, self).__init__(text)
        self.setFont(QFont('Arial', 10))
