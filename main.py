def main():
    Playlist.CreateInstance()

    Engine.CreateInstance()
    Engine.Instance.LoadScene("test")
    GenerLevel()
    
    Engine.Instance.Start()
    
    while Engine.Instance.restart:
        Engine.Instance = None

        Engine.CreateInstance()
        Engine.Instance.LoadScene("test")
        GenerLevel()

        Engine.Instance.Start()

def GenerLevel():
    for i in ["aste", "debrisLeft"]:
        while len(Engine.Instance.pool[i].pool) != 0:
            obj = Engine.Instance.pool[i].Get()
            obj.position = glm.vec3([randint(-50, 50), randint(-50, 50), randint(100, 2000)])
            obj.rotation = glm.vec3([randint(0, 360), randint(0, 360), randint(0, 360)])


#################################################

# Import des dependances
from dependencies.engine.engine import *
from dependencies.music.music_control import Playlist
from random import *

# Check si le projet se lance avec succes
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succes

print("Ended with sucess")

