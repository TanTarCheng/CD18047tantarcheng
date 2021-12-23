import pygame
import pygame_menu
import AssistedCervicalSpineRetraction as ACSR1
import Exercise3 as E3

pygame.init()
# Constants and global variables
WIDTH, HEIGHT = 1260, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#setLv_dificulty
easyCount = 10
hardCount = 15

# Load image
backgroundImg = 'ExercisePic/upper-back-pain.png'

#Event handeling
def set_Module(module, value):
    '''
    for event in pygame.event.get(): \== easy
        if (event.type == pygame.QUIT):
            running == False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_a):
                print("you pressed the a key")
    for event in pygame.event.get(): \ == hard
        if (event.type == pygame.QUIT):
            running == False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_a):
                print("you pressed the a key")
    '''
    pass

def set_difficulty(value, difficulty, totalCount):
    ACSR1.set_totalCount(totalCount)
    ''' 
    E2.set_totalCount(totalCount)
    E3.set_totalCount(totalCount)
    E4.set_totalCount(totalCount)
    E5.set_totalCount(totalCount)
    E5.set_totalCount(totalCount)
    E6.set_totalCount(totalCount)
    E7.set_totalCount(totalCount)
    '''
    pass

def start_the_game():
    # Do the job here !
    '''run set moudle'''

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