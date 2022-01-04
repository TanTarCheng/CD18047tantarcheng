import pygame
import pygame_menu
import ExerciseOne as E1
import ExerciseTwo as E2
import ExerciseThree as E3
import ExerciseFour as E4
import ExerciseFive as E5
import ExerciseSix as E6

pygame.init()
# Constants and global variables
WIDTH, HEIGHT = 1260, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#setLv_dificulty
easyCount = 6
hardCount = 11

moduleSet = 1

# Load image
backgroundImg = 'ExercisePic/upper-back-pain.png'

#Event handeling

def set_difficulty(value, difficulty, totalCount):
    E1.set_totalCount(totalCount)
    E2.set_totalCount(totalCount)
    E3.set_totalCount(totalCount)
    E4.set_totalCount(totalCount)
    E5.set_totalCount(totalCount)
    E6.set_totalCount(totalCount)

def set_Module(module, value):
    global  moduleSet
    moduleSet = value



def start_the_game():

    if moduleSet == 1:
        E1.runExercise()

    elif moduleSet == 2:
        E1.runExercise()


# Create menus: Main menu
mytheme = pygame_menu.themes.THEME_BLUE.copy()
myimage = pygame_menu.baseimage.BaseImage(
    image_path=backgroundImg)
mytheme.background_color = myimage


menu = pygame_menu.Menu('Backpain', 1260, 960, theme=mytheme)

menu.add.selector('Difficulty :', [('Easy', 1, easyCount), ('Hard', 2, hardCount)], onchange=set_difficulty)

menu.add.selector("Module:", [('Module1', 1), ('Module2', 2)], onchange=set_Module)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)