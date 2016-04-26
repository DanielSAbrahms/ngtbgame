# Author: Daniel Abrahms
# Version: 1.6
# Before editing, PLEASE READ Game Documentation located in the Design Folder
# Goals for this version: Add the first actual game feature, involving a user fetching an object from random coordinates
# User must bring back object to start


from __future__ import print_function
from pygame import *
import os

os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/Python Files")
from animation import *
from exitMaskSprite import *
from objectSprite import *
from playerSprite import playerSprite
from terrainSprite import terrainSprite
from collectableSprite import *

# <editor-fold desc="Global Variables">
global mapMask
global background
global player
global currentBoard
global walk_cycle_speed
global leftExitMask
global rightExitMask
global upExitMask
global downExitMask
global spriteGroup
global objects
global default_layer


# </editor-fold>

# <editor-fold desc="Methods">


# @summary: clears group or list of all elements
# @param s_group: group or list name
# @post: Group or list will be completely empty
# @return: returns s_group after completely removing all objects
def clearGroup(s_group):
    for obj in iter(s_group):
        s_group.remove(obj)
    return s_group


# @summary: Switches board and runs the necessary commands
# @param int newboard : The desired board for map change.
# If player is in board1 and wants to be board2, newboard must be '2'
# @pre This code can't be run every iteration in loop for optimization reasons
# @pre global variables background and mapMask will be set for previous board
# @post global variables background and mapMask will be set for newboard board
# @post clears objects, default layer, and spriteGroup
# @post runs code that sets up a board
def switchBoard(newBoard):
    global background
    global mapMask
    global currentBoard
    global leftExitMask
    global rightExitMask
    global upExitMask
    global objects
    global spriteGroup
    global downExitMask
    global default_layer
    currentBoard = newBoard
    os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/Boards/Board" + str(newBoard))
    background = pygame.image.load("board" + str(newBoard) + ".png")
    background = pygame.transform.scale(background, (800, 600)).convert()
    mapMask = terrainSprite(newBoard)
    try:
        leftExitMask = exitMaskSprite(newBoard, "left")
    except:
        leftExitMask = None
    try:
        rightExitMask = exitMaskSprite(newBoard, "right")
    except:
        rightExitMask = None
    try:
        upExitMask = exitMaskSprite(newBoard, "up")
    except:
        upExitMask = None
    try:
        downExitMask = exitMaskSprite(newBoard, "down")
    except:
        downExitMask = None
    os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/Boards")
    objects = []
    spriteGroup.empty()
    default_layer = pygame.sprite.LayeredUpdates(player)
    objectListFile = open("BoardObjectList.txt", 'r')
    for line in objectListFile:
        if line[0] != '#' and len(line) > 15:
            objects.append(objectSprite(line))
    for obj in objects:
        if newBoard == obj.board:
            spriteGroup.add(obj)


# @summary: Changes Player Sprite Image according to Walking Cycle Position
# @param player_direction : the direction of the player either UP DOWN LEFT RIGHT
# @pre player sprite image will be what is was before the function was called
# @post player sprite image will be the next image
def walking_cycle(player_direction):
    global player
    global walk_cycle_speed
    global walking_counter
    directory = os.path.expanduser('~') + "/Desktop/ngtbgame/Animations/PlayerAnimations/"
    if player_direction == UP:
        if (walking_counter > walk_cycle_speed - 1) or walking_counter < 0:
            walking_counter = 0
        image = animation(walk_cycle_speed, walking_counter - 1, "UpWalkingAnimation", directory)
        image = pygame.transform.scale(image, expandUpDown)
        player.image = image
    elif player_direction == DOWN:
        if (walking_counter > walk_cycle_speed - 1) or walking_counter < 0:
            walking_counter = 0
        image = animation(walk_cycle_speed, walking_counter - 1, "DownWalkingAnimation", directory)
        image = pygame.transform.scale(image, expandUpDown)
        player.image = image
    elif player_direction == RIGHT:
        if (walking_counter > walk_cycle_speed - 1) or walking_counter < 0:
            walking_counter = 0
        image = animation(walk_cycle_speed, walking_counter - 1, "RightWalkingAnimation", directory)
        image = pygame.transform.scale(image, expandLeftRight)
        player.image = image
    elif player_direction == LEFT:
        if (walking_counter > walk_cycle_speed - 1) or walking_counter < 0:
            walking_counter = 0
        image = animation(walk_cycle_speed, walking_counter - 1, "LeftWalkingAnimation", directory)
        image = pygame.transform.scale(image, expandLeftRight)
        player.image = image


