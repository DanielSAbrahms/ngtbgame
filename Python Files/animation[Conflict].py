import pygame
from pygame import *
import os


def animation(length,runner,folderName,directory):
    frames = GetFolderSize(directory + folderName)
    frame_length = int(length/frames)
    frameList = []
    for item in range(frames):
        frameList.append(pygame.image.load(directory + folderName + "/" + str(item) + ".png"))
    image = frameList[int(runner/frame_length)]
    return image

def GetFolderSize(path):
    return len(os.listdir(path))-1
    
