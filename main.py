# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import pygame
import client
menuwindow = True
pygame.font.init()
pygame.font.get_init()
menu = pygame.display.set_mode((600,600))
tcpip = 0
font1 = pygame.font.SysFont('chalkduster.ttf', 70)
font2 = pygame.font.SysFont('chalkduster.ttf', 40)
text1 = font1.render('Menu', True, (0, 255, 0))
text2 = font2.render('Local mode', True, (0, 255, 0))
text3 = font2.render('TCP/IP mode', True, (0, 255, 0))
text4 = font2.render('Join', True, (0, 255, 0))
text5 = font2.render('Create server', True, (0, 255, 0))
text6 = font2.render('back', True, (0, 255, 0))
textRect1 = text1.get_rect()
textRect1.center = (300, 100)
textRect2 = text2.get_rect()
textRect2.center = (300, 300)
textRect3 = text3.get_rect()
textRect3.center = (300, 400)
textRect4 = text4.get_rect()
textRect4.center = (300, 300)
textRect5 = text5.get_rect()
textRect5.center = (300, 400)
textRect6 = text6.get_rect()
textRect6.center = (300, 500)
pygame.display.set_caption("cfgame-MENU")
xc = 200
yc = 295
while menuwindow:
    menu.fill((0,0,0))
    if tcpip == 0 :
        menu.blit(text1, textRect1)
        menu.blit(text2, textRect2)
        menu.blit(text3, textRect3)
    if tcpip == 1:
        menu.blit(text1, textRect1)
        menu.blit(text4, textRect4)
        menu.blit(text5, textRect5)
        menu.blit(text6, textRect6)


    choice = pygame.draw.rect(menu, pygame.Color(0, 255, 0), pygame.Rect(xc, yc, 10, 10))

    for event1 in pygame.event.get():
        if event1.type == pygame.KEYDOWN:
            if event1.key == pygame.K_KP_ENTER and yc == 295 and tcpip == 0:
                client.client()
            if event1.key == pygame.K_KP_ENTER and yc == 395:
                tcpip = 1
            if event1.key == pygame.K_KP_ENTER and yc == 495:
                tcpip = 0

            if event1.key == pygame.K_DOWN and yc == 295:
                yc = 395
            if event1.key == pygame.K_DOWN and yc == 395:
                yc = 495

            if event1.key == pygame.K_UP and yc == 395 :
                yc = 295
            if event1.key == pygame.K_UP and yc == 495 :
                yc = 395

        # only do something if the event is of type QUIT
        if event1.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            menuwindow = False

        pygame.display.update()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
