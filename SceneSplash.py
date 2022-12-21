import pygwidgets
import pyghelpers
import pygame
import sys
from pygame.locals import *
from Constants import *


class SceneSplash(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        #TEXTS:
        self.ChooseText = pygwidgets.DisplayText(self.window,
                                                  (50, 10),
                                                  "Choose a picture!",
                                                  fontSize=40,
                                                  textColor=YELLOW,
                                                  fontName="cmr10",
                                                  width=WINDOW_WIDTH-50-50,
                                                  justified="center")


        #BUTTONS:
        self.image1 = pygwidgets.CustomButton(self.window,
                                              (WINDOW_WIDTH/2 - SMALL_IMG - 10, 50),
                                              up="images/1up.jpg",
                                              over="images/1over.jpg")
        
        self.image2 = pygwidgets.CustomButton(self.window,
                                              (WINDOW_WIDTH/2 + 10, 50),
                                              up="images/2up.jpg",
                                              over="images/2over.jpg")
        
        self.image3 = pygwidgets.CustomButton(self.window,
                                              (WINDOW_WIDTH/2 - SMALL_IMG - 10,
                                               50 + SMALL_IMG + 10 +10),
                                              up="images/3up.jpg",
                                              over="images/3over.jpg")
        
        self.image4 = pygwidgets.CustomButton(self.window,
                                              (WINDOW_WIDTH/2 + 10,
                                               50 + SMALL_IMG + 10 +10),
                                              up="images/4up.jpg",
                                              over="images/4over.jpg")
        
        self.ExitButton = pygwidgets.CustomButton(self.window,
                                                  (WINDOW_WIDTH/2 - 120, WINDOW_HEIGHT - 120 - 15),
                                                  up="images/button_exit_up.png",
                                                  over="images/button_exit_over.png",
                                                  disabled="images/button_exit_disable.png")
                                                
        
    def getSceneKey(self):
        return SCENE_SPLASH

    def enter(self, data):
        pass

    def handleInputs(self, eventList, keyPressedList):
        for event in eventList:
            if self.image1.handleEvent(event):
                self.goToScene(SCENE_PLAY, IMG_TUPLE[0])
            if self.image2.handleEvent(event):
                self.goToScene(SCENE_PLAY, IMG_TUPLE[1])
            if self.image3.handleEvent(event):
                self.goToScene(SCENE_PLAY, IMG_TUPLE[2])
            if self.image4.handleEvent(event):
                self.goToScene(SCENE_PLAY, IMG_TUPLE[3])
            if ((event.type == QUIT) or
                ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
                (self.ExitButton.handleEvent(event))):
                pygame.quit()
                sys.exit()

                
    def update(self):
        pass

    def draw(self):
        self.window.fill(BACK_GRD)
        #Button
        self.image1.draw()
        self.image2.draw()
        self.image3.draw()
        self.image4.draw()
        self.ExitButton.draw()
        #Text
        self.ChooseText.draw()

    def leave(self):
        return None
