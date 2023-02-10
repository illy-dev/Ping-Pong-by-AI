import pygame
import sys

# initialize pygame
pygame.init()

# screen size
screen_width = 800
screen_height = 600

# create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# player1 position and size
player1_x = 20
player1_y = screen_height/2
player1_width = 20
player1_height = 100

# player2 position and size
player2_x = screen_width - 40
player2_y = screen_height/2
player2_width = 20
player2_height = 100

# ball position
ball_x = screen_width/2
ball_y = screen_height/2

# ball radius
ball_radius = 20

# ball velocity
ball_velocity_x = 1
ball_velocity_y = 1

# player1 velocity
player1_velocity = 0

# player1 speed
player1_speed = 2

while True:
    # update ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # update player1 position
    player1_y += player1_velocity

    # check for collision with top or bottom of screen
    if ball_y <= 0 or ball_y >= screen_height-ball_radius*2:
        ball_velocity_y = -ball_velocity_y

    # check for collision with player1 or player2
    if ball_x <= player1_width and (player1_y <= ball_y <= player1_y+player1_height):
        ball_velocity_x = -ball_velocity_x
    if ball_x >= screen_width-player2_width-ball_radius*2 and (player2_y <= ball_y <= player2_y+player2_height):
        ball_velocity_x = -ball_velocity_x

    # check if ball is out of the screen
    if ball_x<=0 or ball_x>=screen_width:
        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_velocity_x = -ball_velocity_x

    # clear screen
    screen.fill((0, 0, 0))

    # draw players and ball
    pygame.draw.rect(screen, (255, 255, 255), (player1_x, player1_y, player1_width, player1_height))
    pygame.draw.rect(screen, (255, 255, 255), (player2_x, player2_y, player2_width, player2_height))
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_x), int(ball_y)), ball_radius)

    # update display
    pygame.display.update()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_velocity = -player1_speed
            elif event.key == pygame.K_DOWN:
                player1_velocity = player1_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1_velocity = 0
