# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import pygame
import local
import server
import Join
menuwindow = True
pygame.font.init()
pygame.font.get_init()
menu = pygame.display.set_mode((600,600))
players = [2,3,4]
i=0
tcpip = 0
joinmenu = 0
createserver = 0

user_text = ''
nickname = ''
nickname2 = ''
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
color2 = color_passive
color3 = color_passive
active1 = False
active2 = False
active3 = False
font1 = pygame.font.SysFont('chalkduster.ttf', 70)
font2 = pygame.font.SysFont('chalkduster.ttf', 40)
text1 = font1.render('Menu', True, (0, 255, 0))
text2 = font2.render('Local mode', True, (0, 255, 0))
text3 = font2.render('TCP/IP mode', True, (0, 255, 0))
text4 = font2.render('Join', True, (0, 255, 0))
text5 = font2.render('Create server', True, (0, 255, 0))
text6 = font2.render('back', True, (0, 255, 0))
text7 = font2.render('Server IP :', True, (0, 255, 0))
text8 = font2.render('Connect', True, (0, 255, 0))
text9 = font2.render('Start', True, (0, 255, 0))
text12 = font2.render('Nickname: ', True, (0, 255, 0))



input_rect = pygame.Rect(230, 180, 400, 32)
input_rect2 = pygame.Rect(230, 280, 400, 32)
input_rect3 = pygame.Rect(230, 180, 400, 32)

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
textRect7 = text6.get_rect()
textRect7.center = (100, 200)
textRect8 = text6.get_rect()
textRect8.center = (300,500)
textRect9 = text8.get_rect()
textRect9.center = (300,400)
textRect10 = text6.get_rect()
textRect10.center = (300,500)
textRect15 = text12.get_rect()
textRect15.center = (140,300)
textRect16 = text12.get_rect()
textRect16.center = (140,200)
textRect12 = text9.get_rect()
textRect12.center = (300,300)
pygame.display.set_caption("cfgame-MENU")
xc = 200
yc = 295
while menuwindow:
    menu.fill((0,0,0))
    if tcpip == 0 and joinmenu == 0 and createserver == 0 :
        menu.blit(text1, textRect1)
        menu.blit(text2, textRect2)
        menu.blit(text3, textRect3)
    if tcpip == 1:
        menu.blit(text1, textRect1)
        menu.blit(text4, textRect4)
        menu.blit(text5, textRect5)
        menu.blit(text6, textRect6)
    if joinmenu == 1 and tcpip == 0:
        menu.blit(text1, textRect1)
        menu.blit(text8, textRect9)
        menu.blit(text7, textRect7)
        menu.blit(text6, textRect8)
        menu.blit(text12, textRect15)
        if active1:
            color = color_active
        else:
            color = color_passive
            # draw rectangle and argument passed which should
            # be on screen
        if active2:
            color2 = color_active
        else:
            color2 = color_passive
            # draw rectangle and argument passed which should
            # be on screen
        pygame.draw.rect(menu, color, input_rect)
        pygame.draw.rect(menu, color2, input_rect2)

        text_surface = font2.render(user_text, True, (255, 255, 255))
        menu.blit(text_surface, (input_rect.x, input_rect.y + 5))
        input_rect.w = max(230, text_surface.get_width() + 10)
        text_surface2 = font2.render(nickname, True, (255, 255, 255))
        menu.blit(text_surface2, (input_rect2.x, input_rect2.y + 5))
        input_rect2.w = max(230, text_surface2.get_width() + 10)
    if createserver == 1 :
        text10 = font2.render('Number of players:' + str(players[i]), True, (0, 255, 0))
        textRect11 = text10.get_rect()
        textRect11.center = (300, 400)
        menu.blit(text6, textRect10)
        menu.blit(text10, textRect11)
        menu.blit(text9, textRect12)
        menu.blit(text12, textRect16)
        if active3:
            color3 = color_active
        else:
            color3 = color_passive
            # draw rectangle and argument passed which should
            # be on screen

        pygame.draw.rect(menu, color3, input_rect3)

        text_surface3 = font2.render(nickname2, True, (255, 255, 255))
        menu.blit(text_surface3, (input_rect3.x, input_rect3.y + 5))
        input_rect3.w = max(230, text_surface3.get_width() + 10)
    choice = pygame.draw.rect(menu, pygame.Color(0, 255, 0), pygame.Rect(xc, yc, 10, 10))

    for event1 in pygame.event.get():
        if event1.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event1.pos):
                active1 = True
            else:
                active1 = False
            if input_rect2.collidepoint(event1.pos):
                active2 = True
            else:
                active2 = False
            if input_rect3.collidepoint(event1.pos):
                active3 = True
            else:
                active3 = False
        if event1.type == pygame.KEYDOWN:
            # Check for backspace
            if event1.key == pygame.K_BACKSPACE:
                if active1:
                # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                if active2:
                    nickname = nickname[:-1]
                if active3:
                    nickname2 = nickname2[:-1]
            # Unicode standard is used for string
            # formation
            else:
                if active1:
                    user_text += event1.unicode
                if active2:
                    nickname += event1.unicode
                if active3:
                    nickname2 += event1.unicode
            if event1.key == pygame.K_RETURN and yc == 295 and tcpip == 0 and joinmenu == 0 and createserver == 0:
                local.local()
            if event1.key == pygame.K_RETURN and yc == 295 and tcpip == 1:
                joinmenu = 1
                yc = 395
                tcpip = 0
            if event1.key == pygame.K_RETURN and yc == 495 and createserver == 1:
                createserver = 0
                tcpip = 1
                yc = 295
            if event1.key == pygame.K_RETURN and yc == 295 and createserver == 1:
                server.server(players[i], nickname2)


            if event1.key == pygame.K_RETURN and yc == 395 and joinmenu == 1 and len(user_text) > 11:
                Join.join(user_text, nickname)


            if event1.key == pygame.K_RETURN and yc == 495 and joinmenu == 1 and tcpip == 0:
                joinmenu = 0
                tcpip = 1
                createserver = 0
                yc = 295
            if event1.key == pygame.K_RETURN and yc == 395 and tcpip == 1:
                createserver = 1
                tcpip = 0
                joinmenu = 0
                yc = 295
            if event1.key == pygame.K_RETURN and yc == 395 and createserver == 0 and joinmenu == 0 and tcpip == 0:
                tcpip = 1
            if event1.key == pygame.K_LEFT and i > 0 and yc == 395 and createserver == 1:
                i = i - 1
            if event1.key == pygame.K_RIGHT and i < 2 and yc == 395 and createserver == 1:
                i = i + 1
            if event1.key == pygame.K_RETURN and yc == 495:
                tcpip = 0
                yc = 295
            if event1.key == pygame.K_DOWN and yc == 395 and (tcpip == 1 or createserver == 1 or joinmenu == 1):
                yc = 495
            if event1.key == pygame.K_DOWN and yc == 295:
                yc = 395
            if event1.key == pygame.K_UP and yc == 395 and joinmenu == 0:
                yc = 295
            if event1.key == pygame.K_UP and yc == 495:
                yc = 395

        # only do something if the event is of type QUIT
        if event1.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            menuwindow = False
        pygame.display.update()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
