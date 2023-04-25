import pygame as pg
import time
from dependencies.parsejson.parse import *

class Music:
    def __init__(self, path: str, autoPause: bool = True) -> None:
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
        
    def play(self, loop: int = -1, time: float = 0) -> None:
        if self.played == False:
            print("play: " + self.misc)
            self.channel.play(self.music, loop, int(time * 1000))
            self.played = True
    
    def stop(self) -> None:
        print("stop: " + self.misc)
        self.channel.stop()
        self.played = False
    
    def pause(self) -> None:
        if self.played == True:
            print("pause: " + self.misc)
            self.channel.pause()
            self.played = False
        else:
            print("unpause: " + self.misc)
            self.channel.unpause()
            self.played = True
    
    def restart(self, loop: int = -1, time: float = 0) -> None:
        print("restart: " + self.misc)
        self.channel.stop()
        self.channel.play(self.music, loop, int(time * 1000))
        self.played = True

    def set_volume(self, volume: float = 100) -> None:
        self.vol = volume
        self.next_vol = volume

    def smooth_volume(self, volume: float = 100) -> None:
        self.next_vol = volume
    
    def update(self) -> None:
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
        if(Playlist.Instance != None) : return
        Playlist.Instance = Playlist()
    
    def __init__(self) -> None:
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
        for misc in self.miscs:
            self.miscs[misc].update()