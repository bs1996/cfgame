import pygame,sys,numpy
import socket
def client():

    pygame.init()
    screen = pygame.display.set_mode((600,600))
    # define a variable to control the main loop
    running = True
    pygame.display.set_caption("cfgame")
    x1 = 50
    y1 = 50
    x = 0.5
    y = 0.0
    direction = 0
    gameover = 0
    road = []
    t=0
    # main loop
    while running:
        # event handling, gets all event from the event queue
        player1 = pygame.draw.rect(screen, pygame.Color(100,255,255), pygame.Rect(x1, y1, 10, 10))
        if x1 >= 600 and direction == 0:
            x1 = 0
        if x1 <= 0 and direction == 3:
            x1 = 600
        if y1 >= 600 and direction == 1:
            y1 = 0
        if y1 <= 0 and direction == 2:
            y1 = 600
        if gameover == 0 and t>2:
            x1 = x1 + x
            y1 = y1 + y
            point = numpy.array([x1, y1])
            road.append(point)
            for i in road[0:-2]:
                if numpy.array_equal(i,point):
                    gameover=1
                    print(i)
                    print(point)
                    print('gameover')



        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(100)
        t=t+0.01
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_DOWN and direction == 0:
                    x = 0.0
                    y = 0.5
                    direction = 1

                if event.key == pygame.K_UP and direction == 0:
                    x = 0
                    y = -0.5
                    direction = 2

                if event.key == pygame.K_LEFT and direction == 2:
                    x = -0.5
                    y = 0
                    direction = 3
                if event.key == pygame.K_RIGHT and direction == 2:
                    x = 0.5
                    y = 0
                    direction = 0
                if event.key == pygame.K_DOWN and direction == 3:
                    x = 0
                    y = 0.5
                    direction = 1

                if event.key == pygame.K_UP and direction == 3:
                    x = 0
                    y = -0.5
                    direction = 2
                if event.key == pygame.K_LEFT and direction == 1:
                    x = -0.5
                    y = 0
                    direction = 3
                if event.key == pygame.K_RIGHT and direction == 1:
                    x = 0.5
                    y = 0
                    direction = 0
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

