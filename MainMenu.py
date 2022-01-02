import pygame
import pygame_menu
import ExerciseTwo as E1
import ExerciseThree as E2
import ExerciseFour as E3
import ExerciseFFive as E4
import ExerciseSix as E5
import ExerciseSeven as E6

pygame.init()
# Constants and global variables
WIDTH, HEIGHT = 1260, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#setLv_dificulty
easyCount = 6
hardCount = 12

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
    pass

def set_Module(module, value):

    if set_Module == 'Module1' and set_difficulty == 1:
        easyCount
    elif set_Module == 'Module1' and set_difficulty == 2:
        hardCount
    elif set_Module == 'Module2' and set_difficulty == 1:
        easyCount
    else:
        hardCount
    pass


def start_the_game():

    if set_Module == 'Module1':
    #then run exercise 1,2,3
        E1()
        '''E2()
        E3()'''
    elif set_Module == 'Module2':
    #then run exercise 1,2,3,4,5,6
        '''E1()
        E2()
        '''
        E3()
        #E4()
        #E5()
        #E6()
    pass

# Create menus: Main menu
mytheme = pygame_menu.themes.THEME_BLUE.copy()
myimage = pygame_menu.baseimage.BaseImage(
    image_path=backgroundImg)
mytheme.background_color = myimage


menu = pygame_menu.Menu('Backpain', 1260, 960, theme=mytheme)
menu.add.text_input('Name :', default='Player')
menu.add.selector('Difficulty :', [('Easy', 1, easyCount), ('Hard', 2, hardCount)], onchange=set_difficulty)

menu.add.selector("Module:", [('Module1', 1), ('Module2', 2)], onchange=set_Module)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)