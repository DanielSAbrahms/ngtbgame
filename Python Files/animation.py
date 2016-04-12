import pygame
from pygame import *
import os


# @summary: returns images depending upon the position in game
# @param length: how many frames per animation loop
# @param runner: the outside int about where the game is in the animation
# @param folderName: the name of the folder where the animation images are located
# @param directory: The path to the folder
# @return image for the sprite to be set to
def animation(length,runner,folderName,directory):
    images_num = GetFolderSize(directory + folderName)  # How many images are in the folder
    frame_length = int(length/images_num) # How many frames each image is played for
    frameList = [] # The list of images for the animation
    for item in range(images_num):
        frameList.append(pygame.image.load(directory + folderName + "/" + str(item) + ".png"))
    image = frameList[int(runner/frame_length)]
    return image

# @param path: The path for the directory this animation is accessing photos from
# @return int: number of photos in the directory
def GetFolderSize(path):
    return len(os.listdir(path))
    
