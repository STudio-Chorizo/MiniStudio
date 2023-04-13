def main():

    eng = Engine()
    Engine.CreateInstance()

    player = Player("eagle")
    Engine.Instance.AddGameObject(player)

    cat = GameObject("cat", pos=(-10, -7.5, -20), rot=(-90, 0, 0))
    Engine.Instance.AddGameObject(cat)
    cat = GameObject("cat", pos=(-10, -7.5, -40), rot=(-90, 0, 0))
    Engine.Instance.AddGameObject(cat)
    cat = GameObject("cat", pos=(-10, -7.5, -60), rot=(-90, 0, 0))
    Engine.Instance.AddGameObject(cat)
    cat = GameObject("cat", pos=(-10, -7.5, -80), rot=(-90, 0, 0))
    Engine.Instance.AddGameObject(cat)
    cat = GameObject("cat", pos=(-10, -7.5, -100), rot=(-90, 0, 0))
    Engine.Instance.AddGameObject(cat)

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