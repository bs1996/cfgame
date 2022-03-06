import pygame,socket,numpy,Players ,threading
from threading import Thread
def join(ip):

    # Define the port on which you want to connect
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # connect to server on local computer
    s.connect((ip, port))

    # message you send to server
    message = "shaurya says geeksforgeeks"
    while True:

        # message sent to server
        s.send(message.encode())

        # message received from server
        data = s.recv(1024)

        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :', str(data.decode()))

        # ask the client whether he wants to continue
        ans = input()
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()

