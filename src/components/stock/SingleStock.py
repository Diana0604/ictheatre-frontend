from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from stringHelpers import removeAfterN


class SingleStock(QWidget):
    def __init__(self, companyName, companyPrice):
        super().__init__()

        layout = QHBoxLayout()
        # single stock displays:
        # COMPANY NAME | CURRENT STOCK PRICE - updated with time | UP / DOWN arrow - updated with time
        layout.addWidget(QLabel(companyName))
        companyPriceString = f'${companyPrice}'
        if '.' in companyPriceString:
            commaIndex = companyPriceString.index('.')
            companyPriceString = removeAfterN(
                companyPriceString, commaIndex + 3)

        layout.addWidget(QLabel(f'${companyPriceString}'))
        layout.addWidget(QLabel('UP'))

        self.setLayout(layout)
