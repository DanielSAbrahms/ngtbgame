# This is a BETA menu screen for launching the game
#
# Feel free to edit this if you think it will make it work better
# Be sure to make a copy first though

import pygame
from pygame import *
import sys, math, os

global fullscreen # The Variable toggles the fullscreen window
global sound # The Variable toggles the sound ( Music and Effects)

# @pre The existing state of the fullscreen and sound variables
# @post The new state of the fullscreen and sound variables
def options_menu():
    global sound
    global fullscreen

pygame.init()

# <editor-fold desc = "Instance Data">
FPS = 60  # The Frames per second
fpsClock = pygame.time.Clock()
# </editor-fold>

os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/MenuSources")

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("NGTB Game")
os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame")
pygame.display.set_icon(pygame.image.load("logo.png"))
os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/MenuSources")
WHITE = (255, 255, 255)

logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo, (800, 600))

background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (1200, 900))

playGame = pygame.image.load("playGame.png")

options = pygame.image.load("options.png")

quit = pygame.image.load("quit.png")

selectionArrows = pygame.image.load("selectionArrows.png")
selection = 0
selected = False
fullscreen = False
sound = False
background_x = 0
background_y = 0
moving_left_x = True
moving_left_y = True

optionsList = [playGame, options, quit]

while True:
    if moving_left_x:
        background_x -= 0.5
    else:
        background_x += 0.5
    if moving_left_y:
        background_y -= 0.5
    else:
        background_y += 0.5

    if background_x <= -200:
        moving_left_x = False
    elif background_x >= 0:
        moving_left_x = True

    if background_y <= -150:
        moving_left_y = False
    elif background_y >= 0:
        moving_left_y = True

    DISPLAYSURF.fill(WHITE)

    DISPLAYSURF.blit(background, (background_x, background_y))

    DISPLAYSURF.blit(logo, (0, 0))

    for x in range(len(optionsList)):
        DISPLAYSURF.blit(optionsList[x], (300, 300 + (x * 75)))
        if x == selection:
            DISPLAYSURF.blit(selectionArrows, (190, 280 + (x * 76)))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                if selection == 0:
                    selection = 0
                else:
                    selection -= 1
            if event.key == K_DOWN:
                if selection == len(optionsList) - 1:
                    selection = len(optionsList) - 1
                else:
                    selection += 1
            if event.key == K_RETURN:
                selected = True
        # Quit Command
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if selected and selection == 0:
        os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/Python Files")
        execfile("main.py", {fullscreen: "global", sound: "global"})
    elif selected and selection == 1:
        # TODO Options menu should be created
        options_menu()
    elif selected and selection == 2:
        pygame.quit()
        sys.exit()

    # <editor-fold desc="Debug Info">
    font = pygame.font.Font(None, 15)
    text = font.render(str(fpsClock)[11:13], 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.topleft = DISPLAYSURF.get_rect().topleft
    # </editor-fold>

    pygame.display.update()
    fpsClock.tick(FPS)
