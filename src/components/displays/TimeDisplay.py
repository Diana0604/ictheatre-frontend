from PyQt5.QtWidgets import QLabel

#display current time
class TimeDisplay(QLabel):
    def __init__(self):
        super().__init__("00:00")
