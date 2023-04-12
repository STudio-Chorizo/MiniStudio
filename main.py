from Engine import Engine
from Scripts.GUI import Menu
# Description: Main du projet
def main():
    Engine = Engine(800,800)
    Menu = Menu(engine)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()

#################################################

# Import des d�pendances
from dependencies.dependencies_controler import *

# Check si le projet se lance avec succ�s
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succ�s
print("Ended with sucess")