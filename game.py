import pygame
import random
import sys
import time
from pygame.locals import *

## Eagle Stratagems
ESR = {"name": "Eagle Strafing Run", "codeName": "ESR", "code": "122"}
EA = {"name": "Eagle Airstrike", "codeName": "EA", "code": "1232"}
ECB = { "name": "Eagle Cluster Bomb", "codeName": "ECB", "code": "12332"}
ESS = {"name": "Eagle Smoke Strike", "codeName": "ESS", "code": "1213"}
ENA = {"name": "Eagle Napalm Airstrike", "codeName": "ENA", "code": "1231"}
E110RP = {"name": "Eagle 110mm Rocket Pods", "codeName": "E110RP", "code": "1214"}
ESB = {"name": "Eagle 500kg Bomb", "codeName": "ESB", "code": "12333"}

## Orbital Strikes
OPS = {"name": "Orbital Precision Strike", "codeName": "OPS", "code": "221"}
OGB = {"name": "Orbital Gatling Barrage", "codeName": "OGB", "code": "23411"}
OGS = {"name": "Orbital Gas Strike", "codeName": "OGS", "code": "12333"}
O120HEB = {"name": "Orbital 120mm HE Barrage", "codeName": "O120HEB", "code": "223423"}
OAS = {"name": "Orbital Airburst Strike", "codeName": "OAS", "code": "222"}
OSS = {"name": "Orbital Smoke Strike", "codeName": "OSS", "code": "2231"}
OEMSS = {"name": "Orbital EMS Strike", "codeName": "OEMSS", "code": "2243"}
O380HEB = {"name": "Orbital 380mm HE Barrage", "codeName": "O380HEB", "code": "2311433"}
OWB = {"name": "Orbital Walking Barrage", "codeName": "OWB", "code": "232323"}
OL = {"name": "Orbital Laser", "codeName": "OL", "code": "23123"}
ONB = {"name": "Orbital Napalm Barrage", "codeName": "ONB", "code": "223421"}
ORS = {"name": "Orbital Railcannon Strike", "codeName": "ORS", "code": "21332"}

