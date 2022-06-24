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

'''
time.sleep(5)
pyautogui.mouseInfo()
for i in rows:
    print(i)
# import gmaps
# import gmaps.datasets
#
# gmaps.configure(api_key='AI...')