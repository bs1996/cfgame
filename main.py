# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import pygame
import client
menuwindow = True

menu = pygame.display.set_mode((300,600))
pygame.display.set_caption("cfgame-MENU")
while menuwindow:
    for event1 in pygame.event.get():
        if event1.type == pygame.KEYDOWN:
            if event1.key == pygame.K_KP_ENTER:
                client.client()
        # only do something if the event is of type QUIT
        if event1.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            menuwindow = False




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
