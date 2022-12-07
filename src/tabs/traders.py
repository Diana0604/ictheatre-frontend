import PySimpleGUI as sg
from src.api.apiGetters import getSellersList, getCompaniesArray
from src.helpers.stringHelpers import numberToTwoDecimals
from src.constants.symbols import SYMBOL_UP, SYMBOL_DOWN

sg.theme('Default1')
sg.set_options(font=("@MS Gothic", 11))

companies = getCompaniesArray()
sellersList = getSellersList()
tradersList = sellersList["sellers"]
shareBundlesList = sellersList["shareBundles"]

shareBundles = {}
traders = {}
for trader in tradersList:
    traders[trader['id']] = trader
    traders[trader['id']]['open'] = True
    shareBundles[trader['id']] = []
for shareBundle in shareBundlesList:
    ownerId = shareBundle["ownerId"]
    companyId = shareBundle["companyId"]
    companyName = companies[companyId]["name"]
    quantity = shareBundle["quantity"]
    shareBundles[ownerId].append(
        f'{companyName}: {quantity} shares - currently valued at ${numberToTwoDecimals(companies[shareBundle["companyId"]]["currentPricePerShare"])}'
    )

tradersLayout = [[
    sg.Text(
        "These are the traders that you can call to convince to buy and sell shares."
    ),
],
                 [
                     sg.Text(
                         "Click here",
                         enable_events=True,
                         key="open-guidelines",
                         text_color="#0c00ff",
                         font=('@MS Gothic', 11, ['underline']),
                     ),
                     sg.Text("for more information on how to do this.")
                 ]]

for traderId in traders:
    newTraderObject = [
        sg.Text(
            traders[traderId]['name'],
            key=f'trader-{traderId}',
        ),
        sg.T(SYMBOL_UP,
             enable_events=True,
             key=f'button-toggle-trader-{traderId}'),
    ]
    newSharesObject = [sg.Image(size=(0, 0))] + [
        sg.Listbox(
            values=shareBundles[traderId],  #TODO -> change this info
            key=f'shares-{traderId}',
            visible=True,
            size=(100, len(shareBundles[traderId])),
            )
    ]

    tradersLayout.append(newTraderObject)
    tradersLayout.append(newSharesObject)

tradersTab = sg.Tab(
    'Traders Information',
    [[sg.Column(tradersLayout, scrollable=True, size=(1000, 800))]],
    element_justification='left',
    key="traders-tab",
)


def toggleTraderShares(window, event):
    id = int(str.replace(event, 'button-toggle-trader-', ''))
    sharesToToggle = f"shares-{id}"
    window[sharesToToggle].update(visible=not traders[id]["open"])
    window[event].update(SYMBOL_DOWN if traders[id]["open"] else SYMBOL_UP)
    traders[id]["open"] = not traders[id]["open"]


def openGuidelinesWindow(window):
    layout = [
        [sg.Text("Call the number you have been given,")],
        [sg.Text("Ask for the person you wish to speak to,")],
        [sg.Text("Look at the information and keep that in mind.")],
        [sg.Text("Be kind and respectful, don' be a pushover")],
        [sg.Text("The more you get them to sell, the better your turnover.")],
        [sg.Text("Ask the right questions, but not too many,")],
        [sg.Text("or else you'll leave work without a penny.")],
    ]
    window = sg.Window("Guidelines", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


def tradersUpdate(window):
    sellersShares = getSellersList()
    companies = getCompaniesArray()
    traders = sellersShares["sellers"]
    shareBundlesList = sellersShares["shareBundles"]
    shareBundles = {}
    for shareBundle in shareBundlesList:
        if shareBundle['quantity'] == 0:
            continue
        if not shareBundle['ownerId'] in shareBundles:
            shareBundles[shareBundle['ownerId']] = []
        shareBundles[shareBundle['ownerId']].append(
            f'{companies[shareBundle["companyId"]]["name"]}: {shareBundle["quantity"]} shares - currently valued at ${numberToTwoDecimals(companies[shareBundle["companyId"]]["currentPricePerShare"])}'
        )
    for trader in traders:
        traderId = trader["id"]
        window[f'shares-{traderId}'].update(values=shareBundles[traderId])
        window[f'shares-{traderId}'].set_size(
            (100, len(shareBundles[traderId])))
