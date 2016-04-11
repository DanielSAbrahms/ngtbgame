#NGTB Game v1.1
#Code by Daniel Abrahms


from __future__ import print_function
import pygame, sys,math
from pygame.locals import *


def object_collision(player, mask):
    global player_x
    global player_y
    if pygame.sprite.collide_mask(player,mask):
        player_x = pygame.sprite.collide_mask(player,mask)[0]
        player_y = pygame.sprite.collide_mask(player,mask)[1]



def object_float(object_y,original_pos):
    global object1_counter
    
    object1_counter+=1
    if object1_counter > 120:
        object1_counter = 0
        object_y = original_pos
    if object1_counter <= 30:
        return object_y + 0.5  
    elif object1_counter <= 60:
        return object_y + 0.25
    elif object1_counter <= 90:
        return object_y - 0.5
    elif object1_counter <= 120:
        return object_y - 0.25




def player_bounds():
    global player_x
    global player_y
    if player_x > 720:
        player_x = 720
        return True
    if player_y > 520:
        player_y = 520
        return True
    if player_x < -20:
        player_x = -20
        return True
    if player_y < -20:
        player_y = -20
        return True


global player_x
global player_y
global object1_counter

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption("NGTB Game")

walk_cycle_speed = 15 #Lower is Faster
move_speed = 6
direction = "down"
player_x = 500
player_y = 300


fullscreen = False

player_front_standing = pygame.image.load('PlayerImageFrontStanding.png')
player_front_standing = pygame.transform.scale(player_front_standing,(90,100))
player_front_walking1 = pygame.image.load("PlayerImageFrontWalkingLeft.png")
player_front_walking1 = pygame.transform.scale(player_front_walking1,(90,100))
player_front_walking2 = pygame.image.load("PlayerImageFrontWalkingRight.png")
player_front_walking2 = pygame.transform.scale(player_front_walking2,(90,100))

player_back_standing = pygame.image.load('PlayerImageBackStanding.png')
player_back_standing = pygame.transform.scsale(player_back_standing,(90,100))
player_back_walking1 = pygame.image.load("PlayerImageBackWalkingLeft.png")
player_back_walking1 = pygame.transform.scale(player_back_walking1,(90,100))
player_back_walking2 = pygame.image.load("PlayerImageBackWalkingRight.png")
player_back_walking2 = pygame.transform.scale(player_back_walking2,(90,100))

player_left_standing = pygame.image.load('PlayerImageLeftStanding.png')
player_left_standing = pygame.transform.scale(player_left_standing,(100,100))
player_left_walking1 = pygame.image.load("PlayerImageLeftWalkingLeft.png")
player_left_walking1 = pygame.transform.scale(player_left_walking1,(100,100))
player_left_walking2 = pygame.image.load("PlayerImageLeftWalkingRight.png")
player_left_walking2 = pygame.transform.scale(player_left_walking2,(100,100))

player_right_standing = pygame.image.load('PlayerImageRightStanding.png')
player_right_standing = pygame.transform.scale(player_right_standing,(100,100))
player_right_walking1 = pygame.image.load("PlayerImageRightWalkingLeft.png")
player_right_walking1 = pygame.transform.scale(player_right_walking1,(100,100))
player_right_walking2 = pygame.image.load("PlayerImageRightWalkingRight.png")
player_right_walking2 = pygame.transform.scale(player_right_walking2,(100,100))

background = pygame.image.load('GrassBG.png').convert()
background = pygame.transform.scale(background,(800,600))

mask = pygamepygame.image.load('rivermask.png')
mask = pygame.transform.scale(background,(800,600))

object1 = pygame.image.load("VRHeadset.png")
object1 = pygame.transform.scale(object1,(100,100))

is_walking = False

object1_x = 320
object1_y = 200
object1_counter = 0
counter = 0



player = player_front_standing

keys = [False, False, False, False]

while True:

    object1_y = object_float(object1_y,200)
    
    if player_bounds():
        is_walking = False

    if is_walking == False or counter > walk_cycle_speed:
        counter = 0


    if direction == "up":
        player = player_back_standing
    elif direction == "down":
        player = player_front_standing
    elif direction == "right":
        player = player_right_standing
    elif direction == "left":
        player = player_left_standing




    if is_walking:
        if direction == "up":
            if counter <= int(walk_cycle_speed/2):
                player = player_back_walking1
            elif counter <= walk_cycle_speed:
                player = player_back_walking2
            counter+=1
        elif direction == "down":
            if counter <= int(walk_cycle_speed/2):
                player = player_front_walking1
            elif counter <= walk_cycle_speed:
                player = player_front_walking2
            counter+=1
        elif direction == "left":
            if counter <= int(walk_cycle_speed/2):
                player = player_left_walking1
            elif counter <= walk_cycle_speed:
                player = player_left_standing
            counter+=1
        elif direction == "right":
            if counter <= int(walk_cycle_speed/2):
                player = player_right_walking1
            elif counter <= walk_cycle_speed:
                player = player_right_standing
            counter+=1
            
    #object_collision(player, mask)
            
    DISPLAYSURF.blit(background,(0,0))
   
    DISPLAYSURF.blit(player,(player_x,player_y))
    DISPLAYSURF.blit(object1,(object1_x,object1_y))
    

    

    if keys[0]:
        direction = "left"
        player_x -= move_speed
        is_walking = True
    elif keys[1]:
        direction = "right"
        player_x += move_speed
        is_walking = True
    elif keys[3]:
        direction = "down"
        player_y += move_speed
        is_walking = True
    elif keys[2]:
        direction = "up"
        player_y -= move_speed
        is_walking = True
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                keys[1] = True
            if event.key == K_LEFT:
                keys[0] = True
            if event.key == K_UP:
                keys[2] = True
            if event.key == K_DOWN:
                keys[3] = True
            if event.key == K_v and fullscreen == False: 
                pygame.display.set_mode((800,600),pygame.FULLSCREEN)
                fullscreen = True
            elif event.key == K_v:
                pygame.display.set_mode((800,600),pygame.RESIZABLE)
                fullscreen = False

        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                keys[1] = False
                is_walking = False
            if event.key == K_LEFT:
                keys[0] = False
                is_walking = False
            if event.key == K_UP:
                keys[2] = False
                is_walking = False
            if event.key == K_DOWN:
                keys[3] = False
                is_walking = False
                
                
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    font = pygame.font.Font(None, 20)
    text = font.render(str(fpsClock), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = DISPLAYSURF.get_rect().centerx
    DISPLAYSURF.blit(text, textpos)

    pygame.display.update()
    fpsClock.tick(FPS)

