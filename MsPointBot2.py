import pyautogui
import os
import time
from msedge.selenium_tools import Edge

SearchOne = "50 cent"

WDL = input("Do You Want The Loop: ")

while True:
    os.system('start microsoft-edge://')
    pyautogui.typewrite(SearchOne)
    pyautogui.press('enter')
    time.sleep(60)
    os.system("taskkill /im chrome.exe /f")

    if WDL == "no":
        break
