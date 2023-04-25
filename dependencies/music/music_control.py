import pygame as pg
import time
from dependencies.parsejson.parse import *

class Music:
    def __init__(self, path: str, autoPause: bool = True) -> None:
        """Création de la musique (se fait automatiquement avec la playlist)\n
        ======\n
        path: chemin vers le fichier audio\n
        autoPause: si la musique doit se mettre en pause quand le volume est au minimum"""
        self.path = path
        self.misc = self.path.split("/")[-1]
        self.path.replace("/", "\\")

        self.music = pg.mixer.Sound(self.path)
        self.channel = pg.mixer.find_channel(True)

        self.vol = 100
        self.next_vol = 100

        self.played = False
        self.autoPause = [autoPause, False]
        self.lastUpdate = time.time()

        self.set_volume(self.vol)
        self.update()
        
    def play(self, loop: int = 0, time: float = 0) -> None:
        """Joue la musique\n
        ======\n
        loop: nombre de fois que la musique doit se répéter (-1 = infini)\n
        time: timing de départ de la musique"""
        if self.played == False:
            print("play: " + self.misc)
            self.channel.play(self.music, loop, int(time * 1000))
            self.played = True
    
    def stop(self) -> None:
        """Arrête la musique"""
        print("stop: " + self.misc)
        self.channel.stop()
        self.played = False
    
    def pause(self) -> None:
        """Met en pause la musique\n
        Si la musique est déjà en pause, la remet en lecture\n
        ======\n
        La musique se mettreras également en pause quand le volume est au minimum si autoPause est à True\n
        S'il est en pause à cause du volume, il se remettra en lecture quand le volume sera supérieur à 0\n
        Vous pourrez néanmoins le mettre en pause ou remmettre la lecture manuellement avec pause() même si le volume est au minimum"""
        if self.played:
            print("pause: " + self.misc)
            self.channel.pause()
            self.played = False
        else:
            print("unpause: " + self.misc)
            self.channel.unpause()
            self.played = True
    
    def restart(self, loop: int = 0, time: float = 0) -> None:
        """Redémarre la musique quel soit déjà lancé ou non (équivalent d'un forcePlay())\n
        ======\n
        loop: nombre de fois que la musique doit se répéter (-1 = infini)\n
        time: timing de départ de la musique"""
        print("restart: " + self.misc)
        self.channel.stop()
        self.channel.play(self.music, loop, int(time * 1000))
        self.played = True

    def set_volume(self, volume: float = 100) -> None:
        """Change le volume de la musique d'un coup"""
        self.vol = volume
        self.next_vol = volume

    def smooth_volume(self, volume: float = 100) -> None:
        """Change le volume de la musique progressivement"""
        self.next_vol = volume
    
    def update(self) -> None:
        """Update la musique"""
        updateTime = time.time() - self.lastUpdate
        self.lastUpdate = time.time()
        if self.vol != self.next_vol:
            if self.vol > self.next_vol:
                self.vol -= updateTime * 20
            else:
                self.vol += updateTime * 20
        if abs(self.vol - self.next_vol) < 1:
            self.vol = self.next_vol
        self.channel.set_volume(self.vol / 100)

        if self.vol == 0 and self.autoPause[0]:
            if self.autoPause[1] == False:
                print("pause: " + self.misc)
                self.channel.pause()
                self.autoPause[1] = True
        elif self.vol != 0 and self.autoPause[0]:
            if self.autoPause[1] == True:
                print("unpause: " + self.misc)
                self.channel.unpause()
                self.autoPause[1] = False

class Playlist:
    Instance = None
    @staticmethod
    def CreateInstance():
        """Initialisation de l'instance de la playlist"""
        if(Playlist.Instance != None) : return
        Playlist.Instance = Playlist()
    
    def __init__(self) -> None:
        """INTERDICTION D'APPELLER CETTE FONCTION !!!\n
        Utiliser CreateInstance() a la place\n
        ======\n
        Initialisation de la playlist"""
        pg.mixer.init()
        pg.mixer.set_num_channels(len(ASSETS["playlist"]))
        self.miscs = {}
        for path in ASSETS["playlist"]:
            self.miscs[path] = Music(ASSETS["playlist"][path])
            self.miscs[path].play(0)
            self.miscs[path].pause()
        
        for misc in self.miscs:
            self.miscs[misc].stop()
    
    def update(self) -> None:
        """Update toute les musiques"""
        for misc in self.miscs:
            self.miscs[misc].update()