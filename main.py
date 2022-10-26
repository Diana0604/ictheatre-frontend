from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from constants import mainConstants
import sys
sys.path.append('./src/constants')


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(mainConstants.WINDOWTITLE)

        layout = QGridLayout()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
