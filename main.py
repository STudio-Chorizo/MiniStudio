# Description: Main du projetdependencies/moderngl


def main():
    engine = Engine()
    cube = GameObject()
    cube.SetModel("Cube", ASSETS["name"]["object"], 2)
    engine.Start()

#################################################

# Import des dependances
from dependencies.parsejson.parse import *
import dependencies.moderngl.main as loadgl
from dependencies.Engine.Engine import *
from dependencies.Engine.GameObject import *

# Check si le projet se lance avec succes
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succ�s
print("Ended with sucess")