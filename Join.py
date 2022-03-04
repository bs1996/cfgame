import pygame,socket,numpy,Players
def join(ip):
    import socket

    message=input('write message')
    # Create a socket object
    s = socket.socket()
    # Define the port on which you want to connect
    port = 12345
    # connect to the server on local computer
    s.connect((ip, port))

    # receive data from the server and decoding to get the string.
    print(s.recv(1024).decode())
    print(s.recv(1024).decode())
    s.send(message.encode())
    # close the connection
    s.close()