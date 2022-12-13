import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *
from PIL import Image

class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.SpriteImgList = {}
        #START BUTTON
        #RESTART BUTTON?
        #TIMER
        #BACKGROUND MUSIC?
        #TILE SLIDE MUSIC?

    def getSceneKey(self):
        return SCENE_PLAY

    def enter(self, choosenImg):
        #Process the choosen Img (slice it up)
        large_img = Image.open(choosenImg)
        width, height = large_img.size
        w_pixel, h_pixel = width // N, height // N
        #num will be the key, the PIL.Image object is the value
        num = 1
        for y in range(N):
            for x in range(N):
                sprite_img = large_img.crop((x * w_pixel,
                                             y * h_pixel,
                                             (x+1) * w_pixel,
                                             (y+1) * h_pixel))
                
                self.SpriteImgList[num] = sprite_img
                num+=1
        #Change one object to a simple black fill, in the dict
        #TOP - RIGHT SQUARE BLACK?!
    
    def handleInputs(self, eventsList, keysPressedList):
        for event in eventsList:
            pass
        #HERE CHECK WHICH ONE IS CLICKED AND IF THE
        #EMPTY IS IN THE TOUCHING CROSS, THAN SWAP IT OUT

    def draw(self):
        #REDRAW THE TILES
        #DRAW THE BUTTONS, TIMER, ETC..
        pass

    def leave(self):
        return None
        
