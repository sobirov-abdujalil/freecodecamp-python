# Lab: Build a Player Interface
from abc import ABC, abstractmethod

class Playable(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class MusicPlayer(Playable):
    def __init__(self, track):
        self.track = track
        self.playing = False

    def play(self):
        self.playing = True
        return f"Playing {self.track}"

    def pause(self):
        self.playing = False
        return f"Paused {self.track}"

    def stop(self):
        self.playing = False
        return f"Stopped {self.track}"

mp = MusicPlayer("Song.mp3")
print(mp.play())
print(mp.pause())