# @summary: Changes Player Sprite Image according to Running Cycle Position
# @param player_direction : the direction of the player either UP DOWN LEFT RIGHT
# @pre player sprite image will be what is was before the function was called
# @post player sprite image will be the next image
def running_cycle(player_direction):  # Changes Player Sprite according to Running Cycle Position-----
    global player
    global walk_cycle_speed
    global walking_counter
    directory = os.path.expanduser('~') + "/Desktop/ngtbgame/Animations/PlayerAnimations/"
    if player_direction == UP:
        if (walking_counter > walk_cycle_speed - 1) or walking_counter < 0:
            walking_counter = 0
        image = animation(walk_cycle_speed, walking_counter - 1, "UpWalkingAnimation", directory)
        image = pygame.transform.scale(image, expandUpDown)
        player.image = image
    elif player_direction == DOWN:
        if (walking_counter > walk_cycle_speed - 1) or walking_counter < 0:
            walking_counter = 0
        image = animation(walk_cycle_speed, walking_counter - 1, "DownWalkingAnimation", directory)
        image = pygame.transform.scale(image, expandUpDown)
        player.image = image
    elif player_direction == RIGHT:
        if (walking_counter > walk_cycle_speed - 1) or walking_counter < 0:
            walking_counter = 0
        image = animation(walk_cycle_speed, walking_counter - 1, "RightRunningAnimation", directory)
        image = pygame.transform.scale(image, expandLeftRight)
        player.image = image
    elif player_direction == LEFT:
        if (walking_counter > walk_cycle_speed - 1) or walking_counter < 0:
            walking_counter = 0
        image = animation(walk_cycle_speed, walking_counter - 1, 'LeftRunningAnimation', directory)
        image = pygame.transform.scale(image, expandLeftRight)
        player.image = image


# @summary: Changes Player Sprite Image according to direction
# @param player_direction:  the direction of the player either UP DOWN LEFT RIGHT
# @pre player sprite image will be previous
# @post player sprite image will be changed according to direction
def direction_calibration(player_direction):  # Changes player Sprite according to Direction------------
    global player
    if player_direction == UP:
        player.image = player_back_standing
    elif player_direction == DOWN:
        player.image = player_front_standing
    elif player_direction == RIGHT:
        player.image = player_right_standing
    elif player_direction == LEFT:
        player.image = player_left_standing


# </editor-fold>

pygame.init()

spriteGroup = pygame.sprite.Group()

# <editor-fold desc="Instance Data">
FPS = 60  # The Frames per second
fpsClock = pygame.time.Clock()
move_speed_px = 240  # Pixel/s: Player Speed while walking
move_speed = move_speed_px / 60  # Player Speed in a smaller increment for ease of use
walk_speed = move_speed
run_speed = int(move_speed * 1.5)
player_idle_animation_delay = 4  # In seconds: How long it takes for the animation to kick in for player idle
keys = [False, False, False, False]  # The key statuses for UP DOWN LEFT RIGHT
walk_cycle_speed = 40  # Lower is Faster: The speed of the walking and running animation
walking_counter = 0  # Where the player is in the walking cycle
animation_counter = 0  # Where the player is in the animation
fullscreen = False  # Toggle for full-screen window
is_walking = False  # The walking status of player
is_running = False  # The running status of player
has_item = False
game_loop_counter = 0  # The count of game loops
animation_delay = 0
currentBoard = 1
# The player directions made into string items
# in order to return Compiler error versus Logic error in case of typo
DOWN = 'down'
UP = 'up'
LEFT = 'left'
RIGHT = 'right'
# Stretches player image to fit realism
expandLeftRight = (125, 150)
expandUpDown = (125, 150)
playerBounds = terrainSprite(0)
# </editor-fold>

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("NGTB Game")

# <editor-fold desc="Sets Up Player Images">
os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/PlayerImages")
player_front_standing = pygame.image.load('PlayerImageFrontStanding.png')
player_front_standing = pygame.transform.scale(player_front_standing, expandUpDown)

player_back_standing = pygame.image.load('PlayerImageBackStanding.png')
player_back_standing = pygame.transform.scale(player_back_standing, expandUpDown)

