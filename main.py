def main():
    Engine.CreateInstance()
    Engine.Instance.LoadScene("test")

    Playlist.CreateInstance(Engine.Instance.MasterVolume)
    
    Engine.Instance.Start()

#################################################

# Import des dependances
from dependencies.parsejson.parse import *
import dependencies.moderngl.main as loadgl
from dependencies.engine.engine import *
from dependencies.engine.gameobject import *
from dependencies.music.music_control import Playlist
from dependencies.scripts.gui.menu import Menu

# Check si le projet se lance avec succes
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succes
print("Ended with sucess")

# # Description: Main du projet
# def main():
#     engine = Engine(1920,1080)
#     menu = Menu(engine)
#     engine.AddGameObject(menu)
#     engine.Update()

# #################################################

# # Import des dependances
# from Engine.Engine import Engine
# from Scripts.GUI.Menu import Menu
# from dependencies.dependencies_controler import *