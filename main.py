from dependencies.Level.Level import Level
# Description: Main du projetdependencies/moderngl
def main():
    dino = Level()
    dino.LoadNiveau(2)

#################################################

# Import des dependances
from dependencies.parsejson.parse import *
import dependencies.moderngl.main as loadgl

# Check si le projet se lance avec succes
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succ�s
print("Ended with sucess")