import PySimpleGUI as sg
from apiGetters import getSellersList, getCompaniesArray
from helpers.stringHelpers import numberToTwoDecimals

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

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
                     sg.Text("Click here",
                             enable_events=True,
                             key="open-guidelines",
                             text_color="#3a02fe",
                             font=('', 10, ['underline'])),
                     sg.Text("for more information on how to do this.")
                 ]]

for traderId in traders:
    newTraderObject = [
        sg.Text(traders[traderId]['name'],
                key=f'trader-{traderId}',
                font=('Arial, 15')),
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
            font=("Arial", 13))
    ]

    tradersLayout.append(newTraderObject)
    tradersLayout.append(newSharesObject)

tradersTab = sg.Tab(
    'Traders Information',
    [[sg.Column(tradersLayout, scrollable=True, size=(1000, 1000))]],
    #tradersLayout,
    element_justification='left',
    key="traders-tab",
    #enable_events=True
)


def toggleTraderShares(window, event):
    id = int(str.replace(event, 'button-toggle-trader-', ''))
    sharesToToggle = f"shares-{id}"
    window[sharesToToggle].update(visible=not traders[id]["open"])
    window[event].update(SYMBOL_DOWN if traders[id]["open"] else SYMBOL_UP)
    traders[id]["open"] = not traders[id]["open"]


def openGuidelinesWindow(window):
    layout = [[sg.Text(
        "New Window",
        key="new",
    )]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
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
        print(shareBundle['quantity'])
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
        window[f'shares-{traderId}'].set_size((100, len(shareBundles[traderId])))
