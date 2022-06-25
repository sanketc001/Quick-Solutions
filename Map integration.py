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
for j in range(20):
    pyautogui.locate('mark.png')
    pyautogui.scroll(100)
    time.sleep(1)
#pyautogui.mouseInfo()
for i in rows:
    print(i)
    pyautogui.click(355,111)
    pyautogui.write(i[0])
    pyautogui.click(781,110)
    time.sleep(1)
    pyautogui.click('cross.png')
    for j in range(20):
        pyautogui.locate('mark.png')
        pyautogui.scroll(100)
# import gmaps
# import gmaps.datasets
#
# gmaps.configure(api_key='AI...')