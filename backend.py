import random
import json
import os

def loadfile(path):
  with open(path,"r",encoding="utf-8") as file:
    data = json.load(file)
  file.close()
  return data

def savefile(path,value):
  with open(path,"w",encoding="utf-8") as file:
    json.dump(value,file)
  file.close()

settings=loadfile(os.path.dirname(os.path.abspath(__file__))+"/settings.json")
items = loadfile(os.path.dirname(os.path.abspath(__file__))+"/list.json")

def getrandomelement():
  return random.choice(items)
