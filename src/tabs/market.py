import PySimpleGUI as sg
from src.api.apiGetters import getCompaniesArray
from src.constants.symbols import ARROW_UP_FILE, ARROW_DOWN_FILE

from src.helpers.stringHelpers import numberToTwoDecimals

sg.theme('Default1')
sg.set_options(font=("@MS Gothic", 11))

companies = getCompaniesArray()

marketLayout = []

columnLeft = []
columnRight = []

for companyId in companies:
    newCompanyObject = [
        sg.Text(
            f"{companies[companyId]['name']}: Shares Price At ${companies[companyId]['currentPricePerShare']}",
            key=f'market-company-{companies[companyId]["id"]}',
        ),
    ]
    columnLeft.append(newCompanyObject)
    newArrowObject = [
        sg.Image(ARROW_UP_FILE,
                 visible=False,
                 key=f'arrow-up-{companies[companyId]["id"]}'),
        sg.Image(ARROW_DOWN_FILE,
                 key=f'arrow-down-{companies[companyId]["id"]}'),
    ]
    columnRight.append(newArrowObject)

marketLayout.append([sg.Column(columnLeft), sg.Column(columnRight)])

marketTab = sg.Tab(
    'Market Information',
    marketLayout,
    element_justification='left',
    key="market-tab",
)

previousCompanies = getCompaniesArray()


def companiesUpdate(window):
    global previousCompanies
    companies = getCompaniesArray()
    for companyId in companies:
        window[f'market-company-{companies[companyId]["id"]}'].update(
            f"{companies[companyId]['name']}: Shares Price At ${numberToTwoDecimals(companies[companyId]['currentPricePerShare'])}"
        )
        if companies[companyId]["currentPricePerShare"] > previousCompanies[
                companyId]["currentPricePerShare"]:
            window[f'arrow-up-{companies[companyId]["id"]}'].update(
                visible=False)
            window[f'arrow-down-{companies[companyId]["id"]}'].update(
                visible=True)
        if companies[companyId]["currentPricePerShare"] < previousCompanies[
                companyId]["currentPricePerShare"]:
            window[f'arrow-up-{companies[companyId]["id"]}'].update(
                visible=True)
            window[f'arrow-down-{companies[companyId]["id"]}'].update(
                visible=False)

    previousCompanies = companies
