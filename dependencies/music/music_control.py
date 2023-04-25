# from dependencies.parsejson.parse import *
import pygame as pg

class Music:
    def __init__(self, path: str = "dependencies\\music\\BATIMS.mp3") -> None:
        self.path = path
        self.music = pg.mixer.Sound(self.path)
        
    def play(self) -> None:
        self.music.play()

pg.init()
pg.mixer.init()
bendy = Music("dependencies\\music\\BATIMS.mp3")
dwarf = Music("dependencies\\music\\DDH.mp3")

while True: 
    event = pg.event.wait()
    dwarf.play()
    if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]: 
        break

pg.quit() 