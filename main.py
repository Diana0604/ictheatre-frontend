import PySimpleGUI as sg
import threading
import time
from score import scoreTab, scoreUpdate
from traders import openGuidelinesWindow, tradersTab, toggleTraderShares, tradersUpdate

sg.theme('Default1')

#Define Layout with Tabs
tabgrp = [[sg.TabGroup([[
    scoreTab,
    tradersTab,
]])]]


def init():
    global updatesThread
    #Create Window
    window = sg.Window("Tabs", tabgrp, finalize=True, resizable=True, size=(500, 500))

    #Method that will be called every second to update
    def updates():
        t = threading.currentThread()
        while getattr(t, "windowOpen", True):
            time.sleep(1.0)
            scoreUpdate(window)
            tradersUpdate(window)

    #Prepare updates thread
    updatesThread = threading.Thread(target=updates)
    updatesThread.start()
    return window


def run(window):
    while True:
        #Read  values entered by user
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if 'button-toggle-trader' in event:
            toggleTraderShares(window, event)
        if 'open-guidelines' in event:
            openGuidelinesWindow(window)


def end(window):
    global updatesThread
    #Finish updates before closing windows
    updatesThread.windowOpen = False
    updatesThread.join()

    #access all the values and if selected add them to a string
    window.close()