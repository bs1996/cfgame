import pygame,socket,numpy,Players ,threading,json
from threading import Thread


def join(ip):

    # Define the port on which you want to connect
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # connect to server on local computer
    s.connect((ip, port))

    # message you send to server
    message = "hello"
    while True:

        # message sent to server
        s.send(message.encode())

        # message received from server
        player_number = int(s.recv(1024).decode())

        # print the received message
        # here it would be a reverse of sent message



        # ask the client whether he wants to continue
        print("start")
        Players.main(s,2,player_number)
    # close the connection
    s.close()

