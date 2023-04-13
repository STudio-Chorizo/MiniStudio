import json
import os

ASSETS = {}

def parseJson(path):
    global ASSETS
    file = open(os.getcwd()+path, 'r')
    return json.loads(file.read())

ASSETS = parseJson("/Assets/assets.json")