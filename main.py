def main():
    Playlist.CreateInstance()

    Engine.CreateInstance()
    Engine.Instance.LoadScene("test")
    
    Engine.Instance.Start()

#################################################

# Import des dependances
from dependencies.engine.engine import *
from dependencies.music.music_control import Playlist

# Check si le projet se lance avec succes
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succes

print("Ended with sucess")

