import pyautogui
import csv
import time
rows = []
with open("Maharashtra.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
'''
355,111
781,110
675,405
410,142
'''
time.sleep(5)
print(pyautogui.KEY_NAMES)
for i in rows:
    print(i)
    pyautogui.click(355,111)
    pyautogui.write(i[0])
    pyautogui.click(781,110)
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('cross.png',confidence=0.9))
    for j in range(10):
        pyautogui.moveTo(pyautogui.locateCenterOnScreen("mark.png",confidence=0.7))
        pyautogui.scroll(100)
        time.sleep(1)
    temp=pyautogui.locateCenterOnScreen("mark.png",confidence=0.7)
    print(pyautogui.locateCenterOnScreen("mark.png",confidence=0.7))
    pyautogui.click(457,147)
    pyautogui.click(temp)
    time.sleep(1)
    pyautogui.write(i[0])
    time.sleep(1)
    pyautogui.hotkey('tab')
    for j in i[1:]:
        pyautogui.write(j)
    pyautogui.hotkey("enter")



pyautogui.mouseInfo()
# import gmaps
# import gmaps.datasets
#
# gmaps.configure(api_key='AI...')