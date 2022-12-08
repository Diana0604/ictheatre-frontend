import PySimpleGUI as sg
from math import floor
from src.api.apiGetters import getPlayerInfo, getShowStatus
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

frameLeft = sg.Frame(title="Rune's Data", layout=layoutLeft, size=(600, 600))

#build right display

BAR_WIDTH = 75  # width of each bar
BAR_SPACING = 30  # space between each bar
#BAR_SPACING = 75  # space between each bar
EDGE_OFFSET = 3  # offset from the left edge for first bar
#EDGE_OFFSET = 20  # offset from the left edge for first bar
GRAPH_SIZE = (600, 600)  # size in pixels

layoutRight = [[sg.Graph(GRAPH_SIZE, (0, 0), GRAPH_SIZE, k='-GRAPH-')]]
frameRight = sg.Column(layout=layoutRight, element_justification="centre")
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
# LIQUID ASSETS GRAPH ========================
currentLiquidAssets = playerJson["liquidAssets"]
goal = 2e9  #could come from database
#goalPR = 100
percentage = 500 / goal
#percentagePR = 500 / goalPR
colorPercentage = 2 / goal
# STOCK VALUE GRAPH ========================
currentStockValueScore = playerJson["stockValueScore"]
stockValueGoal = 250  #could come from database
stockValuePercentage = 500 / stockValueGoal
stockValueColorPercentage = 2 / stockValueGoal
# PR GRAPH ========================
currentPublicRelationsIndex = playerJson["publicRelationsIndex"]
publicRelationsIndexGoal = 100  #could come from database
publicRelationsIndexPercentage = 500 / publicRelationsIndexGoal
publicRelationsIndexColorPercentage = 2 / publicRelationsIndexGoal

# first update
firstUpdate = True

beginningOfNight = datetime(year=1999,
                            month=12,
                            day=31,
                            hour=11,
                            minute=00,
                            second=00)


def secondsToTimer(seconds):
    global beginningOfNight
    if (seconds < 3600):
        return f"{((beginningOfNight + timedelta(seconds=seconds)).strftime('%X %x'))} PM"
    else:
        if beginningOfNight.year == 1999:
            beginningOfNight = beginningOfNight + timedelta(days=1)
        return f"{((beginningOfNight + timedelta(seconds=seconds)).strftime('%X %x'))} AM"


