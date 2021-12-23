import pygame ;
import socket;

pygame.init()
screen = pygame.display.set_mode((600,600))
# define a variable to control the main loop
running = True
pygame.display.set_caption("cfgame")
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
