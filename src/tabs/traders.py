import PySimpleGUI as sg
from apiGetters import getSellersList, getCompaniesArray
from helpers.stringHelpers import numberToTwoDecimals

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

companies = getCompaniesArray()
sellersList = getSellersList()
sellers = sellersList["sellers"]
shareBundlesList = sellersList["shareBundles"]

shareBundles = {}
traders = {}
for seller in sellers:
    traders[seller['id']] = seller
    traders[seller['id']]['open'] = True
    shareBundles[seller['id']] = []
for shareBundle in shareBundlesList:
    shareBundles[shareBundle['ownerId']].append(
        f'{companies[shareBundle["companyId"]]["name"]}: {shareBundle["quantity"]} shares - currently valued at ${numberToTwoDecimals(companies[shareBundle["companyId"]]["currentPricePerShare"])}'
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
        sg.Text(traders[traderId]['name'], key=f'trader-{traderId}'),
        sg.T(SYMBOL_UP,
             enable_events=True,
             key=f'button-toggle-trader-{traderId}'),
    ]
    newSharesObject = [sg.Image(size=(0, 0))] + [
        sg.Listbox(
            values=shareBundles[traderId],  #TODO -> change this info
            key=f'shares-{traderId}',
            visible=True,
            size=(100, len(shareBundles[traderId])))
    ]

    tradersLayout.append(newTraderObject)
    tradersLayout.append(newSharesObject)

tradersTab = sg.Tab(
    'Traders Information',
    [[sg.Column(tradersLayout, scrollable=True, size=(1000, 1000))]],
    #tradersLayout,
    element_justification='left',
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
    global companies
    sellersShares = getSellersList()
    traders = sellersShares["sellers"]
    shareBundlesList = sellersShares["shareBundles"]
    shareBundles = {}
    for shareBundle in shareBundlesList:
        if not shareBundle['ownerId'] in shareBundles:
            shareBundles[shareBundle['ownerId']] = []
        shareBundles[shareBundle['ownerId']].append(
            f'{companies[shareBundle["companyId"]]["name"]}: {shareBundle["quantity"]} shares - currently valued at ${numberToTwoDecimals(companies[shareBundle["companyId"]]["currentPricePerShare"])}'
        )
    for trader in traders:
        #print(trader)
        traderId = trader["id"]
        window[f'shares-{traderId}'].update(values=shareBundles[traderId])
