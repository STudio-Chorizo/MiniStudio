import json
import os

ASSETS = {}

def parseJson(path = "/Assets/assets.json"):
    global ASSETS
    file = open(os.getcwd()+path, 'r')
    ASSETS = json.loads(file.read())

parseJson()