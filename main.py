def main():
    Engine.CreateInstance()
    Engine.Instance.LoadScene("test")

    Playlist.CreateInstance(Engine.Instance.MasterVolume)
    Playlist.Instance.miscs["game"].play()

    Engine.Instance.Start()

#################################################

# Import des dependances
from dependencies.parsejson.parse import *
import dependencies.moderngl.main as loadgl
from dependencies.engine.engine import *
from dependencies.engine.gameobject import *
from dependencies.scripts.entities.player import *
from dependencies.music.music_control import Playlist

# Check si le projet se lance avec succes
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succes
print("Ended with sucess")