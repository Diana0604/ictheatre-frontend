from PyQt5.QtWidgets import QWidget, QHBoxLayout
from stringHelpers import numberToTwoDecimals, removeAfterN
from labels import RegularLabel


class SingleStock(QWidget):
    def __init__(self, companyName, stockPrice):
        super().__init__()

        layout = QHBoxLayout()

        # single stock displays:
        # COMPANY NAME | CURRENT STOCK PRICE - updated with time | UP / DOWN arrow - updated with time
        layout.addWidget(RegularLabel(companyName))

        # get stock price with two decimals
        stockPrice = numberToTwoDecimals(stockPrice)
        self.priceDisplay = RegularLabel(f'${stockPrice}')
        layout.addWidget(self.priceDisplay)

        # add arrow
        layout.addWidget(RegularLabel('UP'))

        self.setLayout(layout)

    def updatePriceDisplay(self, stockPrice):
        stockPrice = numberToTwoDecimals(stockPrice)
        self.priceDisplay.setText(stockPrice)
