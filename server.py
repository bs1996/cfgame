import pygame,socket,numpy,Players,json

from _thread import *
import threading
print_lock = threading.Lock()





def server(players_number):
   # initializing socket
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
   while players_number < 3:
      # accept connection
      print("Waiting for " + str(players_number) + " players")
      c, addr = s.accept()
      print('got connection from addr', addr)

      c.send(number.encode())
      Players.main(c,players_number,1)
      players_number = players_number + 1
   s.close()





