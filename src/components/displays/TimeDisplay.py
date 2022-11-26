from labels import RegularLabel

#display current time
class TimeDisplay(RegularLabel):
    def __init__(self):
        super().__init__("00:00")
