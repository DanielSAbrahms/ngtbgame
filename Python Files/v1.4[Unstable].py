from __future__ import print_function
import pygame, sys,math
from pygame.locals import *
from animation import *


class playerSprite(pygame.sprite.Sprite):

    def __init__(self):
 
    # Call the parent class (Sprite) constructor
        super(playerSprite, self).__init__()
 
    # Load the image
        self.image = pygame.image.load("PlayerImageFrontStanding.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        
 
    # Set our transparent color
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class terrainSprite(pygame.sprite.Sprite):

    def __init__(self,board):
 
    # Call the parent class (Sprite) constructor
        super(terrainSprite, self).__init__()
 
    # Load the image
        if board > 0:
            self.image = pygame.image.load(str("board" + str(board) + "Mask.png"))
        else:
            self.image = pygame.image.load(str("playerBounds.png"))
        self.image = pygame.transform.scale(self.image,(800,600))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
 
    # Set our transparent color
        self.rect = self.image.get_rect()

    
    
 


pygame.init()

spriteGroup = pygame.sprite.Group()


FPS = 60
fpsClock = pygame.time.Clock()
move_speed = 7
animation_delay_time = 4 #In seconds
keys= [False,False,False,False]
direction = 'up'
walk_cycle_speed = 10 #Lower is Faster
walking_counter = 0
animation_counter = 0
fullscreen = False
is_walking = False
count = 0
animation_delay = 0
currentBoard = 1

DISPLAYSURF = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption("NGTB Game")

player_front_standing = pygame.image.load('PlayerImageFrontStanding.png')
player_front_standing = pygame.transform.scale(player_front_standing,(90,100))
player_front_walking1 = pygame.image.load("PlayerImageFrontWalkingLeft.png")
player_front_walking1 = pygame.transform.scale(player_front_walking1,(90,100))
player_front_walking2 = pygame.image.load("PlayerImageFrontWalkingRight.png")
player_front_walking2 = pygame.transform.scale(player_front_walking2,(90,100))

player_back_standing = pygame.image.load('PlayerImageBackStanding.png')
player_back_standing = pygame.transform.scale(player_back_standing,(90,110))
player_back_walking1 = pygame.image.load("PlayerImageBackWalkingLeft.png")
player_back_walking1 = pygame.transform.scale(player_back_walking1,(90,110))
player_back_walking2 = pygame.image.load("PlayerImageBackWalkingRight.png")
player_back_walking2 = pygame.transform.scale(player_back_walking2,(90,110))

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


background = pygame.image.load('board' + str(currentBoard) + '.png').convert()
background = pygame.transform.scale(background,(800,600))

object1 = pygame.image.load("VRHeadset.png")
object1 = pygame.transform.scale(object1,(100,100))


object1_x = 320
object1_y = 200
object1_walking_counter = 0
walking_counter = 0

player = playerSprite()
player.rect.x = 200
player.rect.y = 200
player.mask = pygame.mask.from_surface(pygame.image.load("PlayerImageMask.png"))
spriteGroup.add(player)

mapMask = terrainSprite(currentBoard)
playerBounds = terrainSprite(0)
background_x = 0
background_y = 0

old_player_coor = (player.rect.x,player.rect.y)





while True:
    animation_delay += 1
    
    #Debug Info---------------------------------------------------------------------------------------------------------
    font = pygame.font.Font(None, 15)
    text = font.render(str(fpsClock), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = DISPLAYSURF.get_rect().centerx

    #Check Collision with Masks---------------------------------------------------------------------------------------------------------
    if pygame.sprite.collide_mask(player,mapMask) or pygame.sprite.collide_mask(player,playerBounds):
        player.rect.x = old_player_coor[0]
        player.rect.y = old_player_coor[1]
        is_walking = False
    else:
        old_player_coor = (player.rect.x,player.rect.y)
        
    #Reset Walking Counter---------------------------------------------------------------------------------------------------------   
    if is_walking == False or walking_counter > walk_cycle_speed:
        walking_counter = 0

    #Changes player Sprite according to Direction----------------------------------------------------------------------------------
    if direction == "up":
        player.image = player_back_standing
    elif direction == "down":
        player.image = player_front_standing
    elif direction == "right":
        player.image = player_right_standing
    elif direction == "left":
        player.image = player_left_standing

    #Changes Player Sprite according to Walking Cycle Position--------------------------------------------------------------------------------
    if is_walking:
        if direction == "up":
            if walking_counter <= int(walk_cycle_speed/2):
                player.image = player_back_walking1
            elif walking_counter <= walk_cycle_speed:
                player.image = player_back_walking2
            walking_counter+=1
        elif direction == "down":
            if walking_counter <= int(walk_cycle_speed/2):
                player.image = player_front_walking1
            elif walking_counter <= walk_cycle_speed:
                player.image = player_front_walking2
            walking_counter+=1
        elif direction == "left":
            if walking_counter <= int(walk_cycle_speed/2):
                player.image = player_left_walking1
            elif walking_counter <= walk_cycle_speed:
                player.image = player_left_standing
            walking_counter+=1
        elif direction == "right":
            if walking_counter <= int(walk_cycle_speed/2):
                player.image = player_right_walking1
            elif walking_counter <= walk_cycle_speed:
                player.image = player_right_standing
            walking_counter+=1

    #Animation Player---------------------------------------------------------------------------------------------------------
    if is_walking == False and animation_delay > 60*animation_delay_time:
        if direction == "down": #Idle animation for player facing down ------------------------------
            if animation_counter > 59:
                animation_counter = 0
            image = animation(60,10,animation_counter,"DownIdleAnimation_CoinFlip")
            image = pygame.transform.scale(image,(90,100))
            player.image = image
            animation_counter+=1
        if direction == "left": #Idle animation for player facing left ------------------------------
            if animation_counter > 29:
                animation_counter = 0
            image = animation(30,3,animation_counter,"LeftIdleAnimation_Dance")
            image = pygame.transform.scale(image,(100,100))
            player.image = image
            animation_counter+=1
        if direction == "right": #Idle animation for player facing right ------------------------------
            if animation_counter > 119:
                animation_counter = 0
            image = animation(120,2,animation_counter,"RightIdleAnimation_PhoneLook")
            image = pygame.transform.scale(image,(100,100))
            player.image = image
            animation_counter+=1
    elif is_walking == True: # Reset Delay Counter
        animation_delay = 0

        
    DISPLAYSURF.fill((255,255,255))
    DISPLAYSURF.blit(background,(background_x,background_y))
    spriteGroup.draw(DISPLAYSURF)
    DISPLAYSURF.blit(text, textpos)
    

    pygame.display.flip()
    if keys[0]:
        direction = "left"
        player.rect.x -= move_speed
        is_walking = True
    elif keys[1]:
        direction = "right"
        player.rect.x += move_speed
        is_walking = True
    elif keys[3]:
        direction = "down"
        player.rect.y += move_speed
        is_walking = True
    elif keys[2]:
        direction = "up"
        player.rect.y -= move_speed
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

    
    

    pygame.display.update()
    fpsClock.tick(FPS)
