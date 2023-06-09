import json
import os

ASSETS = {}
SCENES = {}
DIALOG = {}


def parseJson(path: str) -> bool | list | dict:
    """Parse le fichier json au chemin projet/`path` sous forme de liste ou de dictionnaire ou renvoie False si le fichier n'est pas trouver.\n
    Inclue la variable `ASSETS` et `SCENES` déjà parser pour récupérer les assets et scenes du projet"""
    global ASSETS
    global SCENES
    try:
        file = open(os.getcwd().replace("\\Assets", "")+path, 'r')
        return json.loads(file.read())
    except:
        return False

ASSETS = parseJson("/Assets/assets.json")

SCENES = parseJson("/Assets/scenes.json")

def loadDialog(Lang: str = "fr") -> dict:
    """Load le fichier langue avec comme parametre la langue, récupérable dans la variable DIALOG\n
    `fr`\n
    `en`"""
    global DIALOG
    DIALOG = parseJson("/Assets/dialog/" + Lang + ".json")
    return DIALOG

