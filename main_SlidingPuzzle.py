import pygame
import pyghelpers
import sys
from Constants import *
from SceneSplash import *
from ScenePlay import *

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH_HEIGHT, WINDOW_WIDTH_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
# Instantiate all scenes and store them into a list
scenesList = [SceneSplash(window),
              ScenePlay(window)]

# Create the Scene Manager, passing in the scenes list, and FPS
oSceneMgr = pyghelpers.SceneMgr(scenesList, FPS)

# Tell the scene manager to start running
oSceneMgr.run()
