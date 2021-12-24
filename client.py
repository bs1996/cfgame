import pygame ;
import socket;

pygame.init()
screen = pygame.display.set_mode((600,600))
# define a variable to control the main loop
running = True
pygame.display.set_caption("cfgame")
x1 = 50.0
y1 = 50.0
x = 0.1
y = 0.0
direction = 0
# main loop
while running:
    # event handling, gets all event from the event queue
    player1 = pygame.draw.rect(screen, pygame.Color(100,255,255), pygame.Rect(x1, y1, 10, 10))

    pygame.display.update()
    x1 = x1 + x
    y1 = y1 + y


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN and direction == 0:
                x = 0.0
                y = 0.1
                direction = 1

            if event.key == pygame.K_UP and direction == 0:
                x = 0
                y = -0.1
                direction = 2

            if event.key == pygame.K_LEFT and direction == 2:
                x = -0.1
                y = 0
                direction = 3
            if event.key == pygame.K_RIGHT and direction == 2:
                x = 0.1
                y = 0
                direction = 0
            if event.key == pygame.K_DOWN and direction == 3:
                x = 0
                y = 0.1
                direction = 1

            if event.key == pygame.K_UP and direction == 3:
                x = 0
                y = -0.1
                direction = 2
            if event.key == pygame.K_LEFT and direction == 1:
                x = -0.1
                y = 0
                direction = 3
            if event.key == pygame.K_RIGHT and direction == 1:
                x = 0.1
                y = 0
                direction = 0
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

