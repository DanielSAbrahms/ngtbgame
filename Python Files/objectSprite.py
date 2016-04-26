from __future__ import print_function
import pygame, sys, math, os
from pygame.locals import *


def getBoardNum(line):
    return int(line[5:8])


def getObjectName(line):
    name = ""
    startChecking = False
    for char in line:
        if char == '(' and startChecking == False:
            startChecking = True
        elif char == ';':
            startChecking = False
        if startChecking:
            name += char
    return str(name[1:])


def getXCoor(line):
    num = ""
    startChecking = False
    for char in line:
        if char == ';' and startChecking == False:
            startChecking = True
        elif char == '.':
            startChecking = False
        if startChecking:
            num += char
    return int(num[1:])


def getYCoor(line):
    num = ""
    startChecking = False
    for char in line:
        if char == '.' and startChecking == False:
            startChecking = True
        elif char == '/':
            startChecking = False
        if startChecking:
            num += char
    return int(num[1:])


def getXSize(line):
    num = ""
    startChecking = False
    for char in line:
        if char == '/' and startChecking == False:
            startChecking = True
        elif char == '>':
            startChecking = False
        if startChecking:
            num += char
    return int(num[1:])


def getYSize(line):
    num = ""
    startChecking = False
    for char in line:
        if char == ">" and startChecking == False:
            startChecking = True
        elif char == ')':
            startChecking = False
        if startChecking:
            num += char
    return int(num[1:])


class objectSprite(pygame.sprite.Sprite):
    def __init__(self, line):
        super(objectSprite, self).__init__()

        os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/ObjectImages")
        self.name = getObjectName(line)
        self.board = getBoardNum(line)
        self.label = self.name
        self.xSize = getXSize(line)
        self.ySize = getYSize(line)
        image = pygame.image.load(self.name + ".png")
        image = pygame.transform.scale(image, (self.xSize, self.ySize))
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = getXCoor(line)
        self.rect.y = getYCoor(line)
