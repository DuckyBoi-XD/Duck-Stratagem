import pygame
import random
import sys
import time
from pygame.locals import *

## Eagle Stratagems
ESR = {"name": "Eagle Strafing Run", "code": ("↑","→","→"), "length": 3}
EA = {"name": "Eagle Airstrike", "code": ("↑","→","↓","→"), "length": 4}
ECB = { "name": "Eagle Cluster Bomb", "code": ("↑","→","↓","↓","→"), "length": 5}
ESS = {"name": "Eagle Smoke Strike", "code": ("↑","→","↑","↓"), "length": 4}
ENA = {"name": "Eagle Napalm Airstrike", "code": ("↑","→","↓","↑"), "length": 4}
E110RP = {"name": "Eagle 110mm Rocket Pods", "code": ("↑","→","↑","←"), "length": 4}
ESB = {"name": "Eagle 500kg Bomb", "code": ("↑","→","↓","↓","↓"), "length": 5}

## Orbital Strikes 
OPS = {"name": "Orbital Precision Strike", "code": ("→","→","↑"), "length": 3}
OGB = {"name": "Orbital Gatling Barrage", "code": ("→","↓","←","↑","↑" ), "length": 5}
OGS = {"name": "Orbital Gas Strike", "code": ("↑","→","↓","↓","↓"), "length": 5}
O120HEB = {"name": "Orbital 120mm HE Barrage", "code": ("→","→","↓","←","→","↓"), "length": 6}
OAS = {"name": "Orbital Airburst Strike", "code": ("→","→","→"), "length": 3}
OSS = {"name": "Orbital Smoke Strike", "code": ("→","→","↓","↑"), "length": 4}
OEMSS = {"name": "Orbital EMS Strike", "code": ("→","→","←","↓",), "length": 4}
O380HEB = {"name": "Orbital 380mm HE Barrage", "code": ("→","↓","↑","↑","←","↓","↓"), "length": 7}
OWB = {"name": "Orbital Walking Barrage", "code": ("→","↓","→","↓","→","↓"), "length": 6}
OL = {"name": "Orbital Laser", "code": ("→","↓","↑","→","↓"), "length": 5}
ONB = {"name": "Orbital Napalm Barrage", "code": ("→","→","↓","←","→","↑"), "length": 6}
ORS = {"name": "Orbital Railcannon Strike", "code": ("→","↑","↓","↓","→"), "length": 5}

stratagems = (ESR, EA, ECB, ESS, ENA, E110RP, ESB, OPS, OGB, OGS, O120HEB, OAS, OSS, OEMSS, O380HEB, OWB, OL, ONB, ORS) # Stratagem codes

stratagems_range = 0
for i in stratagems:
    stratagems_range += 1

display_bg = pygame.Color(0, 0, 0) # background colour for pygame display
class App:
    def __init__(self):
        self._running = True # sets var to true when game runs
        self._display_surf = None # def the var for display
        self.FPS = pygame.time.Clock() # def FPS by clock
        self.stratagem_list_name = [] # list of stratagems for the user to complete
        self.mode = None # how hard/many stratagems
        self.mode_options = ("Trivial", "Hard", "Super Helldive") # the different difficulties
        self.mode_amount = 5 # temp mode ammount
        self.name_stratagem_text = []
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((700, 500), pygame.HWSURFACE | pygame.DOUBLEBUF) # creates pygame window (size)
        font = pygame.font.Font('font.ttf', 36)
        SAC = 0 # stratagem_amount_count
        while True: # creates a list of stratagems for the user to complete
            if SAC < self.mode_amount:
                self.stratagem_list_name.append(random.choice(stratagems)["name"])
                SAC += 1
            else:
                print(self.stratagem_list_name)
                break
        for i in self.stratagem_list:
            self.name_stratagem_text += i["name"]

        self.text_surface = font.render(self.name_stratagem_text, True, (255, 255, 255)) # defines text to be displayed
        pygame.display.set_caption("Duck Stratagem") # Display window name
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

            self._display_surf.blit(self.text_surface, (100, 100)) # displays text

            for event in pygame.event.get(): # grabs the events (keyboard triggers etc)
                self.on_event(event) # checks if the game has 'quitted'?
                pygame.display.flip() # updates display
            self.on_loop()
            self.on_render()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()