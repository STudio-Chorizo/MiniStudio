# Description: Main du projetdependencies/moderngl


def main():
    engine = Engine.CreateInstance()
    cube = GameObject()
    cube.SetModel("Cat", rot=(-90, 0, 0))
    Engine.Instance.Start()

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

# Check si le projet se termine avec succes
print("Ended with sucess")