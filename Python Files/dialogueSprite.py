from __future__ import print_function
import pygame, sys, math, os
from pygame.locals import *


class dialogueSprite(pygame.sprite.Sprite):
    def __init__(self, text, character):
        super(dialogueSprite, self).__init__()
        os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/CharacterCloseUps/")
        self.image = pygame.image.load(character + ".png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 225
        self.font = pygame.font.Font(None, 32)
        self.dialogue = self.font.render(text, 1, (10, 10, 10))