def scoreUpdate(window):
    global EDGE_OFFSET, BAR_WIDTH, BAR_SPACING, firstUpdate
    global currentLiquidAssets, goal, percentage, colorPercentage
    global currentPublicRelationsIndex, publicRelationsIndexGoal, publicRelationsIndexPercentage, publicRelationsIndexColorPercentage
    global currentStockValueScore, stockValueGoal, stockValuePercentage, stockValueColorPercentage
    if not window.is_closed():
        showStatus = getShowStatus()
        window['score-timer'].update(
            secondsToTimer(showStatus['timeSinceStartup']))
        playerJson = getPlayerInfo()
        playerJson[
            "publicRelationsIndex"] = playerJson["publicRelationsIndex"] * 100
        liquidAssets = playerJson['liquidAssets']
        if liquidAssets > 1e9:
            newText = f'Liquid Assets: ${numberToTwoDecimals(liquidAssets/1e9)} billion'
            window['liquidAssets'].update(newText)
        elif liquidAssets > 1e6:
            newText = f'Liquid Assets: ${numberToTwoDecimals(liquidAssets/1e6)} million'
            window['liquidAssets'].update(newText)
        else:
            newText = f'Liquid Assets: ${numberToTwoDecimals(playerJson["liquidAssets"])}'
            window['liquidAssets'].update(newText)
        newText = f'Stock Value Score: ${numberToTwoDecimals(playerJson["stockValueScore"])}'
        window['stockValueScore'].update(newText)
        newText = f'Public Relations Index: {numberToTwoDecimals(playerJson["publicRelationsIndex"])}%'
        window['publicRelationsIndex'].update(newText)
        # GRAPH UPDATE
        if firstUpdate:
            # PR INDEX
            window['-GRAPH-'].draw_text(
                text=f' - - 100%',
                location=(
                    EDGE_OFFSET + 2 * (BAR_WIDTH + BAR_SPACING) + BAR_SPACING +
                    BAR_WIDTH / 2,
                    publicRelationsIndexGoal * publicRelationsIndexPercentage +
                    10),
                font=("@MS Gothic", 10))
            window['-GRAPH-'].draw_text(
                text=f' PR Index',
                location=(EDGE_OFFSET + 2 * (BAR_WIDTH + BAR_SPACING) +
                          BAR_SPACING + BAR_WIDTH / 2, 5),
                font=("@MS Gothic", 10))
            #STOCK VALUE
            window['-GRAPH-'].draw_text(
                text=f' - - $250',
                location=(EDGE_OFFSET + BAR_WIDTH + BAR_SPACING + BAR_SPACING +
                          BAR_WIDTH / 2,
                          stockValueGoal * stockValuePercentage + 10),
                font=("@MS Gothic", 10))
            window['-GRAPH-'].draw_text(
                text=f'Stock Value Price',
                location=(EDGE_OFFSET + BAR_WIDTH + BAR_SPACING + BAR_SPACING +
                          BAR_WIDTH / 2, 5),
                font=("@MS Gothic", 10))
            # LIQUID ASSETS
            window['-GRAPH-'].draw_text(text=f'- - $12 billion',
                                        location=(EDGE_OFFSET + BAR_WIDTH / 2,
                                                  goal * percentage + 10),
                                        font=("@MS Gothic", 10))
            window['-GRAPH-'].draw_text(text=f'Liquid Assets',
                                        location=(EDGE_OFFSET + BAR_WIDTH / 2,
                                                  5),
                                        font=("@MS Gothic", 10))
            currentLiquidAssets = playerJson["liquidAssets"]

        if playerJson[
                "publicRelationsIndex"] != currentPublicRelationsIndex or firstUpdate:
            #firstUpdate = False
            red = 255
            green = 255
            if (playerJson["publicRelationsIndex"] <
                    publicRelationsIndexGoal / 2):
                green = floor(publicRelationsIndexColorPercentage * green *
                              playerJson["publicRelationsIndex"])
            else:
                red = floor(red * publicRelationsIndexColorPercentage *
                            (publicRelationsIndexGoal -
                             playerJson["publicRelationsIndex"]))
                if red < 0:
                    red = 0
            hexRed = f'{red:x}'
            if len(hexRed) == 1:
                hexRed = f'0{hexRed}'
            hexGreen = f'{green:x}'
            if len(hexGreen) == 1:
                hexGreen = f'0{hexGreen}'
            newColor = f'#{hexRed}{hexGreen}00'
            #window['-GRAPH-'].erase()
            window['-GRAPH-'].draw_rectangle(
                top_left=(EDGE_OFFSET + 2 * (BAR_WIDTH + BAR_SPACING) +
                          BAR_SPACING, playerJson["publicRelationsIndex"] *
                          publicRelationsIndexPercentage + 10),
                bottom_right=(EDGE_OFFSET + 3 * (BAR_WIDTH + BAR_SPACING), 20),
                fill_color=newColor)
            currentPublicRelationsIndex = playerJson["publicRelationsIndex"]
        if playerJson[
                "stockValueScore"] != currentStockValueScore or firstUpdate:
            #firstUpdate = False
            red = 255
            green = 255
            if (playerJson["stockValueScore"] < stockValueGoal / 2):
                green = floor(stockValueColorPercentage * green *
                              playerJson["stockValueScore"])
            else:
                red = floor(red * stockValueColorPercentage *
                            (stockValueGoal - playerJson["stockValueScore"]))
                if red < 0:
                    red = 0
            hexRed = f'{red:x}'
            if len(hexRed) == 1:
                hexRed = f'0{hexRed}'
            hexGreen = f'{green:x}'
            if len(hexGreen) == 1:
                hexGreen = f'0{hexGreen}'
            newColor = f'#{hexRed}{hexGreen}00'
            #window['-GRAPH-'].erase()
            window['-GRAPH-'].draw_rectangle(
                top_left=(
                    EDGE_OFFSET + BAR_WIDTH + BAR_SPACING + BAR_SPACING,
                    playerJson["stockValueScore"] * stockValuePercentage + 10),
                bottom_right=(EDGE_OFFSET + 2 * (BAR_WIDTH + BAR_SPACING), 20),
                fill_color=newColor)
            currentStockValueScore = playerJson["stockValueScore"]
        if playerJson["liquidAssets"] != currentLiquidAssets or firstUpdate:
            firstUpdate = False
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
            #window['-GRAPH-'].erase()
            top_right_y = playerJson["liquidAssets"] * percentage + 10
            if(top_right_y < 20) : 
                top_right_y = 50 
            window['-GRAPH-'].draw_rectangle(
                top_left=(EDGE_OFFSET,
                          top_right_y),
                bottom_right=(EDGE_OFFSET + BAR_WIDTH + BAR_SPACING, 20),
                fill_color=newColor)
