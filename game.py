import pygame
import sys
import time
from pygame.locals import *

stratagems = [ # Stratagem codes
    
    ## Eagle Stratagems
    {"codename": "ESR", "name": "Eagle Strafing Run", "code": ("↑","→","→"), "len": 3},
    {"codename": "EA", "name": "Eagle Airstrike", "code": ("↑","→","↓","→"), "len": 4},
    {"codename": "ECB", "name": "Eagle Cluster Bomb", "code": ("↑","→","↓","↓","→"), "len": 5},
    {"codename": "ESS", "name": "Eagle Smoke Strike", "code": ("↑","→","↑","↓"), "len": 4},
    {"codename": "ENA", "name": "Eagle Napalm Airstrike", "code": ("↑","→","↓","↑"), "len": 4},
    {"codename": "E110RP", "name": "Eagle 110mm Rocket Pods", "code": ("↑","→","↑","←"), "len": 4},
    {"codename": "E5B", "name": "Eagle 500kg Bomb", "code": ("↑","→","↓","↓","↓"), "len": 5},
]

display_bg = pygame.Color(255, 255, 255) # background colour for pygame display
class App:
    def __init__(self):
        self._running = True # sets var to true when game runs
        self._display_surf = None # def the var for display
        self.FPS = pygame.time.Clock() # def FPS by clock
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((700, 500), pygame.HWSURFACE | pygame.DOUBLEBUF) # creates pygame window (size)
        self._running = True # sets var to true when game runs again?
    def on_event(self, event):
        if event.type == pygame.QUIT: # if the game is exitted out of
            self._running = False # sets var to false
    def on_loop(self):
        pass
    def on_render(self):
        self._display_surf.fill((display_bg)) # sets displays colour
    def on_cleanup(self):
        pygame.quit() # cleanly quits the game when game is quitted
    def on_execute(self):
        if self.on_init() == False: # error handler???
            self._running = False 
        while(self._running): # constant loop when _running is true
            self.FPS.tick(60) # sets fps to 60

            for event in pygame.event.get(): # grabs the events (keyboard triggers etc)
                self.on_event(event) # checks if the game has 'quitted'?
                pygame.display.flip() # updates display
            self.on_loop()
            self.on_render()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()