player_left_standing = pygame.image.load('PlayerImageLeftStanding.png')
player_left_standing = pygame.transform.scale(player_left_standing, expandLeftRight)

player_right_standing = pygame.image.load('PlayerImageRightStanding.png')
player_right_standing = pygame.transform.scale(player_right_standing, expandLeftRight)
# </editor-fold>

os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/Boards/Board1")
background = pygame.image.load('board1.png').convert()
background = pygame.transform.scale(background, (800, 600))

# Utilizes objectSprite class in order to properly add objects
os.chdir(os.path.expanduser('~') + "/Desktop/ngtbgame/Boards")
objects = []
objectListFile = open("BoardObjectList.txt", 'r')

# <editor-fold desc="Sets up objects">
for line in objectListFile:
    if line[0] != '#' and len(line) > 15:
        objects.append(objectSprite(line))
for obj in objects:
    if currentBoard == obj.board:
        spriteGroup.add(obj)
# </editor-fold>

# <editor-fold desc="Sets up player">
player = playerSprite(expandUpDown)
direction = DOWN
player.rect.x = 200
player.rect.y = 200
default_layer = pygame.sprite.LayeredUpdates(player)
# </editor-fold>


# <editor-fold desc="Sets us Board Masks">
mapMask = terrainSprite(currentBoard)
try:
    leftExitMask = exitMaskSprite(currentBoard, "left")
except:
    leftExitMask = None
try:
    rightExitMask = exitMaskSprite(currentBoard, "right")
except:
    rightExitMask = None
try:
    upExitMask = exitMaskSprite(currentBoard, "up")
except:
    upExitMask = None
try:
    downExitMask = exitMaskSprite(currentBoard, "down")
except:
    downExitMask = None
# </editor-fold>

