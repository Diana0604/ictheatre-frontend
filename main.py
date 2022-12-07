import PySimpleGUI as sg
import threading
import time
from src.tabs.score import scoreTab, scoreUpdate
from src.tabs.traders import openGuidelinesWindow, tradersTab, toggleTraderShares, tradersUpdate
from src.tabs.market import companiesUpdate, marketTab

sg.theme('Default1')

#Define Layout with Tabs
tabgrp = [[
    sg.TabGroup([[scoreTab, tradersTab, marketTab]],
                enable_events=True,
                key='tab-group',
                background_color="#c0c0c0",)
]]


def init():
    global updatesThread
    #Create Window
    window = sg.Window("Tabs",
                       tabgrp,
                       finalize=True,
                       resizable=True,
                       size=(1000, 800))

    #Method that will be called every second to update
    def updates():
        t = threading.currentThread()

        while getattr(t, "windowOpen", True):
            #if getattr(t, "tabOpen", "score-tab"):
            scoreUpdate(window)
            #if(getattr(t, "tabOpen", "traders-tab")):
            tradersUpdate(window)
            #if(getattr(t, "tabOpen", "market-tab")):
            companiesUpdate(window)
            time.sleep(1.0)

    #Prepare updates thread
    updatesThread = threading.Thread(target=updates)
    updatesThread.start()
    return window


def run(window):
    while True:
        #Read  values entered by user
        event, values = window.read()
        #print(values)
        if event == sg.WIN_CLOSED:
            end(window)
            break
        if event == 1:
            continue
        event = str(event)
        if 'button-toggle-trader' in event:
            toggleTraderShares(window, event)
        if 'open-guidelines' in event:
            openGuidelinesWindow(window)


def end(window):
    global updatesThread
    #Finish updates before closing windows
    updatesThread.windowOpen = False
    #updatesThread.join()
    time.sleep(1)

    #access all the values and if selected add them to a string
    window.close()

window = init()
run(window)