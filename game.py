import pygame
from pygame.locals import K_w, K_UP, K_s, K_DOWN, QUIT, K_ESCAPE, KEYDOWN, KEYUP
import numpy as np

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
color_of_items = (251, 248, 243)

rect_width = 10
rect_height = 120

surf1_y = SCREEN_HEIGHT//2
surf2_y = SCREEN_HEIGHT//2

ball_x = SCREEN_WIDTH//2
ball_y =  SCREEN_HEIGHT//2

surf1_y_movement = 0
surf2_y_movement = 0

surface_speed = 5
ball_speed = 2

if np.random.randint(0,2):
        ball_x_movement = ball_speed
else:
     ball_x_movement = -ball_speed
if np.random.randint(0,2):
        ball_y_movement = ball_speed
else:
     ball_y_movement = -ball_speed




    
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                surf2_y_movement = surface_speed
            if event.key == K_s:
                    surf1_y_movement = surface_speed
            if event.key == K_UP:
                    surf2_y_movement = -surface_speed
            if event.key == K_w:
                    surf1_y_movement = -surface_speed
        elif event.type == KEYUP:
            if event.key == K_DOWN or event.key == K_UP:
                surf2_y_movement = 0
            elif event.key == K_w or event.key == K_s:
                surf1_y_movement = 0
        elif event.type == pygame.QUIT:
            running = False
            break
    screen.fill((35,35,35))

    if surf1_y >= SCREEN_HEIGHT - rect_height and surf1_y_movement > 0:
        surf1_y_movement = 0
        surf1_y = SCREEN_HEIGHT - rect_height
    if surf1_y < 0 and surf1_y_movement < 0:
        surf1_y_movement = 0
        surf1_y = 0
    if surf2_y >= SCREEN_HEIGHT - rect_height and surf2_y_movement > 0:
        surf2_y_movement = 0
        surf2_y = SCREEN_HEIGHT - rect_height
    if surf2_y < 0 and surf2_y_movement < 0:
        surf2_y_movement = 0
        surf2_y = 0
    surf1_y += surf1_y_movement
    surf2_y += surf2_y_movement

    if ball_x < rect_width and ball_y in range(surf1_y, surf1_y+rect_height):
        ball_x_movement = ball_speed
    elif ball_x > SCREEN_WIDTH - rect_width and ball_y in range(surf2_y, surf2_y+rect_height):
         ball_x_movement = -ball_speed
    elif ball_x < rect_width or ball_x > SCREEN_WIDTH - rect_width:
         pygame.quit()

    if ball_y <= 0:
         ball_y_movement = ball_speed
    elif ball_y >= SCREEN_HEIGHT:
         ball_y_movement = -ball_speed
    
    ball_x += ball_x_movement
    ball_y += ball_y_movement


    surf1 = pygame.draw.rect(screen, color_of_items, (0,surf1_y, rect_width,rect_height))
    surf2 = pygame.draw.rect(screen, color_of_items, (SCREEN_WIDTH-10,surf2_y,rect_width,rect_height))
    ball = pygame.draw.circle(screen,color_of_items, (ball_x, ball_y),5)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
