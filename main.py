from Engine.Engine import Engine
from Scripts.GUI.Menu import Menu
# Description: Main du projet
def main():
    engine = Engine(1000,580)
    menu = Menu(engine)
    engine.AddGameObject(menu)
    engine.Update()
    
    
    

#################################################

# Import des d�pendances
from dependencies.dependencies_controler import *

# Check si le projet se lance avec succ�s
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succ�s
print("Ended with sucess")