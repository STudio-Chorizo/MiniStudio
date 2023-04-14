def main():

    eng = Engine()
    Engine.CreateInstance()

    player = Player("eagle")
    Engine.Instance.AddGameObject(player)

    cat = []
    for i in range(0, 20):
        cat.append(GameObject("cat", pos=(-10, -7.5, -20 * i), rot=(-90 + i, 0, 0)))
        Engine.Instance.AddGameObject(cat[i])

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