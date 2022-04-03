import pygame,socket,numpy,Players ,threading,json
from threading import Thread


def join(ip):

    # Define the port on which you want to connect
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

