import pygame
import pyghelpers
import pygwidgets
from pygame.locals import *


class SceneSplash():
    def __init__(self, window):
        self.window = window

        self.WelcomeText = pygwidgets.DisplayText(self.window,
                                              (50, 50),
                                              "Choose a picture!",
                                              justified="center")
        #Loading in the pictures
        self.picturePath = "/home/kali/Desktop/Py/Sliding_puzzle/images/"
        self.pictureList = []
        for picture in self.picturePath:
            print(picture)


oScene = SceneSplash(2)
