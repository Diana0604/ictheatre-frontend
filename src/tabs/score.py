import PySimpleGUI as sg
from math import floor
from main import sg
from apiGetters import getPlayerInfo, getShowStatus
from src.helpers.stringHelpers import numberToTwoDecimals
from datetime import datetime, timedelta

sg.theme('Default1')
sg.set_options(font=("@MS Gothic", 11))

#build left display

layoutLeft = [
    [
        sg.Text(
            'Liquid Assets: loading',
            key="liquidAssets",
            font=("@MS Gothic", 20),
        )
    ],
    [
        sg.Text('Stock Value Score: loading',
                key="stockValueScore",
                font=("@MS Gothic", 20))
    ],
    [
        sg.Text('Public Relations Index: loading',
                key="publicRelationsIndex",
                font=("@MS Gothic", 20))
    ],
]

frameLeft = sg.Frame(title="Rune's Data", layout=layoutLeft, size=(600,600))

#build right display

BAR_WIDTH = 50  # width of each bar
BAR_SPACING = 0  # space between each bar
#BAR_SPACING = 75  # space between each bar
EDGE_OFFSET = 0  # offset from the left edge for first bar
#EDGE_OFFSET = 20  # offset from the left edge for first bar
GRAPH_SIZE = (500, 500)  # size in pixels

layoutRight = [[sg.Graph(GRAPH_SIZE, (0, 0), GRAPH_SIZE, k='-GRAPH-')]]
frameRight = sg.Column( layout=layoutRight, element_justification="centre")
#cloumnRight = [[
#    sg.Frame(title="Company's Income", layout=frameRight, size=(600, 600))
#]]

#get two columns
scoreLayout = [[
    sg.Text('00:00',
            key='score-timer',
            font=("@MS Gothic", 20),
            justification="center",
            size=(500, 2))
], [frameLeft, frameRight]]

scoreTab = sg.Tab(
    'Company Information',
    scoreLayout,
    element_justification='left',
    key="score-tab",
)

count = 0

playerJson = getPlayerInfo()
currentLiquidAssets = playerJson["liquidAssets"]
goal = 500000  #could come from database
percentage = 500 / goal
colorPercentage = 2 / goal
firstUpdate = True

beginningOfNight = datetime(year=1999,
                            month=12,
                            day=31,
                            hour=11,
                            minute=00,
                            second=00)


def secondsToTimer(seconds):
    global beginningOfNight
    if(seconds < 3600):
        return f"{((beginningOfNight + timedelta(seconds=seconds)).strftime('%X %x'))} PM"
    else :
        if beginningOfNight.year == 1999 :
            beginningOfNight = beginningOfNight + timedelta(days=1)
        return f"{((beginningOfNight + timedelta(seconds=seconds)).strftime('%X %x'))} AM"


def scoreUpdate(window):
    global EDGE_OFFSET, BAR_WIDTH, currentLiquidAssets, percentage, firstUpdate, goal
    if not window.is_closed():
        showStatus = getShowStatus()
        window['score-timer'].update(
            secondsToTimer(showStatus['timeSinceStartup']))
        playerJson = getPlayerInfo()
        newText = f'Stock Value Score: ${numberToTwoDecimals(playerJson["stockValueScore"])}'
        window['stockValueScore'].update(newText)
        newText = f'Public Relations Index: {numberToTwoDecimals(playerJson["publicRelationsIndex"]*100)}%'
        window['publicRelationsIndex'].update(newText)
        newText = f'Liquid Assets: ${numberToTwoDecimals(playerJson["liquidAssets"])}'
        window['liquidAssets'].update(newText)
        if playerJson["liquidAssets"] != currentLiquidAssets or firstUpdate:
            firstUpdate = True
            red = 255
            green = 255
            if (playerJson["liquidAssets"] < goal / 2):
                green = floor(colorPercentage * green *
                              playerJson["liquidAssets"])
            else:
                red = floor(red * colorPercentage *
                            (goal - playerJson["liquidAssets"]))
                if red < 0:
                    red = 0
            hexRed = f'{red:x}'
            if len(hexRed) == 1:
                hexRed = f'0{hexRed}'
            hexGreen = f'{green:x}'
            if len(hexGreen) == 1:
                hexGreen = f'0{hexGreen}'
            newColor = f'#{hexRed}{hexGreen}00'
            window['-GRAPH-'].erase()
            window['-GRAPH-'].draw_rectangle(
                top_left=(EDGE_OFFSET,
                          playerJson["liquidAssets"] * percentage),
                bottom_right=(EDGE_OFFSET + BAR_WIDTH, 0),
                fill_color=newColor)
            window['-GRAPH-'].draw_text(text=f' -- ${goal}',
                                        location=(BAR_SPACING + EDGE_OFFSET +
                                                  25, goal * percentage + 10),
                                        font=("@MS Gothic", 15))
            currentLiquidAssets = playerJson["liquidAssets"]
