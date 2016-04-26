from __future__ import print_function
import pygame, sys, math, os
from pygame.locals import *


class playerSprite(pygame.sprite.Sprite):
    def __init__(self, expandUpDown):
        # Call the parent class (Sprite) constructor
        super(playerSprite, self).__init__()

        # Load the image
        os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/PlayerImages")
        self.image = pygame.image.load("PlayerImageFrontStanding.png")
        self.image = pygame.transform.scale(self.image, expandUpDown)
        mask_image = pygame.image.load("PlayerImageMask.png")
        mask_image = pygame.transform.scale(mask_image, expandUpDown)
        self.mask = pygame.mask.from_surface(mask_image)
        self.label = ("Player")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
