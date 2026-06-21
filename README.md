# Duck Stratagem

The Helldivers 2 arcade game (Stratagem Hero) made with python using pygame

## Features

- Savefile: Uses a savefile system where the game saves high scores of past games to show your own personal best.
- Pygame: Uses Pygame to: display a window for the game, tracks keybaord input and display images and text.
- PyPi: Uses Pypi to easily access/play the game by installing the package using pypi.
- Compatibility: The game can run on MacOS, Windows and (hopefully) Linux.

## Images

<img alt="Title screen of the game" src="images/titlescreen.png" />

###

<img alt="Game screen when inputting code" src="images/midgame.png">

###

<img alt="Point scoring screen" src="images/pointscoring.png">

###

<img alt="Game over screen" src="images/gameover.png">

## How to Access

Requirements:

- MacOS or Linux device
- Python 3.9 or later (the latest to be safe)
- Pip 22 or later (the latest to be safe)
- Pygame 2.6.0 or later (should be installed when installing the package from Pypi)

1. You'll need to have Python and pip installed. 
    - You can follow [this](https://www.python.org/downloads/) to install Python
    - You can follow [this](https://pypi.org/project/pip/) to install pip

2. In Terminal or Command Prompt, enter the command:

    ```sh
    pip install duck-stratagem
    ```

    This will install the game. This is from the Pypi package [duck-stratagem](https://pypi.org/project/duck-stratagem/)

3. Once installed, you can use the commands:

    - `ds`
    - `duck-stratagem`
    - `play-ds`
    - `play-duck-stratagem`
    (Capatalisation doesn't matter)

4. Enjoy and good luck

## How to Play

1. When running the command to play the game, it will bring you to the title screen, instructing the user to press any stratagem key (wasd and arrow keys)(keys to input the code of the stratagem).

2. Once pressed, the game will give you a countdown then will display the the top 5 images of the stratagems in the list, outlining the current stratagem, and the code of it to input with the stratagem keys. For every completed stratagem, you will get 20 points

3. When completing the list, you will gain points based on the time lasted (frames left/10, max 90), multiplied by 2 (+0.5 per 5 rounds) if they didnt make a mistake, multipled by the amount of rounds completed (1.0 + 0.1 x (ammount of round completed)). So, when completing round 10, the score will be calculated as:
((ammount of stratagems completed x 20) + (time left)) x perfection x round multiplier.

4. After scoring, you'll move on to the next round when pressing any stratagem key, repeating the game.

5. You lose when you don't complete the codes of all the stratagems in the list in the given time. This will prompt you with the game over screen and save your score to the high score list.

## Notes

This is my first time using pygame, so the structure of the code will absolutely be wack.
There also might be some miscalculations with the score where any feedback is appreciated.
I also forgot to add sound effect so If I need to fix anything with this game, I'll probarly add it
