import geojson
import json
import pandas as pd
import csv
file=open("/content/Beed-Khasara.geojson","r")
l=[]
for i in file:
  try:
    l.append(dict(json.loads(i[:-2])))
  except:
    pass
print(l[0])
filename = "/content/Beed-Khasara.txt"
with open(filename, 'w') as csvfile:
  for i in l:
    csvfile.writelines(str(i)+"\n")