import json
import os

ASSETS = {}

def parseJson(path):
    global ASSETS
    try:
        file = open(os.getcwd()+path, 'r')
        return json.loads(file.read())
    except:
        return False

ASSETS = parseJson("/Assets/assets.json")