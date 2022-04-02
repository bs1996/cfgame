import pygame, numpy,sys,Players,Join,server,json

def send (c,e) :
    data = json.dumps(e)
    c.send(data.encode())

def rec (c) :
    recdata = c.recv(1024).decode()
    data = json.loads(recdata)
    return data
def GameScreen(w1,w2,w3,w4,screen):
    pygame.draw.rect(screen, pygame.Color(100, 200, 255), pygame.Rect(w1[0], w1[1], 10, 10))
    pygame.draw.rect(screen, pygame.Color(100, 200, 255), pygame.Rect(w2[0], w2[1], 10, 10))
    pygame.draw.rect(screen, pygame.Color(100, 200, 255), pygame.Rect(w3[0], w3[1], 10, 10))
    pygame.draw.rect(screen, pygame.Color(100, 200, 255), pygame.Rect(w4[0], w4[1], 10, 10))
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(100)


def check_collision(r1,r2,r3,r4,p1,p2,p3,p4,g1,g2,g3,g4,loss):
    for i in r1:
        if numpy.array_equal(i, p1) and g1 == 0:
            loss = loss +1
            g1 = 1
            print('gameover')
          #  screen.blit(text1, textRect1)

    for j in r2:
        if numpy.array_equal(j, p1) and g1 == 0:
            g1 = 1
            loss = loss + 1
            print('gameover')
          #  screen.blit(text1, textRect1)

    for i in r2[0:-1]:
        if numpy.array_equal(i, p2) and g2 ==0:
            g2 = 1
            loss = loss + 1

            print('test')
           # screen.blit(text2, textRect2)

    for j in r1:
        if numpy.array_equal(j, p2) and g2 ==0:
            g2 = 1
            loss = loss + 1
            print('test')
           # screen.blit(text2, textRect2)

    return r1,r2,r3,r4,p1,p2,p3,p4,g1,g2,g3,g4,loss
def main(sock,players_number,player_number):
    pygame.init()
    pygame.font.init()
    pygame.font.get_init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("cfgame")
    running = 1
    g1, g2, g3, g4 = 0, 0, 0, 0  #gameover status
    t = 0  # time
    xp = 0.5
    yp = 0
    loss = 0
    road1 = []
    road2 = []
    road3 = []
    road4 = []
    direction = 0
    if player_number == 1:
        x = 50
        y = 50
        w1 = [x, y]
    if player_number == 2:
        x = 550
        y = 50
        w2 = [x, y]
    if player_number == 3:
        x = 550
        y = 550
        w3 = [x, y]
    if player_number == 4:
        x = 50
        y = 550
        w4 = [x, y]
    while running == 1:
        if g1 == 0:
            x = x + xp
            y = y + yp
        if loss == 3:
            running = 0
        if direction == 0:
            p1 = numpy.array([x + 10, y])
        if direction == 3:
            p1 = numpy.array([x - 10, y])
        if direction == 1:
            p1 = numpy.array([x, y + 10])
        if direction == 2:
            p1 = numpy.array([x, y - 10])

        if x >= 600 and direction == 0:
            x = 0
        if x <= 0 and direction == 3:
            x = 600
        if y >= 600 and direction == 1:
            y = 0
        if y <= 0 and direction == 2:
            y = 600
        if player_number == 1:
            road1.append(w1)
           # road2.append(w2)
           # road3.append(w3)
           # road4.append(w4)
            if t >= 2.0 :
                road1,road2,road3,road4,p1,p2,p3,p4,g1,g2,g3,g4,loss = check_collision(road1,road2,road3,road4,p1,p2,p3,p4,g1,g2,g3,g4,loss)
        data = rec(sock)
        if player_number == 1 :
            dat = {1,w1,w2,w3,w4}
            if data[0] == 2 :
                w2 = data[1]
            if data[0] == 3 :
                w3 = data[1]
            if data[0] == 4 :
                w4 = data[1]
        if player_number == 2 :
            dat = {2,w2}
            w1=data[1]
            w3=data[3]
            w4=data[4]
        if player_number == 3 :
            dat = {3,w3}
            w1 = data[1]
            w2 = data[2]
            w4 = data[4]
        if player_number == 4 :
            dat = {4,w4}
            w1 = data[1]
            w2 = data[3]
            w3 = data[3]
        send(sock,dat)
        GameScreen(w1,w2,w3,w4,screen)
        t = t + 0.01
        ######### BUTTONS ##########################

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and direction == 0:
                    xp = 0.0
                    yp = 1
                    direction = 1

                if event.key == pygame.K_UP and direction == 0:
                    xp = 0
                    yp = -1
                    direction = 2

                if event.key == pygame.K_LEFT and direction == 2:
                    xp = -1
                    yp = 0
                    direction = 3
                if event.key == pygame.K_RIGHT and direction == 2:
                    xp = 1
                    yp = 0
                    direction = 0
                if event.key == pygame.K_DOWN and direction == 3:
                    xp = 0
                    yp = 1
                    direction = 1

                if event.key == pygame.K_UP and direction == 3:
                    xp = 0
                    yp = -1
                    direction = 2
                if event.key == pygame.K_LEFT and direction == 1:
                    xp = -1
                    yp = 0
                    direction = 3
                if event.key == pygame.K_RIGHT and direction == 1:
                    xp = 1
                    yp = 0
                    direction = 0

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    return w1, w2, w3, w4
if __name__=="__main__":
    main(1,2,1)