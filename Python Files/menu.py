# This is a BETA menu screen for launching the game
# Feel free to edit this if you think it will make it work better
# Be sure to make a copy first though

import pygame
from pygame import *
import sys, math, os

global fullscreen
global sound

def options_menu():
    global sound
    global fullscreen


pygame.init()

#<editor-fold desc = "Instance Data">
FPS = 60  # The Frames per second
fpsClock = pygame.time.Clock()
#</editor-fold>

os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/MenuSources")

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("NGTB Game")
os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame")
pygame.display.set_icon(pygame.image.load("logo.png"))
os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/MenuSources")
WHITE = (255, 255, 255)

logo = pygame.image.load("logo.png")

playGame = pygame.image.load("playGame.png")

options = pygame.image.load("options.png")

quit = pygame.image.load("quit.png")

selectionArrows = pygame.image.load("selectionArrows.png")
selection = 0
selected = False
fullscreen = False
sound = False

optionsList = [playGame, options, quit]

while True:

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(logo,(158,100))

    for x in range(len(optionsList)):
        DISPLAYSURF.blit(optionsList[x], (300, 270 + (x * 75)))
        if x == selection:
            DISPLAYSURF.blit(selectionArrows, (190, 253 + (x * 75)))

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
        #TODO Options menu should be created
        options_menu()
    elif selected and selection == 2:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
