from __future__ import print_function
import pygame, sys,math,os
from pygame.locals import *



class playerSprite(pygame.sprite.Sprite):

    def __init__(self):
 
    # Call the parent class (Sprite) constructor
        super(playerSprite, self).__init__()
 
    # Load the image
        os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/PlayerImages")
        self.image = pygame.image.load("PlayerImageFrontStanding.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.label = ("Player")
        
 
    # Set our transparent color
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
