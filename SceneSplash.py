import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *


class SceneSplash(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        #TEXTS:
        self.WelcomeText = pygwidgets.DisplayText(self.window,
                                                  (50, 10),
                                                  "Welcome!",
                                                  fontSize=70,
                                                  textColor=YELLOW,
                                                  fontName="cmr10",
                                                  width=WINDOW_WIDTH-50-50,
                                                  justified="center")

        self.ChooseText = pygwidgets.DisplayText(self.window,
                                                  (50, 80 + SMALL_IMG + 20 + SMALL_IMG + 10),
                                                  "Choose a picture!",
                                                  fontSize=40,
                                                  textColor=YELLOW,
                                                  fontName="cmr10",
                                                  width=WINDOW_WIDTH-50-50,
                                                  justified="center")
        """
        self.CreatorText = pygwidgets.DisplayText(self.window,
                                                  (0, WINDOW_HEIGHT-14),
                                                  "by Github/MaksoPe v1.0",
                                                  fontSize=12,
                                                  textColor=WHITE,
                                                  fontName="cmr10",
                                                  width=WINDOW_WIDTH-2,
                                                  justified="right")
        """
        #BUTTONS:
        self.image1 = pygwidgets.CustomButton(self.window,
                                              (WINDOW_WIDTH/2 - SMALL_IMG - 10, 80),
                                              up="images/1up.jpg",
                                              over="images/1over.jpg")
        
        self.image2 = pygwidgets.CustomButton(self.window,
                                              (WINDOW_WIDTH/2 + 10, 80),
                                              up="images/2up.jpg",
                                              over="images/2over.jpg")
        
        self.image3 = pygwidgets.CustomButton(self.window,
                                              (WINDOW_WIDTH/2 - SMALL_IMG - 10,
                                               80 + SMALL_IMG + 10 +10),
                                              up="images/3up.jpg",
                                              over="images/3over.jpg")
        
        self.image4 = pygwidgets.CustomButton(self.window,
                                              (WINDOW_WIDTH/2 + 10,
                                               80 + SMALL_IMG + 10 +10),
                                              up="images/4up.jpg",
                                              over="images/4over.jpg")
        
        self.exitButton = pygwidgets.TextButton(self.window,
                                                (20, 660),
                                                "Exit")
                                                
        


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

                
    def update(self):
        pass

    def draw(self):
        self.window.fill(BACK_GRD)
        self.WelcomeText.draw()
        self.image1.draw()
        self.image2.draw()
        self.image3.draw()
        self.image4.draw()
        self.ChooseText.draw()
        #self.CreatorText.draw()

    def leave(self):
        return None
