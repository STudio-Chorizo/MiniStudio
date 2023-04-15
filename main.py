def main():
    Engine.CreateInstance()
    
    Engine.Instance.LoadScene("test")

    for o in Engine.Instance.gameObjects:
        Engine.Instance.gameObjects[o].SetCollider((5, 6, 5))



    Engine.Instance.Start()

#################################################

# Import des dependances
from dependencies.parsejson.parse import *
import dependencies.moderngl.main as loadgl
from dependencies.engine.engine import *
from dependencies.engine.gameobject import *
from dependencies.scripts.entities.player import *

# Check si le projet se lance avec succes
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succes
print("Ended with sucess")