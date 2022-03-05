import pygame,socket,numpy,Players
from _thread import *
import threading
print_lock = threading.Lock()


# thread function
def threaded(c):
   while True:

      # data received from client
      data = c.recv(1024)
      if not data:
         print('Bye')

         # lock released on exit
         print_lock.release()
         break

      # reverse the given string from client
      data = data[::-1]

      # send back reversed string to client
      c.send(data)

   # connection closed
   c.close()
def server(player_number):
   # next create a socket object
   s = socket.socket()
   print("Socket successfully created")
   stnumber = str(player_number)
   # reserve a port on your computer in our
   # case it is 12345 but it can be anything
   port = 12345

   # Next bind to the port
   # we have not typed any ip in the ip field
   # instead we have inputted an empty string
   # this makes the server listen to requests
   # coming from other computers on the network
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind(('', port))
   print("socket binded to %s" % (port))

   # put the socket into listening mode
   s.listen(5)
   print("Waiting for players")

   # a forever loop until we interrupt it or
   # an error occurs
   while True:
      # establish connection with client
      c, addr = s.accept()

      # lock acquired by client
      print_lock.acquire()
      print('Connected to :', addr[0], ':', addr[1])

      # Start a new thread and return its identifier
      start_new_thread(threaded, (c,))

   s.close()

