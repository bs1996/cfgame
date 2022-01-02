import pygame,sys,numpy
import socket
def client():
    pygame.init()
    pygame.font.init()
    pygame.font.get_init()
    font2 = pygame.font.SysFont('chalkduster.ttf', 40)
    text1 = font2.render('player 2 win !!', True, (0, 255, 0))
    text2 = font2.render('player 1 win !!', True, (0, 255, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (300, 300)
    textRect2 = text2.get_rect()
    textRect2.center = (300, 300)

    screen = pygame.display.set_mode((600,600))
    # define a variable to control the main loop
    running = True
    pygame.display.set_caption("cfgame")
    x1 = 50
    y1 = 50
    x2 = 400
    y2 = 400
    xp1 = 0.5
    yp1 = 0.0
    xp2 = 0.5
    yp2 = 0.0
    direction1 = 0
    direction2 = 0
    gameover = 0
    road1 = []
    road2 = []
    t=0
    # main loop
    while running:
        # event handling, gets all event from the event queue
        player1 = pygame.draw.rect(screen, pygame.Color(100,255,255), pygame.Rect(x1, y1, 10, 10))
        player2 = pygame.draw.rect(screen, pygame.Color(100, 100, 255), pygame.Rect(x2, y2, 10, 10))
        if x1 >= 600 and direction1 == 0:
            x1 = 0
        if x1 <= 0 and direction1 == 3:
            x1 = 600
        if y1 >= 600 and direction1 == 1:
            y1 = 0
        if y1 <= 0 and direction1 == 2:
            y1 = 600
        if x2 >= 600 and direction2 == 0:
            x2 = 0
        if x2 <= 0 and direction2 == 3:
            x2 = 600
        if y2 >= 600 and direction2 == 1:
            y2 = 0
        if y2 <= 0 and direction2 == 2:
            y2 = 600
        if gameover == 0 and t>2:
            x1 = x1 + xp1
            y1 = y1 + yp1
            x2 = x2 + xp2
            y2 = y2 + yp2
            point1 = numpy.array([x1, y1])
            point2 = numpy.array([x2, y2])
            for i in road1[0:-1]:
                if numpy.array_equal(i,point1):
                    gameover=1
                    print(i)
                    print(point1)
                    print('gameover')
                    screen.blit(text1, textRect1)

            for j in road2:
                if numpy.array_equal(j,point1):
                    gameover=1
                    print('gameover')
                    screen.blit(text1, textRect1)

            for i in road2[0:-1]:
                if numpy.array_equal(i,point2):
                    gameover=1
                    print(i)
                    print(point1)
                    print('gameover')
                    screen.blit(text2, textRect2)

            for j in road1:
                if numpy.array_equal(j,point2):
                    gameover=1
                    print('gameover')
                    screen.blit(text2, textRect2)

            road1.append(point1)
            road2.append(point2)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(100)
        t=t+0.01
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and direction1 == 0:
                    xp1 = 0.0
                    yp1 = 0.5
                    direction1 = 1

                if event.key == pygame.K_UP and direction1 == 0:
                    xp1 = 0
                    yp1 = -0.5
                    direction1 = 2

                if event.key == pygame.K_LEFT and direction1 == 2:
                    xp1 = -0.5
                    yp1 = 0
                    direction1 = 3
                if event.key == pygame.K_RIGHT and direction1 == 2:
                    xp1 = 0.5
                    yp1 = 0
                    direction1 = 0
                if event.key == pygame.K_DOWN and direction1 == 3:
                    xp1 = 0
                    yp1 = 0.5
                    direction1 = 1

                if event.key == pygame.K_UP and direction1 == 3:
                    xp1 = 0
                    yp1 = -0.5
                    direction1 = 2
                if event.key == pygame.K_LEFT and direction1 == 1:
                    xp1 = -0.5
                    yp1 = 0
                    direction1 = 3
                if event.key == pygame.K_RIGHT and direction1 == 1:
                    xp1 = 0.5
                    yp1 = 0
                    direction1 = 0
                if event.key == pygame.K_s and direction2 == 0:
                    xp2 = 0.0
                    yp2 = 0.5
                    direction2 = 1

                if event.key == pygame.K_w and direction2 == 0:
                    xp2 = 0
                    yp2 = -0.5
                    direction2 = 2

                if event.key == pygame.K_a and direction2 == 2:
                    xp2 = -0.5
                    yp2 = 0
                    direction2 = 3
                if event.key == pygame.K_d and direction2 == 2:
                    xp2 = 0.5
                    yp2 = 0
                    direction2 = 0
                if event.key == pygame.K_s and direction2 == 3:
                    xp2 = 0
                    yp2 = 0.5
                    direction2 = 1

                if event.key == pygame.K_w and direction2 == 3:
                    xp2 = 0
                    yp2 = -0.5
                    direction2 = 2
                if event.key == pygame.K_a and direction2 == 1:
                    xp2 = -0.5
                    yp2 = 0
                    direction2 = 3
                if event.key == pygame.K_d and direction2 == 1:
                    xp2 = 0.5
                    yp2 = 0
                    direction2 = 0
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

