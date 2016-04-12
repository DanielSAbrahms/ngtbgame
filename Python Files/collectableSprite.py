from __future__ import print_function
import pygame, sys, math, os, random
from pygame.locals import *


class collectableSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(collectableSprite, self).__init__()
        os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/ObjectImages")
        self.label = "Collectable"
        image = pygame.image.load("Box.png")
        image = pygame.transform.scale(image, (100, 100))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.board = 1
        self.mask = pygame.mask.from_surface(self.image)

    def setX(self, x):
        self.rect.x = x

    def setY(self, y):
        self.rect.y = y

    def setBoard(self, b):
        self.board = b

    def setCoor(self):
        x = int(random.randint(0, 750))
        y = int(random.randint(0, 550))
        b = int(random.randint(1,2))
        self.setX(x)
        self.setY(y)
        self.setBoard(b)
