import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *
from PIL import Image

class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.SpriteImgDict = {}
        #START BUTTON
        #RESTART BUTTON?
        #TIMER
        #BACKGROUND MUSIC?
        #TILE SLIDE MUSIC?

    def getSceneKey(self):
        return SCENE_PLAY

    def enter(self, choosenImg):
        large_img = pygame.image.load(choosenImg)
        large_img = pygame.Surface.convert_alpha(large_img)

	#side = Square side length in pixels
	#N = how many puzzle pieces in each row/column
        large_img_width = large_img.get_width()
        side = large_img_width // N

        key = 1
        for y in range(N):
            for x in range(N):
                subsurfaceRect = pygame.Rect(x*side,
                                             y*side,
                                             side,
                                             side)
                
                tile_image = large_img.subsurface(subsurfaceRect)
		
                oTile = pygwidgets.Image(self.window,
                                         (20 + x * side, 20 + y * side),
                                         tile_image)
						       
                self.SpriteImgDict[key] = oTile
                key+=1
        
    def handleInputs(self, eventsList, keysPressedList):
        for event in eventsList:
            pass
        #HERE CHECK WHICH ONE IS CLICKED AND IF THE
        #EMPTY IS IN THE TOUCHING CROSS, THAN SWAP IT OUT

    def draw(self):
        self.window.fill(BACK_GRD)
        for key,value in self.SpriteImgDict.items():
            self.SpriteImgDict[key].draw()

    def leave(self):
        return None
        
