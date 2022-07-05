import time
import pyautogui
time.sleep(5)
while(True):
    pyautogui.scroll(-250)
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen("3.png"))
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("4.png",confidence=0.9))
    time.sleep(2)
    if(pyautogui.locateCenterOnScreen("6.png")!=None):
        pyautogui.click(pyautogui.locateCenterOnScreen("6.png"))
    else:
        pyautogui.click(pyautogui.locateCenterOnScreen("7.png"))
    time.sleep(2)
    pyautogui.click(672,461)
    time.sleep(2)
    pyautogui.click(471,14)
    time.sleep(2)
    pyautogui.click(pyautogui.locateCenterOnScreen("5.png",confidence=0.9))
    time.sleep(3)