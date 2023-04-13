# Description: Main du projetdependencies/moderngl
def main():
    app = loadgl.GraphicsEngine()
    timing = time.time()
    while True:
        app.get_time()
        app.check_events()
        app.camera.update()
        app.render()
        app.delta_time = app.clock.tick(60)
        print("FPS: " + str(int(60 / (time.time() - timing))))
        timing = time.time()

#################################################

# Import des dependances
from dependencies.parsejson.parse import *
import dependencies.moderngl.main as loadgl
import time

# Check si le projet se lance avec succes
print("Start with sucess")

# Lance le projet
main()

# Check si le projet se termine avec succes
print("Ended with sucess")