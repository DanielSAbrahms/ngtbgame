# This is a BETA menu screen for launching the game
# Feel free to edit this if you think it will make it work better
# Be sure to make a copy first though

import pygame
from pygame import *
import sys, math, os

pygame.init()

#<editor-fold desc = "Instance Data">
FPS = 60  # The Frames per second
fpsClock = pygame.time.Clock()
#</editor-fold>

os.chdir(os.path.expanduser('~') + "/Google Drive/PyGame Games/NGTB Game/MenuSources")

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("NGTB Game")
os.chdir(os.path.expanduser('~') + "/Google Drive/PyGame Games/NGTB Game")
pygame.display.set_icon(pygame.image.load("logo.png"))
os.chdir(os.path.expanduser('~') + "/Google Drive/PyGame Games/NGTB Game/MenuSources")
WHITE = (255, 255, 255)

logo = pygame.image.load("logo.png")

playGame = pygame.image.load("playGame.png")

options = pygame.image.load("options.png")

quit = pygame.image.load("quit.png")

selectionArrows = pygame.image.load("selectionArrows.png")
selection = 0
selected = False
fullscreen = False

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
        os.chdir(os.path.expanduser('~') + "/Google Drive/PyGame Games/NGTB Game/Python Files")
        execfile("v1.6.2.py", {fullscreen: "global"})
    elif selected and selection == 1:
        #TODO Options menu should be created
        options()

    pygame.display.update()
    fpsClock.tick(FPS)