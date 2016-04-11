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

    def __init__(self):
 
    # Call the parent class (Sprite) constructor
        super(terrainSprite, self).__init__()
 
    # Load the image
        self.image = pygame.image.load("riverMask.png")
        self.image = pygame.transform.scale(self.image,(800,600))
        terrainSprite.mask = pygame.mask.from_surface(self.image)
 
    # Set our transparent color
        self.rect = self.image.get_rect()


 


pygame.init()

spriteGroup = pygame.sprite.Group()


FPS = 60
fpsClock = pygame.time.Clock()
move_speed = 5
animation_delay_time = 4 #In seconds

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

background = pygame.image.load('GrassBG.png').convert()
background = pygame.transform.scale(background,(800,600))

bigbackground = pygame.image.load('bigmap.png')
bigbackground = pygame.transform.scale(bigbackground,(2000,1500))

object1 = pygame.image.load("VRHeadset.png")
object1 = pygame.transform.scale(object1,(100,100))

is_walking = False

object1_x = 320
object1_y = 200
object1_walking_counter = 0
walking_counter = 0

player = playerSprite()
player.rect.x = 200
player.rect.y = 200
player.mask = pygame.mask.from_surface(pygame.image.load("PlayerImageMask.png"))
spriteGroup.add(player)

pondMask = terrainSprite()
pondMask.rect.x = 0
pondMask.rect.y = 0
background_x = 0
background_y = 0

old_player_coor = (player.rect.x,player.rect.y)



keys= [False,False,False,False]
direction = 'up'
walk_cycle_speed = 20 #Lower is Faster
walking_counter = 0
animation_counter = 0
fullscreen = False
count = 0
animation_delay = 0

while True:
    animation_delay += 1
    if pygame.sprite.collide_mask(player,pondMask):
        player.rect.x = old_player_coor[0]
        player.rect.y = old_player_coor[1]
        is_walking = False
    else:
        old_player_coor = (player.rect.x,player.rect.y)

            

    if player.rect.x > 720:
        player.rect.x = 720
        is_walking = False
    if player.rect.y > 520:
        player.rect.y = 520
        is_walking = False
    if player.rect.x < -20:
        player.rect.x = -20
        is_walking = False
    if player.rect.y < -20:
        player.rect.y = -20
        is_walking = False
        
    if is_walking == False or walking_counter > walk_cycle_speed:
        walking_counter = 0
    
    if direction == "up":
        player.image = player_back_standing
    elif direction == "down":
        player.image = player_front_standing
    elif direction == "right":
        player.image = player_right_standing
    elif direction == "left":
        player.image = player_left_standing




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

    if is_walking == False and animation_delay > 60*animation_delay_time:
        if direction == "down":
            if animation_counter > 59:
                animation_counter = 0
            image = animation(60,10,animation_counter,"DownIdleAnimation_CoinFlip")
            image = pygame.transform.scale(image,(90,100))
            player.image = image
            animation_counter+=1
        if direction == "left":
            if animation_counter > 29:
                animation_counter = 0
            image = animation(30,3,animation_counter,"LeftIdleAnimation_Dance")
            image = pygame.transform.scale(image,(100,100))
            player.image = image
            animation_counter+=1
        if direction == "right":
            if animation_counter > 119:
                animation_counter = 0
            image = animation(120,2,animation_counter,"RightIdleAnimation_PhoneLook")
            image = pygame.transform.scale(image,(100,100))
            player.image = image
            animation_counter+=1
    elif is_walking == True:
        animation_delay = 0

    
        
    DISPLAYSURF.fill((255,255,255))
    DISPLAYSURF.blit(background,(background_x,background_y))
    spriteGroup.draw(DISPLAYSURF)
    

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

    font = pygame.font.Font(None, 20)
    text = font.render(str(fpsClock), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = DISPLAYSURF.get_rect().centerx
    

    pygame.display.update()
    fpsClock.tick(FPS)
