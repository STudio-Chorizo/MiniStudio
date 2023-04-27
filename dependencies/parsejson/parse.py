import json
import os

ASSETS = {}
SCENES = {}

def parseJson(path: str) -> bool | list | dict:
    """Parse le fichier json au chemin projet/`path` sous forme de liste ou de dictionnaire ou renvoie False si le fichier n'est pas trouver.\n
    Inclue la variable `ASSETS` et `SCENES` déjà parser pour récupérer les assets et scenes du projet"""
    global ASSETS
    try:
        file = open(os.getcwd().replace("\\Assets", "")+path, 'r')
        return json.loads(file.read())
    except:
        return False

ASSETS = parseJson("/Assets/assets.json")
SCENES = parseJson("/Assets/scenes.json")