display_bg = pygame.Color(0, 0, 0) # background colour for pygame display
class App:
    def __init__(self):
        self.image_names = ("arrow_up.png", "arrow_right.png", "arrow_down.png", "arrow_left.png") # list of the names of the file
        self.image_names_var = ("arrow_up", "arrow_right", "arrow_down", "arrow_left", "Barrow_up", "Barrow_right", "Barrow_down", "Barrow_left") # the variable name options
        self.keypress_list = (pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
        self.image_var_dict = {}

        self._running = True # sets var to true when game runs
        self._display_surf = None # def the var for display
        self.FPS = pygame.time.Clock() # def FPS by clock

        self.stratagemList_ci_hand = [] # list of stratagems code for the user to complete
        self.stratagemList_hand = []
        self.mode = None # how hard/many stratagems
        self.mode_options = ("Trivial", "Hard", "Super Helldive") # the different difficulties
        self.mode_amount = 5 # temp mode ammount
        self.stratagem_list_code = []
        self.name_stratagem_text = ""
        self.stratagem_text = ""

        self.list_completion = 0
        self.code_completion = -1
    def on_init(self):
        pygame.init()
        self.stratagems = (ESR, EA, ECB, ESS, ENA, E110RP, ESB, OPS, OGB, OGS, O120HEB, OAS, OSS, OEMSS, O380HEB, OWB, OL, ONB, ORS) # Stratagem codes
        self.display = pygame.display.set_mode((700, 500), pygame.HWSURFACE | pygame.DOUBLEBUF) # creates pygame window (size)
        font = pygame.font.Font("font.ttf", 36) # font

        '''Images'''
        for i in range(len(self.image_names_var)): # find length of the list for each index
            if i <= 3: # if the index < 4
                image = pygame.transform.smoothscale(pygame.image.load(self.image_names[i]).convert_alpha(), (50, 50))
                # ^ creates an image by grabbing the image name with the same index in inmage_name (which should be the same direction)
                image.set_alpha(50) # turn the opacity to 50/255
                self.image_var_dict[self.image_names_var[i]] = image 
                # ^ adds a dict to the dict(image_var_dict) which the key is the value from image_name_var which it was in the begining
            elif i > 3: # if the index is bigger than 3 (indicating its a bold/bright arrow (last 4 in the list))
                y = i # creates a temp variable y
                y -= 4 # minuses 4 to match up with the image_name (y-4 will be the same direction, y is just it bolded/brigther)
                image = pygame.transform.smoothscale(pygame.image.load(self.image_names[y]).convert_alpha(), (50, 50))
                # ^ creates an image by grabbing the image name in inmage_names which is the same index just minused 4 which will be the same direction
                image.set_alpha(255) # makes the image fully opaque
                self.image_var_dict[self.image_names_var[i]] = image
                # ^ adds a dict to the dict(image_var_dict) which key is the i from before

        '''Length of code for each stratagem'''
        for i in self.stratagems:
            i["length"] = len(i["code"])

        '''Creating list of images for each dictonary in the stratagem list'''
        # code that goes through the codes of the stratagem and creates a list of images which is corrolates to the code 
        for i in self.stratagems: # for dict in the stratagem list
            i["codeImageList"] = [] # create a empty dict key/list for the images
            for y in i["code"]: # for every character in the code
                if y == "1": # if the character is 1
                    i["codeImageList"].append(self.image_var_dict[self.image_names_var[0]]) 
                    # ^ goes to the image dict (image_var_dict) and grabs the first or index 0 valve and adds it to the codeImageList in the dict 
                    # since 1 = up and the index 0 is up
                elif y == "2": # checks if it is anyother number
                    i["codeImageList"].append(self.image_var_dict[self.image_names_var[1]])
                elif y == "3":
                    i["codeImageList"].append(self.image_var_dict[self.image_names_var[2]])
                elif y == "4":
                    i["codeImageList"].append(self.image_var_dict[self.image_names_var[3]])
                else:
                    print("Brokey Brokey Fix Your Codey")

        '''How many stratagems(code images) are added in a hand'''
        SAC = 0 # stratagem_amount_count
        while True: # creates a list of stratagems for the user to complete
            if SAC < self.mode_amount: # checks if it has created enough codes
                temp_stratagem = random.choice(self.stratagems)
                self.stratagemList_hand.append(temp_stratagem)
                self.stratagemList_ci_hand.append(temp_stratagem["codeImageList"]) 
                # ^ grabs a random stratagem image code list and adds it to the stratagem list code images list
                # A random dict/variable in stratagems and grabs the "codeImageList" and adds it to another list which is the playing hand
                SAC += 1 # adds 1 to the count to indicated another has been added
            else:
                break
        
        self.text_surface = font.render("Manual Text", True, (255, 255, 255)) # defines text to be displayed
        pygame.display.set_caption("Duck Stratagem") # Display window name
        self._running = True # sets var to true when game runs again?

    def code_image_display_active(self, completion):
        '''Function that will grab the first code image of the list and display it'''

        '''This code will check if the user has made process of the code and will make the correct ones brighter'''
        if completion != -1: # if the completion number is not 0
            if completion < self.stratagemList_hand[0]["length"]: # Checks if the completion index is smaller or equal to the length of the current code
            # ^ if the completion index(the index of the correct press key) is smaller or equal to the length of the code
                temp_image = (self.stratagemList_ci_hand[0])[completion] # create a temp variable of the completion index of whatever the list is (what the player is on)
                for i in range(4): # for 0-3
                    if self.image_var_dict[self.image_names_var[i]] == temp_image: 
                    # ^ goes through the first 4 k eys (i changing) to see if the value is the same inwhich, we know what the code image is
                        (self.stratagemList_ci_hand[0])[completion] = self.image_var_dict[self.image_names_var[i+4]]
                        # ^ changes the code image to a bolder/brigher image
                        # ^ goes to whatever the list code the player is on, goes into the image/value they are on and changes into the dict value of the original image + 4
                        if completion+1 == self.stratagemList_hand[0]["length"]:
                        # ^ if the completion index (the index of the completed code image) is more than length (compels and entire code) it grabs a new code by removing the first 
                            self.code_completion = -1 # resets the progress on the code (because its a new list)

                            self.stratagemList_ci_hand.pop(0) # removes the first list item
                            self.stratagemList_hand.pop(0)# removes the first list item
                

        '''displays the image (the code)'''
        for i in range(len(self.stratagemList_ci_hand[0])):
            tcinp = 100 + (i*55) # temp code image number position
            self.display.blit((self.stratagemList_ci_hand[0])[i], (tcinp, 100)) # displays code image
            self.display.blit((self.stratagemList_ci_hand[0])[i], (tcinp+1, 100)) # displays code image - bolder
            self.display.blit((self.stratagemList_ci_hand[0])[i], (tcinp, 101)) # displays code image - bolder


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

            self.code_image_display_active(self.code_completion) # displays code image function
            
            for event in pygame.event.get(): # grabs the events (keyboard triggers etc)
                self.on_event(event) # checks if the game has 'quitted'?
                pygame.display.flip() # updates display
                if event.type == pygame.KEYDOWN:
                    for i in self.keypress_list:
                        check_code_index = self.code_completion + 1
                        if event.key == i: # simplify this in the future (or when I'm bothered)
                            print(event.key)
                            print(i)
                            print(self.keypress_list[0])
                            print(self.keypress_list[4])
                            print(((self.stratagemList_hand[0])["code"])[check_code_index])
                            print()
                            if i == self.keypress_list[0] or i == self.keypress_list[4]:
                                print(1)
                                if "1" == ((self.stratagemList_hand[0])["code"])[check_code_index]:
                                    self.code_completion += 1
                                    print("w")
                                else:
                                    pass
                            elif i == self.keypress_list[1] or i == self.keypress_list[5]:
                                print(2)
                                if "2" == ((self.stratagemList_hand[0])["code"])[check_code_index]:
                                    self.code_completion += 1
                                    print("a")
                                else:
                                    pass
                            elif i == self.keypress_list[2] or i == self.keypress_list[6]:
                                print(3)
                                if "3" == ((self.stratagemList_hand[0])["code"])[check_code_index]:
                                    self.code_completion += 1 
                                    print("s")
                                else:
                                    pass
                            elif i == self.keypress_list[3] or i == self.keypress_list[7]:
                                print(4)
                                if "4" == ((self.stratagemList_hand[0])["code"])[check_code_index]:
                                    self.code_completion += 1
                                    print("d")
                                else:
                                    pass
            
            

            

            self.on_loop()
            self.on_render()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()