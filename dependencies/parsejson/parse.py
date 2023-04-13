import json
import os

ASSETS = {}

def parseJson(path: str) -> False | list | dict:
    """Parse le fichier json au chemin projet/`path` sous forme de liste ou de dictionnaire ou renvoie False si le fichier n'est pas trouver.\n
    Inclue la variable `ASSETS` déjà parser pour récupérer les assets du projet"""
    global ASSETS
    try:
        file = open(os.getcwd()+path, 'r')
        return json.loads(file.read())
    except:
        return False

ASSETS = parseJson("/Assets/assets.json")