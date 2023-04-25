# Description: Main du projet
def main():
    engine = Engine(1920,1080)
    menu = Menu(engine)
    engine.AddGameObject(menu)
    engine.Update()
    
    
    

#################################################

# Import des dependances
from Engine.Engine import Engine
from Scripts.GUI.Menu import Menu
from dependencies.dependencies_controler import *

# Check si le projet se lance avec succes
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succes
print("Ended with sucess")