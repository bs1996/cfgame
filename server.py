import pygame,socket,numpy,Players,json

from _thread import *
import threading
print_lock = threading.Lock()





def server(players_number, nickname):
   # initializing socket
   pygame.font.init()
   pygame.font.get_init()
   menu = pygame.display.set_mode((600, 600))
   font1 = pygame.font.SysFont('chalkduster.ttf', 70)
   text1 = font1.render('waiting for ' + str(players_number) + ' players ', True, (0, 255, 0))
   textRect1 = text1.get_rect()
   textRect1.center = (300, 100)
   menu.blit(text1, textRect1)
   pygame.display.update()
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   host = '192.168.0.166'
   port = 12345

   # binding port and host
   s.bind((host, port))

   # waiting for a client to connect
   s.listen(5)
   number = '2'

   # a forever loop until client wants to exit
   while players_number < 5:
      # accept connection
      print("Waiting for " + str(players_number) + " players")
      c, addr = s.accept()
      print('got connection from addr', addr)

      c.send(number.encode())
      Players.main(c,players_number,1,nickname)
      players_number = players_number + 1
   s.close()





