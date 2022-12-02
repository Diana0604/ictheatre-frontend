import PySimpleGUI as sg
from apiGetters import getPlayerInfo

scoreLayout = [[
    sg.Text('Liquid Assets: loading', key="liquidAssets", size=(500, 1))
], [
    sg.Text('Stock Value Score: loading', key="stockValueScore", size=(500, 1))
],
               [
                   sg.Text('Public Relations Index: loading',
                           key="publicRelationsIndex",
                           size=(500, 1)),
               ]]

scoreTab = sg.Tab(
    'Company Information',
    scoreLayout,
    element_justification='left',
    key="score-tab",
    #enable_events=True
)

count = 0


def scoreUpdate(window):
    global count
    count = count + 1
    if not window.is_closed():
        playerJson = getPlayerInfo()
        newText = f'Stock Value Score: ${playerJson["stockValueScore"]}'
        window['stockValueScore'].update(newText)
        newText = f'Public Relations Index: {playerJson["publicRelationsIndex"]*100}%'
        window['publicRelationsIndex'].update(newText)
        newText = f'Liquid Assets: ${playerJson["liquidAssets"]}'
        window['liquidAssets'].update(newText)