# These coordinates are updated to current position after rendering each frame
old_player_coor = (player.rect.x, player.rect.y)
while True:
    # <editor-fold desc="Instables">
    game_loop_counter += 1
    animation_delay += 1
    # </editor-fold>

    # <editor-fold desc="Changes movement speed with walking or running status">
    if (is_running):
        move_speed = 8
    else:
        move_speed = 4
    # </editor-fold>


    # <editor-fold desc="Checks collision with the exit masks">
    for mask in [rightExitMask, leftExitMask, upExitMask, downExitMask]:
        if leftExitMask is not None and pygame.sprite.collide_mask(player, leftExitMask):  # Board 1 -- Left Exit
            print("Leaving NGTB")
            spriteGroup = clearGroup(spriteGroup)
            switchBoard(2)
            objects = clearGroup(objects)
            currentBoard = 2
            rightExitMask.setSpawnPos(player.rect.x + 650, player.rect.y)
            player.rect.x = rightExitMask.playerSpawnPosition[0]
            player.rect.y = rightExitMask.playerSpawnPosition[1]
        elif rightExitMask is not None and pygame.sprite.collide_mask(player, rightExitMask):  # Board 2 -- Right Exit
            print("Leaving Grass")
            spriteGroup = clearGroup(spriteGroup)
            switchBoard(1)
            objects = clearGroup(objects)
            currentBoard = 1
            leftExitMask.setSpawnPos(player.rect.x - 650, player.rect.y)
            player.rect.x = leftExitMask.playerSpawnPosition[0]
            player.rect.y = leftExitMask.playerSpawnPosition[1]

    # </editor-fold>


    # <editor-fold desc="Debug Info">
    font = pygame.font.Font(None, 15)
    text = font.render(str(fpsClock)[11:13], 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.topleft = DISPLAYSURF.get_rect().topleft
    # </editor-fold>

    # <editor-fold desc="Checks collision with playerBounds or mapMask">
    if pygame.sprite.collide_mask(player, mapMask) or pygame.sprite.collide_mask(player, playerBounds):
        player.rect.x = old_player_coor[0]
        player.rect.y = old_player_coor[1]
        is_walking = False
    else:
        old_player_coor = (player.rect.x, player.rect.y)  # Stops player from moving if collision is detected
    # </editor-fold>

    # Reset Walking Counter-------------------------------------------
    if is_walking == False or walking_counter > walk_cycle_speed:
        walking_counter = 0

    # Changes player Sprite according to Direction------------
    direction_calibration(direction)

    # Changes Player Sprite according to Walking Cycle Position--------------------------------
    if is_walking:
        if (is_running):
            walk_cycle_speed = 20
            running_cycle(direction)
        else:
            walk_cycle_speed = 40
            walking_cycle(direction)
        walking_counter += 1

    # <editor-fold desc="Animation Player">
    animation_counter += 1
    if is_walking == False and animation_delay > 60 * player_idle_animation_delay:
        if direction == DOWN:  # Idle animation for player facing down ------------------------------
            if animation_counter > 89:
                animation_counter = 0
            image = animation(90, animation_counter, "DownIdleAnimation_CoinFlip", os.path.expanduser(
                '~') + "/Desktop/ngtbgame/Animations/PlayerAnimations/")
            image = pygame.transform.scale(image, expandUpDown)
            player.image = image
        if direction == LEFT:  # Idle animation for player facing left ------------------------------
            if animation_counter > 44:
                animation_counter = 0
            image = animation(45, animation_counter, "LeftIdleAnimation_Dance", os.path.expanduser(
                '~') + "/Desktop/ngtbgame/Animations/PlayerAnimations/")
            image = pygame.transform.scale(image, expandLeftRight)
            player.image = image
        if direction == RIGHT:  # Idle animation for player facing right ------------------------------
            if animation_counter > 119:
                animation_counter = 0
            image = animation(120, animation_counter, "RightIdleAnimation_PhoneLook", os.path.expanduser(
                '~') + "/Desktop/ngtbgame/Animations/PlayerAnimations/"
                              )
            image = pygame.transform.scale(image, expandLeftRight)
            player.image = image
    # </editor-fold>


    # Reset Delay Counter
    elif is_walking == True or is_running:
        animation_delay = 0

    # <editor-fold desc = "Fountain Animation">
    if currentBoard == 2:
        if animation_counter > 59:
            animation_counter = 0
        image = animation(60, animation_counter - 1, "FountainAnimation",
                          os.path.expanduser(
                              '~') + "/Desktop/ngtbgame/Animations/ObjectAnimations/"
                          )
        for obj in objects:
            if obj.name == "Fountain":
                image = pygame.transform.scale(image, (obj.xSize, obj.ySize))
                obj.image = image
    # </editor-fold>

    # <editor-fold desc="Rendering">
    pygame.sprite.Group.update(spriteGroup)
    DISPLAYSURF.fill((255, 255, 255))
    DISPLAYSURF.blit(background, (0, 0))
    for item in iter(spriteGroup):
        pygame.sprite.LayeredUpdates.add(default_layer, item)
        if item != player:
            if item.rect.y < player.rect.y - 75:
                pygame.sprite.LayeredUpdates.move_to_front(default_layer, player)
            else:
                pygame.sprite.LayeredUpdates.move_to_back(default_layer, player)

    pygame.sprite.LayeredUpdates.draw(default_layer, DISPLAYSURF)
    DISPLAYSURF.blit(text, textpos)
    # </editor-fold>

    # <editor-fold desc="Moves player according to direction and speed">
    pygame.display.flip()
    if keys[0]:
        direction = LEFT
        player.rect.x -= move_speed
        is_walking = True
    elif keys[1]:
        direction = RIGHT
        player.rect.x += move_speed
        is_walking = True
    elif keys[3]:
        direction = DOWN
        player.rect.y += move_speed
        is_walking = True
    elif keys[2]:
        direction = UP
        player.rect.y -= move_speed
        is_walking = True
    # End
    # </editor-fold>

    # <editor-fold desc="Moves player according to direction and speed">
    for event in pygame.event.get():
        # Sets booleans according to key status (Pressing Down)
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                keys[1] = True
            if event.key == K_LEFT:
                keys[0] = True
            if event.key == K_UP:
                keys[2] = True
            if event.key == K_DOWN:
                keys[3] = True
            if event.key == K_LSHIFT:
                is_running = True
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                objectListFile.close()
            if event.key == K_v and fullscreen == False:
                DISPLAYSURF = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
                fullscreen = True
            elif event.key == K_v:
                pygame.display.set_mode((800, 600), pygame.RESIZABLE)
                fullscreen = False

        # Sets booleans according to key status (Releasing)
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
            if event.key == K_LSHIFT:
                is_running = False

        # Quit Command
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            objectListFile.close()
    # </editor-fold>

    # Additional Bug Information, Only prints once a second
    if (game_loop_counter % 60 == 0):
        doNothing = True
    pygame.display.update()
    fpsClock.tick(FPS)
