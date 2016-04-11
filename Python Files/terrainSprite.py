from __future__ import print_function
import pygame, sys,math,os
from pygame.locals import *

class terrainSprite(pygame.sprite.Sprite):

    def __init__(self,board):
 
    # Call the parent class (Sprite) constructor
        super(terrainSprite, self).__init__()
 
    # Load the image
    
        if board > 0:
            os.chdir(os.path.expanduser('~') + "/Google Drive/PyGame Games/NGTB Game/Boards/Board" + str(board))
            self.image = pygame.image.load(str("board" + str(board) + "Mask.png"))
        else:
            os.chdir(os.path.expanduser('~') + "/Google Drive/PyGame Games/NGTB Game")
            self.image = pygame.image.load(str("playerBounds.png"))
        self.image = pygame.transform.scale(self.image,(800,600))
        self.mask = pygame.mask.from_surface(self.image)
        self.label = "TerrrainSprite"
        
        
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
 
    # Set our transparent color
        self.rect = self.image.get_rect()
