from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from stringHelpers import numberToTwoDecimals, removeAfterN


class SingleStock(QWidget):
    def __init__(self, companyName, stockPrice):
        super().__init__()

        layout = QHBoxLayout()

        # single stock displays:
        # COMPANY NAME | CURRENT STOCK PRICE - updated with time | UP / DOWN arrow - updated with time
        layout.addWidget(QLabel(companyName))

        # get stock price with two decimals
        stockPrice = numberToTwoDecimals(stockPrice)
        self.priceDisplay = QLabel(f'${stockPrice}')
        layout.addWidget(self.priceDisplay)

        # add arrow
        layout.addWidget(QLabel('UP'))

        self.setLayout(layout)

    def updatePriceDisplay(self, stockPrice):
        stockPrice = numberToTwoDecimals(stockPrice)
        self.priceDisplay.setText(stockPrice)
