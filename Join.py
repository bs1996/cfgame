import pygame,socket,numpy,Players ,threading,json
from threading import Thread


def join(ip, nickname):
    # Define the port on which you want to connect
    pygame.font.init()
    pygame.font.get_init()
    menu = pygame.display.set_mode((600, 600))
    font1 = pygame.font.SysFont('chalkduster.ttf', 70)
    text1 = font1.render('waiting for players ', True, (0, 255, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (300, 100)
    menu.blit(text1, textRect1)
    pygame.display.update()
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # connect to server on local computer
    s.connect((ip, port))
    player_number = 10
    # message you send to server
    message = "hello"
    while player_number == 10:

        # message sent to server


        # message received from server
        player_number = int(s.recv(1024).decode())

        # print the received message
        # here it would be a reverse of sent message



        # ask the client whether he wants to continue
        print("start")
        Players.main(s,2,player_number)
    # close the connection
    s.close()

