from dependencies.object.guinfoperso import Guiplayer
# Description: Main du projetdependencies/moderngl
def main():
    #maps = Level()
    #maps.LoadNiveau(2)

    infoplayer = Guiplayer()
    infoplayer.LifePlayer()

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