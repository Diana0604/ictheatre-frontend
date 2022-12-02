import PySimpleGUI as sg
from apiGetters import getCompaniesArray

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

companies = getCompaniesArray()

marketLayout = []

for companyId in companies:
    newCompanyObject = [
        sg.Text(
            f"{companies[companyId]['name']}: Shares Price At ${companies[companyId]['currentPricePerShare']}",
            key=f'market-company-{companies[companyId]["id"]}',
            font=('Arial', 15)),
    ]
    marketLayout.append(newCompanyObject)

marketTab = sg.Tab('Market Information',
                   marketLayout,
                   element_justification='left',
                   key="market-tab",
                   #enable_events=True
                   )


def companiesUpdate(window):
    companies = getCompaniesArray()
    for companyId in companies:
        window[f'market-company-{companies[companyId]["id"]}'].update(
            f"{companies[companyId]['name']}: Shares Price At ${companies[companyId]['currentPricePerShare']}"
        )
