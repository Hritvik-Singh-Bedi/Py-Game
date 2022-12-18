import pygame
import random
import math

from pygame import mixer

# Initialise Pygame
pygame.init()  # mandatory for every pygame program

# Create screem
screen = pygame.display.set_mode((800, 600))  # (width, height)

# Background
# background = pygame.image.load('nino.PNG')

# Background Music
# mixer.music.load('file name')     # music is used here because we want it to play long...
# mixer.music.play(-1)      # -1 is for looping the music

# Title and Icon
pygame.display.set_caption("BHADUE ALIENS")  # For changing title

# this whole commented code is used to update the small icon on top left
'''icon = pygame.image.load("name of the image.extension")  #icon here is a variable
pygame.display.set._icon(variable name,i.e, icon) '''

# Player
playerImg = pygame.image.load('player.png')
playerX = 370  # co-ordinates of x-axis
playerY = 480  # co-ordinates of y-axis
playerX_change = 0
# playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))  # random co-ordinates of x-axis
    enemyY.append(random.randint(50, 150))  # random co-ordinates of y-axis
    enemyX_change.append(0.15)
    enemyY_change.append(40)

# Bullet
# ready: can't see the bullet on screen
# fire: the bullet is currently moving
bulletImg = pygame.image.load('Bullet.png')
bulletX = 0  # co-ordinates of x-axis
bulletY = 480  # same co-ordinates of ship for y-axis
bulletX_change = 0
bulletY_change = 0.4
bullet_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
TextX = 10
TextY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 72)

def player(x, y):  # Send in the values of new co-ordinates that's why x,y
    screen.blit(playerImg, (x, y))  # blit helps in drawing the image on the screen
    # x, y in blit helps to take the co-ordinates and draw the image at that point


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def firing_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# game-loop (infinite loop so our screen does'nt close automatically)
# anything we want to be persistent in our game ,i.e, the values we want to be in our game which remain until we hit
# the red cross will be written in this while loop...
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if a keystroke is pressed and i if yes whether its a left key or right key
        '''if event.type == pygame.KEYDOWN:   # KEYDOWN tells if a key is pressed
            print("A key is pressed")
            if event.key == pygame.K_LEFT:  # key object is used to identify the key
                print("Left arrow key is pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow key is pressed")

        if event.type == pygame.KEYUP:   # KEYUP tells if a key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key is released")'''

        # For Moving LEFT and RIGHT
        if event.type == pygame.KEYDOWN:  # KEYDOWN tells if a key is pressed
            if event.key == pygame.K_LEFT:  # key object is used to identify the key
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # bullet_sound = mixer.Sound('file name')   # here we used Sound instead of music
                    # bullet_sound.play()
                    # gets the current x co-ordinate of ship
                    bulletX = playerX
                    firing_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # KEYUP tells if a key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # to stop the player from moving

        # For Moving UP and DOWN
        '''if event.type == pygame.KEYDOWN:  # KEYDOWN tells if a key is pressed
            if event.key == pygame.K_UP:  # key object is used to identify the key
                playerY_change = -0.1
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1

        if event.type == pygame.KEYUP:  # KEYUP tells if a key is released
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0  # to stop the player from moving'''

    # Background color
    screen.fill((0, 0, 0))
    # screen.blit(background, (0, 0))   # this background is strong thats Y the components get slowed as the speed
    # we gave is way too small so in order to overcome this change the speed...
    '''playerX += 0.01  # player is moving 0.01 space towards right'''
    playerX += playerX_change
    # Creating Boundries for Spaceship so it doesn't go out of bounds
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 800(total width) - 64(width of image) = 736
        playerX = 736

    # Enemy Movements
    for i in range(num_of_enemies):
        if enemyY[i] > 400:   # if enemies come below 400px GAME OVER
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.15
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.15
            enemyY[i] += enemyY_change[i]

        # Collision
        Collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if Collision:
            # explosion_sound = mixer.Sound('file name')   # here we used Sound instead of music
            # explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # print(score)
            enemyX[i] = random.randint(0, 735)  # random co-ordinates of x-axis
            enemyY[i] = random.randint(50, 150)  # random co-ordinates of y-axis

        enemy(enemyX[i], enemyY[i], i)

    '''if enemyY <=0:
        enemyY = 0      # ab iss niche nahi jaayega
    elif enemyY >= 536:
        enemyY =536'''
    '''playerY += playerY_change'''
    player(playerX, playerY)  # function call  #value of playerX and playerY is send to the function

    '''enemy(enemyX[i], enemyY[i])'''

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        firing_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    '''Collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if Collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)  # random co-ordinates of x-axis
        enemyY = random.randint(50, 150)  # random co-ordinates of y-axis'''
    show_score(TextX, TextY)
    pygame.display.update()  # mandatory line which helps in updating the value on change in the game window
