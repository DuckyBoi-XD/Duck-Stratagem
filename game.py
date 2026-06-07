import pygame
import random
import sys
import time
from pygame.locals import *

## Eagle Stratagems
ESR = {"name": "Eagle Strafing Run", "code": "122", "length": 3}
EA = {"name": "Eagle Airstrike", "code": "1232", "length": 4}
ECB = { "name": "Eagle Cluster Bomb", "code": "12332", "length": 5}
ESS = {"name": "Eagle Smoke Strike", "code": "1213", "length": 4}
ENA = {"name": "Eagle Napalm Airstrike", "code": "1231", "length": 4}
E110RP = {"name": "Eagle 110mm Rocket Pods", "code": "1214", "length": 4}
ESB = {"name": "Eagle 500kg Bomb", "code": "12333", "length": 5}

## Orbital Strikes
OPS = {"name": "Orbital Precision Strike", "code": "221", "length": 3}
OGB = {"name": "Orbital Gatling Barrage", "code": "23411", "length": 5}
OGS = {"name": "Orbital Gas Strike", "code": "12333", "length": 5}
O120HEB = {"name": "Orbital 120mm HE Barrage", "code": "223423", "length": 6}
OAS = {"name": "Orbital Airburst Strike", "code": "222", "length": 3}
OSS = {"name": "Orbital Smoke Strike", "code": "2231", "length": 4}
OEMSS = {"name": "Orbital EMS Strike", "code": "2243", "length": 4}
O380HEB = {"name": "Orbital 380mm HE Barrage", "code": "2311433", "length": 7}
OWB = {"name": "Orbital Walking Barrage", "code": "232323", "length": 6}
OL = {"name": "Orbital Laser", "code": "23123", "length": 5}
ONB = {"name": "Orbital Napalm Barrage", "code": "223421", "length": 6}
ORS = {"name": "Orbital Railcannon Strike", "code": "21332", "length": 5}

display_bg = pygame.Color(0, 0, 0) # background colour for pygame display
class App:
    def __init__(self):
        self._running = True # sets var to true when game runs
        self._display_surf = None # def the var for display
        self.FPS = pygame.time.Clock() # def FPS by clock
        self.stratagem_list_code_image = [] # list of stratagems code for the user to complete
        self.mode = None # how hard/many stratagems
        self.mode_options = ("Trivial", "Hard", "Super Helldive") # the different difficulties
        self.mode_amount = 5 # temp mode ammount
        self.name_stratagem_text = ""
        self.stratagem_text = ""

    def on_init(self):
        pygame.init()
        self.stratagems = (ESR, EA, ECB, ESS, ENA, E110RP, ESB, OPS, OGB, OGS, O120HEB, OAS, OSS, OEMSS, O380HEB, OWB, OL, ONB, ORS) # Stratagem codes
        self.display = pygame.display.set_mode((700, 500), pygame.HWSURFACE | pygame.DOUBLEBUF) # creates pygame window (size)
        self.image = pygame.transform.smoothscale(pygame.image.load("arrow_down.png").convert_alpha(), (50, 50))
        font = pygame.font.Font(None, 36)
        for i in self.stratagems:
            i["code_image"] = []
            for y in i["code"]:
                if y == "1":
                    i["code_image"].append(pygame.transform.smoothscale(pygame.image.load("arrow_up.png").convert_alpha(), (50, 50)))
                elif y == "2":
                    i["code_image"].append(pygame.transform.smoothscale(pygame.image.load("arrow_right.png").convert_alpha(), (50, 50)))
                elif y == "3":
                    i["code_image"].append(pygame.transform.smoothscale(pygame.image.load("arrow_down.png").convert_alpha(), (50, 50)))
                elif y == "4":
                    i["code_image"].append(pygame.transform.smoothscale(pygame.image.load("arrow_left.png").convert_alpha(), (50, 50)))
                else:
                    continue
        SAC = 0 # stratagem_amount_count
        while True: # creates a list of stratagems for the user to complete
            if SAC < self.mode_amount:
                self.stratagem_list_code_image.append(random.choice(self.stratagems)["code_image"])
                SAC += 1
            else:
                print(self.stratagem_list_code_image)
                print(self.stratagem_list_code_image[0])
                break

        self.text_surface = font.render("Manual Text", True, (255, 255, 255)) # defines text to be displayed
        pygame.display.set_caption("Duck Stratagem") # Display window name
        self._running = True # sets var to true when game runs again?
    def on_event(self, event):
        if event.type == pygame.QUIT: # if the game is exitted out of
            self._running = False # sets var to false
    def on_loop(self):
        pass
    def on_render(self):
        self.display.fill((display_bg)) # sets displays colour
    def on_cleanup(self):
        pygame.quit() # cleanly quits the game when game is quitted
    def on_execute(self):
        if self.on_init() == False: # error handler???
            self._running = False 
        while(self._running): # constant loop when _running is true
            self.FPS.tick(60) # sets fps to 60
            
            for i in self.stratagem_list_code_image:
                self.display.blit(i, (100, 100)) # displays text


            for event in pygame.event.get(): # grabs the events (keyboard triggers etc)
                self.on_event(event) # checks if the game has 'quitted'?
                pygame.display.flip() # updates display
            self.on_loop()
            self.on_render()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

    '''
    self.display.blit(self.image, (100, 100))
            self.display.blit(self.image, (101, 100))
            self.display.blit(self.image, (100, 101))'''