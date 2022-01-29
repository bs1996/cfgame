import pygame,socket,numpy
def server(player):
   s=socket.socket()
   port = 4000
   s.bind('',port)
   s.listen(5)
   while True:
      # Establish connection with client.
      c, addr = s.accept()
      print('Got connection from', addr)

      # send a thank you message to the client. encoding to send byte type.
      c.send('Thank you for connecting'.encode())

      # Close the connection with the client
      c.close()

      # Breaking once connection closed
      break