from __future__ import print_function
import pygame, sys, math, os
from pygame.locals import *


def getBoardNum(line):
    return int(line[5:8])


def getObjectName(line):
    colonCount = 0
    name = ""
    startChecking = False
    for char in line:
        if char == ":":
            colonCount += 1
        if char == '(' and startChecking == False:
            startChecking = True
        elif char == ':' and colonCount == 2:
            startChecking = False
        if startChecking:
            name += char
    return str(name[1:])


def getXCoor(line):
    colonCount = 0
    num = ""
    startChecking = False
    for char in line:
        if char == ":":
            colonCount += 1
        if char == ':' and startChecking == False and colonCount == 2:
            startChecking = True
        elif char == ':' and colonCount == 3:
            startChecking = False
        if startChecking:
            num += char
    return int(num[1:])


def getYCoor(line):
    colonCount = 0
    num = ""
    startChecking = False
    for char in line:
        if char == ":":
            colonCount += 1
        if char == ':' and colonCount == 3:
            startChecking = True
        elif char == ':' and colonCount == 4:
            startChecking = False
        if startChecking:
            num += char
    return int(num[1:])


def getXSize(line):
    colonCount = 0
    num = ""
    startChecking = False
    for char in line:
        if char == ":":
            colonCount += 1
        if char == ':' and colonCount == 4:
            startChecking = True
        elif char == ':' and colonCount == 5:
            startChecking = False
        if startChecking:
            num += char
    return int(num[1:])


def getYSize(line):
    colonCount = 0
    num = ""
    startChecking = False
    for char in line:
        if char == ":":
            colonCount += 1
        if char == ':' and colonCount == 5:
            startChecking = True
        elif char == ')':
            startChecking = False
        if startChecking:
            num += char
    return int(num[1:])


class objectSprite(pygame.sprite.Sprite):
    def __init__(self, line):
        for x in range(len(line)):
            if (line[x] == ","):
                line = line[:x]
                break
        super(objectSprite, self).__init__()

        os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/ObjectImages")
        self.name = getObjectName(line)
        self.hasMask = False
        self.board = getBoardNum(line)
        self.label = self.name
        self.xSize = getXSize(line)
        self.ySize = getYSize(line)
        image = pygame.image.load(self.name + ".png")
        try:  # If image has mask image in ObjectImages
            mask = pygame.image.load(self.name + "Mask.png")
            mask = pygame.transform.scale(mask, (self.xSize, self.ySize))
            self.mask = pygame.mask.from_surface(mask)
            self.hasMask = True
        except:
            print("Warning: No mask found for " + self.name + " object.")
            self.hasMask = False
        image = pygame.transform.scale(image, (self.xSize, self.ySize))

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = getXCoor(line)
        self.rect.y = getYCoor(line)
