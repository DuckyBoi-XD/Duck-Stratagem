import pygame
import random
from pygame.locals import *

## Eagle Stratagems
ESR = {"name": "Eagle Strafing Run", "codeName": "ESR", "code": "122"}
EA = {"name": "Eagle Airstrike", "codeName": "EA", "code": "1232"}
ECB = { "name": "Eagle Cluster Bomb", "codeName": "ECB", "code": "12332"}
ESS = {"name": "Eagle Smoke Strike", "codeName": "ESS", "code": "1213"}
ENA = {"name": "Eagle Napalm Airstrike", "codeName": "ENA", "code": "1231"}
E110RP = {"name": "Eagle 110mm Rocket Pods", "codeName": "E110RP", "code": "1214"}
E500B = {"name": "Eagle 500kg Bomb", "codeName": "E500B", "code": "12333"}

## Orbital Strikes
OPS = {"name": "Orbital Precision Strike", "codeName": "OPS", "code": "221"}
OGB = {"name": "Orbital Gatling Barrage", "codeName": "OGB", "code": "23411"}
OGS = {"name": "Orbital Gas Strike", "codeName": "OGS", "code": "2232"}
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
        self.image_names = ("assets/arrows/arrow_up.png", "assets/arrows/arrow_right.png", "assets/arrows/arrow_down.png", "assets/arrows/arrow_left.png", 
                            "assets/arrows/arrow_up_bold.png", "assets/arrows/arrow_right_bold.png", "assets/arrows/arrow_down_bold.png", "assets/arrows/arrow_left_bold.png") 
                            # ^ list of the names of arrow file
        self.image_names_var = ("arrow_up", "arrow_right", "arrow_down", "arrow_left", "arrow_up_bold", "arrow_right_bold", "arrow_down_bold", "Barrow_left_bold") # the variable name options
        self.stratagem_image = ("assets/stratagempng/ESR.png", "assets/stratagempng/EA.png", "assets/stratagempng/ECB.png", "assets/stratagempng/ESS.png", "assets/stratagempng/ENA.png", 
                            "assets/stratagempng/E110RP.png", "assets/stratagempng/E500B.png", "assets/stratagempng/OPS.png", "assets/stratagempng/OGB.png", "assets/stratagempng/OGS.png", 
                            "assets/stratagempng/O120HEB.png", "assets/stratagempng/OAS.png", "assets/stratagempng/OSS.png", "assets/stratagempng/OEMSS.png", "assets/stratagempng/O380HEB.png", 
                            "assets/stratagempng/OWB.png", "assets/stratagempng/OL.png", "assets/stratagempng/ONB.png", "assets/stratagempng/ORS.png") # list of the names of the file for the stratagem images
        self.keypress_list = (pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
        self.image_var_dict = {}

        self.fps = 60
        self.colour = (254, 254, 17)
        self.red_colour = (224, 0, 0)

        self._running = True # sets var to true when game runs
        self._display_surf = None # def the var for display
        self.FPS = pygame.time.Clock() # def FPS by clock

        self.stratagemList_ci_hand = [] # list of stratagems code for the user to complete
        self.stratagemList_hand = [] # list of the stratagems in the hand
        self.stratagemList_hand_reset = [] # the current code image used to reset the progress
        self.stratagemList_hand_images = [] # list of the stratagem pictures
        self.mode_amount = 5 # temp mode ammount (ammount of stratagems in a hand)
        self.round = 1
        self.score = 0

        self.list_completion = 0 # varialbe to track what index of the list (compleded code)
        self.code_completion = -1 # progress on the code
        self.completion_tracker = False # stops repitition of games code

        self.displayWidth = 1000 # width of display
        self.displayHeight = 450 # height of display
        self.stratagem_text_width = None # width of the text
        self.stratagem_text_height = None # height of the text
        self.stratagem_text_y = 181 # text y position
        self.stratagem_codeimage_y = None # code image y position
        self.stratagem_rectangle_width = 40 # rectangle width
        self.size_code_image = 50
        self.tcpin = None # x position for all display objects to be based on
        self.text_space_y = None
        self.stratagem_imge_list_width = None

        self.time_countdown_start = 15 * self.fps
        self.time_countdown = 15 * self.fps
        self.time_increase = 1.5 * self.fps

        self.game_starting_value = True
        self.cooldown_start = 3 * self.fps
        self.countdown = 3 * self.fps
        self.game_start_screen = True
        self.midgame_start = False
        self.game_play = False
        self.points_scoring = False

        self.perfection_track = True
        self.score_adder = True
        self.total_score_value = 0
        self.key_allow = False
        self.display_score_time = 180
        self.display_score_time_start = 180
        self.score_display_list = []
        self.keypress_game_start = False

        self.high_scores = [5, 2, 9]
        self.high_scores.sort(reverse=True)
        self.end_game = False
        self.round_stratagem_score = 0
        self.end_game_time = 120
        self.end_game_prevention = False
        self.end_game_start = False
        self.end_game_input_checker = False

    def on_init(self):
        pygame.init()
        self.stratagems = (ESR, EA, ECB, ESS, ENA, E110RP, E500B, OPS, OGB, OGS, O120HEB, OAS, OSS, OEMSS, O380HEB, OWB, OL, ONB, ORS) # Stratagem codes
        self.display = pygame.display.set_mode((self.displayWidth, self.displayHeight), pygame.HWSURFACE | pygame.DOUBLEBUF) # creates pygame window (size)
        self.font = pygame.font.Font("assets/font/font.ttf", 25) # font
        self.fontp2 = pygame.font.Font("assets/font/font.ttf", 20) # 2nd paragraphfont
        self.titlefont = pygame.font.Font("assets/font/titlefont.ttf", 30) # font for title
        self.titlefonth2 = pygame.font.Font("assets/font/titlefont.ttf", 25) # 2nd font for title

        '''Images'''
        for i in range(len(self.image_names_var)): # find length of the list for each index
                image = pygame.transform.smoothscale(pygame.image.load(self.image_names[i]).convert_alpha(), (self.size_code_image, self.size_code_image))
                # ^ creates an image by grabbing the image name with the same index in image_name (which should be the same direction)
                self.image_var_dict[self.image_names_var[i]] = image 
                # ^ adds a dict to the dict(image_var_dict) which the key is the value from image_name_var which it was in the begining
    
        # assigns each stratagem with the correct image of the stratagem
        a = 0
        for i in self.stratagems:
            image = pygame.transform.smoothscale(pygame.image.load(self.stratagem_image[a]).convert_alpha(), (75, 75))
            image.set_alpha(100)
            i["image"] = image
            a += 1

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
                self.stratagemList_hand_images.append(temp_stratagem["image"])
                # ^ grabs a random stratagem image code list and adds it to the stratagem list code images list
                # A random dict/variable in stratagems and grabs the "codeImageList" and adds it to another list which is the playing hand
                SAC += 1 # adds 1 to the count to indicated another has been added
            else:
                self.stratagemList_hand_reset = self.stratagemList_ci_hand[0].copy() # sets the reset hand as the hand at the start
                break

        self.stratagem_imge_list_width = (len(self.stratagemList_hand_images[0:6]) * 100) + 25
        pygame.display.set_caption("Duck Stratagem") # Display window name
        self._running = True # sets var to true when game runs again?

    def starting_game(self):
        '''Begining screen when playing the game'''
        start_text_title_txt = "Duck Stratagem"
        start_text_txt = "Press any stratagem input to start!"

        start_text_title = self.titlefont.render(start_text_title_txt, True, (255, 255, 255))
        start_text = self.font.render(start_text_txt, True, self.colour)

        start_text_titlex, start_text_titley = self.titlefont.size(start_text_title_txt)
        start_textx, start_texty = self.font.size(start_text_txt)

        start_text_title_height = (self.displayHeight - (start_text_titley + 50 + start_texty))/2
        start_text_height = (self.displayHeight - start_text_titley + 50)/2

        self.display.blit(start_text_title, ((self.displayWidth - start_text_titlex)/2, start_text_title_height)) # displays it
        self.display.blit(start_text, ((self.displayWidth - start_textx)/2, start_text_height)) # displays it

        pygame.draw.rect(self.display, (255, 255, 255), (0, 40, self.displayWidth, 10), width=0, border_radius=0)
        pygame.draw.rect(self.display, (255, 255, 255), (0, self.displayHeight - 50, self.displayWidth, 10), width=0, border_radius=0)

    def game_starting(self):
        '''game starting countdown'''
        self.countdown -= 1
        if 180 >= self.countdown > 120:
            countdown_text = "3"
        elif 120 >= self.countdown > 60:
            countdown_text = "2"
        elif 60 >= self.countdown > 0:
            countdown_text = "1"
        else:
            countdown_text = "0"
            if self.game_starting_value is True:
                self.game_starting_value = False

        pygame.draw.rect(self.display, (255, 255, 255), (0, 40, self.displayWidth, 10), width=0, border_radius=0)
        pygame.draw.rect(self.display, (255, 255, 255), (0, self.displayHeight - 50, self.displayWidth, 10), width=0, border_radius=0)

        # creating and displaying the text/objects
        countdown_text_title = self.titlefont.render("Get Ready", True, (255, 255, 255))
        countdown_text_text = self.font.render(f"Round {self.round}", True, self.colour)
        countdown_text_value = self.font.render(countdown_text, True, (255, 255, 255))

        cttWidth, cttLength = self.titlefont.size("Get Ready")
        cttxtWidth, cttxtLength = self.font.size(f"Round {self.round}")
        ctvWidth, ctvLength = self.font.size(countdown_text)

        cttx = (self.displayWidth - cttWidth)/2
        cttxtx = (self.displayWidth - cttxtWidth)/2
        ctvx = (self.displayWidth - ctvWidth)/2

        ctty = (self.displayHeight - (cttLength + cttxtLength + ctvLength + 45))/2
        cttxty = ctty + cttLength + 15
        ctvy = cttxty + cttxtLength + 15

        self.display.blit(countdown_text_title, (cttx, ctty))
        self.display.blit(countdown_text_text, (cttxtx, cttxty))
        self.display.blit(countdown_text_value, (ctvx, ctvy))
        
    def code_image_display_active(self, completion):
        '''Function that will grab the first code image of the list and display it'''

        '''This code will check if the user has made process of the code and will make the correct ones brighter'''
        if completion == -1:
            self.stratagemList_ci_hand[0] = self.stratagemList_hand_reset.copy()
        elif completion != -1: # if the completion number is not 0
            if completion < self.stratagemList_hand[0]["length"] and self.completion_tracker == False: # Checks if the completion index is smaller or equal to the length of the current code
            # ^ if the completion index(the index of the correct press key) is smaller or equal to the length of the code
                for b in range(completion+1):
                    temp_image = (self.stratagemList_ci_hand[0])[b] # create a temp variable of the completion index of whatever the list is (what the player is on)
                    for i in range(4): # for 0-3
                        if self.image_var_dict[self.image_names_var[i]] == temp_image: 
                        # ^ goes through the first 4 keys (i changing) to see if the value is the same in which, we know what the code image is
                            (self.stratagemList_ci_hand[0])[b] = self.image_var_dict[self.image_names_var[i+4]]
                            # ^ changes the code image to a bolder/brigher image
                            # ^ goes to whatever the list code the player is on, goes into the image/value they are on and changes into the dict value of the original image + 4
                            self.completion_tracker = True

        image = self.stratagemList_hand_images[0].copy()
        image.set_alpha(255)
        image = pygame.transform.smoothscale(image, (100, 100))
        self.stratagemList_hand_images[0] = image
            
        '''displays the image of the stratagem'''
        for i in range(len(self.stratagemList_hand_images[0:6])): # the rangle length of the hand images
            if i == 0: # if the value is the second one in the list
                self.tcpin = (self.displayWidth-self.stratagem_imge_list_width)/2
                self.display.blit((self.stratagemList_hand_images[i]), (self.tcpin, 75)) # prints main images
            else:
                tcinp = (i*(100)) + self.tcpin + 25
                self.display.blit((self.stratagemList_hand_images[i]), (tcinp, 87.5)) # prints images

        '''Displays text & colour accents'''
        self.stratagem_text_width, self.stratagem_text_height = self.font.size((self.stratagemList_hand[0])["name"]) # grabs the measurements of the text
        text_spaceside = ((self.stratagem_imge_list_width - self.stratagem_text_width)/2) + self.tcpin # calculates the side of the screen from the start of the text to centre it
        self.text_space_y = self.stratagem_text_y - ((self.stratagem_rectangle_width - self.stratagem_text_height)/2)

        '''displays the image (the code)'''
        length_of_list = self.stratagemList_hand[0]["length"]
        stratagem_codeimage_width = (length_of_list*self.size_code_image) + ((length_of_list-1)*20)
        codeImage_extra_space = ((self.stratagem_imge_list_width - stratagem_codeimage_width)/2)

        self.stratagem_codeimage_y = self.text_space_y + self.stratagem_rectangle_width + ((75 - self.size_code_image)/2)
        for i in range(len(self.stratagemList_ci_hand[0])):
            tcinp = self.tcpin + codeImage_extra_space + (i*(self.size_code_image+20)) # temp code image number position
            self.display.blit((self.stratagemList_ci_hand[0])[i], (tcinp, self.stratagem_codeimage_y)) # displays code image

        pygame.draw.rect(self.display, self.colour, (self.tcpin, self.text_space_y, self.stratagem_imge_list_width, self.stratagem_rectangle_width), width=0, border_radius=0)
        pygame.draw.lines(self.display, self.colour, closed=True, points=
            [(self.tcpin +1, 77),
             (self.tcpin+98, 77), 
             (self.tcpin+98, 175), 
             (self.tcpin +1, 175)], width=3)
        text = self.font.render((self.stratagemList_hand[0])["name"], True, (0, 0, 0)) # creates the text data
        self.display.blit(text, (text_spaceside, self.stratagem_text_y)) # displays it


        roundTextTitle = self.font.render("Round", True, (255, 255, 255)) # creates the text data
        roundTextTitlex, roundTextTitley = self.font.size("Round")
        self.display.blit(roundTextTitle, ((self.tcpin - roundTextTitlex)/2, 90)) # displays it

        roundTextValue = self.font.render(str(self.round), True, self.colour) # creates the text data
        self.display.blit(roundTextValue, ((self.tcpin - roundTextTitlex)/2, 115)) # displays it

        scoreTextTitle = self.font.render("Score", True, (255, 255, 255)) # creates the text data
        scoreTextTitlex, scoreTextTitley = self.font.size("Score")
        scoreTextValuex, scoreTextValuey = self.font.size(str(int(self.score)))
        self.display.blit(scoreTextTitle, (self.tcpin + self.stratagem_imge_list_width + (self.tcpin - scoreTextTitlex)/2, 115)) # displays it

        scoreTextValue = self.font.render(str(int(self.score)), True, self.colour) # creates the text data
        self.display.blit(scoreTextValue, (self.tcpin + self.stratagem_imge_list_width + ((self.tcpin - scoreTextTitlex)/2) + scoreTextTitlex - scoreTextValuex, 90)) # displays it

        pygame.draw.rect(self.display, (255, 255, 255), (0, 40, self.displayWidth, 10), width=0, border_radius=0)
        pygame.draw.rect(self.display, (255, 255, 255), (0, self.displayHeight - 50, self.displayWidth, 10), width=0, border_radius=0)

    def timer_countdown(self):
        time_bar = self.time_countdown*(self.stratagem_imge_list_width/self.time_countdown_start)
        pygame.draw.rect(self.display, (153, 153, 153), (self.tcpin, self.stratagem_codeimage_y + 100, self.stratagem_imge_list_width, 20), width=0, border_radius=0)
        pygame.draw.rect(self.display, self.colour, (self.tcpin, self.stratagem_codeimage_y + 100, time_bar, 20), width=0, border_radius=0)

        self.time_countdown -= 1
        if self.time_countdown <= 0:
            pass

    
    def score_count(self):
        '''End of round score calculator/display'''
        pygame.draw.rect(self.display, (255, 255, 255), (0, 40, self.displayWidth, 10), width=0, border_radius=0)
        pygame.draw.rect(self.display, (255, 255, 255), (0, self.displayHeight - 50, self.displayWidth, 10), width=0, border_radius=0)

        # all the text/title
        score_points_title_str = "Points Scored"
        stratagem_completion_text_str = "Round Points"
        time_bonus_text_str = "Time Bonus"
        perfect_multi_text_str = "Perfection Multiplier"
        round_multi_text_str = "Round Multiplier"
        total_score_str = "Total Round Score"
        score_str = "Total Score"
        next_round_str = "Press any stratagem input to start!"

        #converting values into pygame text
        score_points_title = self.titlefonth2.render(score_points_title_str, True, (255, 255, 255))
        stratagem_completion_text = self.fontp2.render(stratagem_completion_text_str, True, self.colour)
        time_bonus_text = self.fontp2.render(time_bonus_text_str, True, self.colour)
        perfect_multi_text = self.fontp2.render(perfect_multi_text_str, True, self.colour)
        round_multi_text = self.fontp2.render(round_multi_text_str, True, self.colour)
        total_score_text = self.fontp2.render(total_score_str, True, (255, 255, 255))
        score_text = self.fontp2.render(score_str, True, (255, 255, 255))
        next_round_text = self.fontp2.render(next_round_str, True, self.colour)


        cptWidth, cptLength = self.titlefont.size(score_points_title_str)
        sctWidth, sctLength = self.fontp2.size(stratagem_completion_text_str)
        tbtWidth, tbtLength = self.fontp2.size(time_bonus_text_str)
        pmtWidth, pmtLength = self.fontp2.size(perfect_multi_text_str)
        rmtWidth, rmtLength = self.fontp2.size(round_multi_text_str)
        tsWidth, tsLength = self.fontp2.size(total_score_str)
        sdWidth, sdLength = self.fontp2.size(score_str)
        nrWidth, nrLength = self.fontp2.size(next_round_str)

        stratagem_completion_value_text = self.fontp2.render(self.stratagem_completion_value, True, self.colour)
        time_bonus_value_text = self.fontp2.render(self.time_bonus_value, True, self.colour)
        perfect_multi_value_text = self.fontp2.render(self.perfect_multi_value, True, self.perfect_multi_colour)
        round_multi_value_text = self.fontp2.render(self.round_multi_value, True, self.colour)
        total_score_value_text = self.fontp2.render(str(self.total_score_value), True, (255, 255, 255))
        score_display_value_text = self.fontp2.render(self.score_value, True, (255, 255, 255))

        self.display.blit(score_points_title, ((self.displayWidth - cptWidth)/2, 70))
        if self.display_score_time == 180:
            self.score_display_list.append(stratagem_completion_text)
            self.score_display_list.append(stratagem_completion_value_text)
        elif self.display_score_time == 150:
            self.score_display_list.append(time_bonus_text)
            self.score_display_list.append(time_bonus_value_text)
        elif self.display_score_time == 120:
            self.score_display_list.append(perfect_multi_text)
            self.score_display_list.append(perfect_multi_value_text)
        elif self.display_score_time == 90:
            self.score_display_list.append(round_multi_text)
            self.score_display_list.append(round_multi_value_text)
        elif self.display_score_time == 60:
            self.score_display_list.append(total_score_text)
            self.score_display_list.append(total_score_value_text)
        elif self.display_score_time == 30:
            self.score_display_list.append(score_text)
            self.score_display_list.append(score_display_value_text)
            self.score_display_list.append(next_round_text)

        display_text_length = (cptLength, sctLength, tbtLength, pmtLength, rmtLength, tsLength, sdLength)
        DFT = 65
        DTL = 0
        for index, i in enumerate(self.score_display_list):
            if index % 2 == 0:
                DTL += display_text_length[int(index/2)]
                DFT += 15
                y = DFT + DTL
                if index == 12:
                    self.display.blit(i, ((self.displayWidth-nrWidth)/2, y))
                    self.midgame_start = True
                else:
                    self.display.blit(i, (150, y))
                    self.display.blit(self.score_display_list[index+1], (self.displayWidth - 250, y))
        self.display_score_time -= 1

    def end_screen(self):
        pygame.draw.rect(self.display, (255, 255, 255), (0, 40, self.displayWidth, 10), width=0, border_radius=0)
        pygame.draw.rect(self.display, (255, 255, 255), (0, self.displayHeight - 50, self.displayWidth, 10), width=0, border_radius=0)

        end_screen_title_str = "GAME OVER"
        high_score_text_str = "High Score"
        top_high_score_value_str = "1. " + str(self.high_scores[0])
        mid_high_score_value_str = "2. " + str(self.high_scores[1])
        bottom_high_score_value_str = "3. " + str(self.high_scores[2])
        score_text_str = "Score"
        score_value_str = str(int(self.score))
        new_game_text_str = "Press any input stratagem to start a new game"

        end_screen_title = self.titlefont.render(end_screen_title_str, True, self.red_colour)
        high_score_text = self.font.render(high_score_text_str, True, self.colour)
        top_high_score_value = self.fontp2.render(top_high_score_value_str, True, (255, 255, 255))
        mid_high_score_value = self.fontp2.render(mid_high_score_value_str, True, (255, 255, 255))
        bottom_high_score_value = self.fontp2.render(bottom_high_score_value_str, True, (255, 255, 255))
        score_text = self.font.render(score_text_str, True, self.colour)
        score_value = self.fontp2.render(score_value_str, True, (255, 255, 255))
        new_game_text = self.font.render(new_game_text_str, True, self.colour)

        estWidth, estLength = self.titlefont.size(end_screen_title_str)
        hstWidth, hstLength = self.font.size(high_score_text_str)
        thsvWidth, thsvLength = self.fontp2.size(top_high_score_value_str)
        stWidth, stLength = self.font.size(score_text_str)
        svWidth, svLength = self.fontp2.size(score_value_str)
        ngtWidth, ngtLength = self.font.size(new_game_text_str)

        high_score_list = [top_high_score_value, mid_high_score_value, bottom_high_score_value]

        DFT = 80
        self.display.blit(end_screen_title, ((self.displayWidth-estWidth)/2, DFT))
        DFT += (20 + estLength)
        self.display.blit(high_score_text, ((self.displayWidth-hstWidth)/2, DFT))
        DFT += (3 + hstLength)

        for i in high_score_list:
            self.display.blit(i, ((self.displayWidth-hstWidth)/2, DFT))
            DFT += (3 + thsvLength)

        DFT += 20
        self.display.blit(score_text, ((self.displayWidth-stWidth)/2, DFT))
        DFT += (5 + stLength)
        self.display.blit(score_value, ((self.displayWidth-svWidth)/2, DFT))
        if self.end_game_time <= 0:
            self.display.blit(new_game_text, ((self.displayWidth-ngtWidth)/2, (self.displayHeight-100)))
            self.end_game_prevention = False
            self.end_game_input_checker = True
        if self.end_game_time > 0:
            self.end_game_time -= 1

    def on_event(self, event):
        if event.type == pygame.QUIT: # if the game is exitted out of
            self._running = False # sets var to false
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit() # cleanly quits the game when game is quitted
    def on_execute(self):
        if self.on_init() == False: # error handler???
            self._running = False 
        while(self._running): # constant loop when _running
            self.FPS.tick(self.fps) # sets fps
            
            '''Tracks the user's keyboard input and checks if it is correct'''
            for event in pygame.event.get(): # grabs the events (keyboard triggers etc)
                self.on_event(event) # checks if the game has 'quitted'?
                if event.type == pygame.KEYDOWN: # if the event is a key press
                    for i in self.keypress_list: # for every value in the keypress list (key presses like wasd and arrow keys)
                        check_code_index = self.code_completion + 1 # creates variable of check code index
                        if event.key == i: # if the event key is one of the values in keypress (doesn't active if its a random key)
                            break_value = 0
                            if self.end_game_prevention is True:
                                break
                            if self.end_game_input_checker is True:
                                self.end_game_input_checker = False
                                self.end_game_start = True
                                self.end_game_time = 120
                                self.score = 0
                                self.end_game = False
                                self.time_countdown = self.time_countdown_start
                                break
                            if self.game_start_screen is True:
                                self.game_start_screen = False
                                self.count = self.time_countdown_start
                                break_value = 1
                            if self.midgame_start is True:
                                self.midgame_start = False
                                self.points_scoring = False
                                self.countdown = self.cooldown_start
                                break_value = 1
                            if self.key_allow is False:
                                break_value = 1
                            if break_value == 1:
                                break
                            for a in range(4): # goes through each value from 0-3
                                if i == self.keypress_list[a] or i == self.keypress_list[a+4]:
                                # ^ if the user pressed key is equal to 2 values in keypress list
                                    if f"{a+1}" == ((self.stratagemList_hand[0])["code"])[check_code_index]:
                                    # ^ if a + 1 (range index that is equal to the keypress +1 to be aligned with the code) equals  the first digit in the code (the first code) 
                                        self.code_completion += 1 # adds one to code completion counter
                                        self.completion_tracker = False
                                        if self.code_completion +1 == self.stratagemList_hand[0]["length"]:
                                        # ^ if the completion index (the index of the completed code image) is more than length (compels and entire code) it grabs a new code by removing the first 
                                            try:
                                                self.code_completion = -1 # resets the progress on the code (because its a new list)
                                                self.stratagemList_ci_hand.pop(0) # removes the first list item
                                                self.stratagemList_hand.pop(0)# removes the first list item
                                                self.stratagemList_hand_images.pop(0)
                                                self.stratagemList_hand_reset = self.stratagemList_ci_hand[0].copy() # sets the reset hand to the new code
                                                self.time_countdown += self.time_increase
                                                self.score += 20
                                                 
                                                if self.time_countdown > self.time_countdown_start:
                                                    self.time_countdown = self.time_countdown_start
                                                break
                                            except IndexError:
                                                self.score += 20
                                                SAC = 0 # stratagem_amount_count
                                                self.mode_amount += 1
                                                if self.mode_amount % 10 == 0:
                                                    self.time_increase -= 5
                                                while True: # creates a list of stratagems for the user to complete
                                                    if SAC < self.mode_amount: # checks if it has created enough codes
                                                        temp_stratagem = random.choice(self.stratagems)
                                                        self.stratagemList_hand.append(temp_stratagem)
                                                        self.stratagemList_ci_hand.append(temp_stratagem["codeImageList"])
                                                        self.stratagemList_hand_images.append(temp_stratagem["image"])
                                                        # ^ grabs a random stratagem image code list and adds it to the stratagem list code images list
                                                        # A random dict/variable in stratagems and grabs the "codeImageList" and adds it to another list which is the playing hand
                                                        SAC += 1 # adds 1 to the count to indicated another has been added
                                                    else:   
                                                        self.stratagemList_hand_reset = self.stratagemList_ci_hand[0].copy() # sets the reset hand as the hand at the start
                                                        self.round += 1
                                                        self.points_scoring = True
                                                        self.time_countdown += self.time_increase
                                                        if self.time_countdown > self.time_countdown_start:
                                                            self.time_countdown = self.time_countdown_start
                                                        # calculates the scores for the round
                                                        self.stratagem_completion_value = str((self.mode_amount-1) * 20)
                                                        self.time_bonus_value = str(int(self.time_countdown/10))
                                                        if self.perfection_track is True:
                                                            self.perfect_multi_value = "2.0x"
                                                            self.perfect_multi_colour = self.colour
                                                            pmv = 2
                                                        elif self.perfection_track is False:
                                                            self.perfect_multi_value = "1.0x"
                                                            self.perfect_multi_colour = self.red_colour
                                                            pmv = 1
                                                        else:
                                                            self.perfect_multi_value = "1.0x"
                                                        self.round_multi_value = str(1 + ((self.round-2)/10)) + "x"
                                                        rmv = 1 + ((self.round-2)/10)
                                                        self.total_score_value = int((int(self.stratagem_completion_value) + int(self.time_countdown/10))*pmv*rmv)
                                                        self.score += self.total_score_value - int(self.stratagem_completion_value)
                                                        self.score_value = str(int(self.score))
                                                        break


                                    else: # if the input is not the correct one 
                                        self.code_completion = -1 # resets progress
                                        self.perfection_track = False
            if self.end_game_start is True:
                self.end_game_start = False
                self.game_start_screen = True
                self.end_game = False
            if self.game_start_screen is True:
                self.starting_game()
                self.perfection_track = True
                self.game_starting_value = True
                self.countdown = 180
            elif self.points_scoring is True:
                self.score_count()
                self.key_allow = False
                self.game_starting_value = True
                self.time_countdown = self.time_countdown_start
            elif self.game_start_screen is False and self.game_starting_value is True or self.midgame_start is False and self.game_starting_value is True:
                self.key_allow = False
                self.perfection_track = True
                self.game_starting()
            elif self.end_game:
                self.end_screen()
            else:
                self.key_allow = True
                self.code_image_display_active(self.code_completion) # displays code image function
                self.timer_countdown()
                self.score_display_list = []
                self.end_display_list_width = []
                self.display_score_time = self.display_score_time_start
                self.midgame_start = False
                if self.time_countdown <= 0:
                    self.end_game = True
                    self.high_scores.append(self.score)
                    self.high_scores.sort(reverse=True)
                    self.high_scores.pop(3)
                    self.end_game_prevention = True
                            
            self.on_loop()
            self.on_render()
            pygame.display.flip() # updates display
            self.display.fill((display_bg)) # sets displays colour
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()