from dependencies.language.language import Luanguage
def main():
   Engine.CreateInstance()
   Engine.Instance.LoadScene("test")
   Engine.Instance.Start()
   Engine.Instance.Ln = 1
   print(DIALOG[Engine.Instance.Ln][0])

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