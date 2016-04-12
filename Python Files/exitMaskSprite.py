from __future__ import print_function
import pygame, sys, math, os
from pygame.locals import *


class exitMaskSprite(pygame.sprite.Sprite):
    def __init__(self, board, direction):
        # Call the parent class (Sprite) constructor
        super(exitMaskSprite, self).__init__()

        # Load the images
        os.chdir(os.path.expanduser('~') + "/Google Drive/PyGame Games/NGTB Game/Boards/Board" + str(board))
        self.image = pygame.image.load((direction.capitalize()) + "Exit" + ".png")
        self.image = pygame.transform.scale(self.image,(800,600))
        self.mask = pygame.mask.from_surface(self.image)
        self.label = "This Mask is " + direction
        self.playerSpawnPosition = (0, 0)

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        # Set our transparent color
        self.rect = self.image.get_rect()

    def setSpawnPos(self, set_x, set_y):
        self.playerSpawnPosition = (set_x, set_y)
