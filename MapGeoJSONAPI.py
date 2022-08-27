#import geojson
import json
from fastapi import FastAPI
import pickle
app = FastAPI()
# file=open("Beed-Khasara.geojson","r")
# l=[]
# for i in file:
#   try:
#     l.append(dict(json.loads(i[:-2])))
#   except:
#     pass
# d={}
# for i in l:
#   d.update({i['properties']['Khasra_No']:i})
# print(d)
# filename = "Khasaradict.pkl"
# geeky_file = open(filename, 'wb')
# pickle.dump(d, geeky_file)
# geeky_file.close()
@app.get("/{k}")
async def read_item(k):
    f = open("Khasaradict.pkl", "rb")
    return str(pickle.load(f)[k])