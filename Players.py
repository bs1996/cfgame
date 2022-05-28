import pygame, numpy,sys,Join,server,json
chat = ''
chatbox = []
user_message = ''
send_message = '     send'
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
color2 = pygame.Color(100, 0, 0)
color3 = pygame.Color(100, 100, 100)
active = False

def send(c, e):
    data = json.dumps(e).encode()
    print(data)
    c.send(data)


def rec(c):
    rdata = c.recv(1024).decode()
    data = json.loads(rdata)
    return data


def GameScreen(w1, w2, w3, w4, screen):
    font3 = pygame.font.SysFont('chalkduster.ttf', 20)
    chat_rect = pygame.Rect(0, 505, 600, 50)
    send_rect = pygame.Rect(530, 555, 70, 50)
    input_rect = pygame.Rect(0, 555, 600, 50)
    pygame.draw.rect(screen, color, input_rect)
    pygame.draw.rect(screen, color2, chat_rect)
    pygame.draw.rect(screen, color3, send_rect)

    text_surface = font3.render(user_message, True, (255, 255, 255))
    text_surface2 = font3.render(chat, True, (255, 255, 255))
    text_surface3 = font3.render(send_message, True, (255, 255, 255))

    screen.blit(text_surface, (input_rect.x, input_rect.y + 5))
    screen.blit(text_surface2, (chat_rect.x, chat_rect.y + 5))
    screen.blit(text_surface3, (send_rect.x, send_rect.y + 5))

    input_rect.w = max(230, text_surface.get_width() + 10)
    pygame.draw.rect(screen, pygame.Color(100, 200, 255), pygame.Rect(w1[0], w1[1], 10, 10))
    pygame.draw.rect(screen, pygame.Color(50, 255, 50), pygame.Rect(w2[0], w2[1], 10, 10))
    pygame.draw.rect(screen, pygame.Color(100, 200, 255), pygame.Rect(w3[0], w3[1], 10, 10))
    pygame.draw.rect(screen, pygame.Color(100, 200, 255), pygame.Rect(w4[0], w4[1], 10, 10))
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(100)
    return input_rect, send_rect


def check_collision(r1, r2, r3, r4, p1, p2, p3, p4, g1, g2, g3, g4, loss):
    for i in r1:
        if numpy.array_equal(i, p1) and g1 == 0:
            loss = loss +1
            g1 = 1
            print('gameover1')
          #  screen.blit(text1, textRect1)

    for j in r2:
        if numpy.array_equal(j, p1) and g1 == 0:
            g1 = 1
            loss = loss + 1
            print('gameover1')
          #  screen.blit(text1, textRect1)

    for i in r2:
        if numpy.array_equal(i, p2) and g2 ==0:
            g2 = 1
            loss = loss + 1

            print('GAMEOVER2')
           # screen.blit(text2, textRect2)

    for j in r1:
        if numpy.array_equal(j, p2) and g2 ==0:
            g2 = 1
            loss = loss + 1
            print('GAMEOVER2')
           # screen.blit(text2, textRect2)

    return g1,g2,loss


def main(sock, players_number, player_number):
    pygame.init()
    pygame.font.init()
    pygame.font.get_init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("cfgame")
    running = 1
    global active
    global color
    global user_message
    global chat
    global chatbox
    x=0
    y=0
    g1, g2, g3, g4 = 0, 0, 0, 0 #gameover status
    w1 = [0.0,0.0]
    w2 = [0.0,0.0]
    w3 = [0.0,0.0]
    w4 = [0.0,0.0]
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    t = 0  # time
    xp = 0.5
    yp = 0
    loss = 0
    road1 = []
    road2 = []
    road3 = []
    road4 = []
    direction = 0
    direction2 = 0
    add = 0
    dat = {"number": 1, "1": w1, "g2": g2, "dir": direction, "chat": chat, "add": add}

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
        if active:
            color = color_active
        else:
            color = color_passive
            # draw rectangle and argument passed which should
            # be on screen
        if (g1 == 0 and player_number == 1) or (g2 == 0 and player_number == 2):
            x = x + xp
            y = y + yp
        if loss == 3:
            running = 0
        if player_number == 1:
            if direction == 0:
                p1 = numpy.array([x + 10, y])
            if direction == 3:
                p1 = numpy.array([x - 10, y])
            if direction == 1:
                p1 = numpy.array([x, y + 10])
            if direction == 2:
                p1 = numpy.array([x, y - 10])

            if direction2 == 0:
                p2 = numpy.array([w2[0] + 10, w2[1]])
            if direction2 == 3:
                p2 = numpy.array([w2[0] - 10, w2[1]])
            if direction2 == 1:
                p2 = numpy.array([w2[0], w2[1]+10])
            if direction2 == 2:
                p2 = numpy.array([w2[0], w2[1] - 10])
            road1.append(w1)
            road2.append(w2)
            road3.append(w3)
            road4.append(w4)
            if t >= 1.0:
                g1, g2, loss = check_collision(road1, road2, road3, road4, p1, p2, p3, p4, g1, g2, g3, g4, loss)
        if x >= 600 and direction == 0:
            x = 0
        if x <= 0 and direction == 3:
            x = 600
        if y >= 500 and direction == 1:
            y = 0
        if y <= 0 and direction == 2:
            y = 500
        data = rec(sock)
        if player_number == 1:
            w1 = [x, y]
            dat = {"number": 1, "1": w1, "g2": g2, "dir": direction, "chat": chat, "add": add}
            if data["number"] == 2:
                w2 = data["1"]
                direction2 = data["dir"]
                if data["add"] == 1:
                    chatbox.append(data["chat"])
        if player_number == 2:
            w2 = [x, y]
            direction2 = direction
            dat = {"number": 2,"1": w2, "g2": 0, "dir": direction2, "chat": chat, "add": add}
            w1 = data["1"]
            g2 = data["g2"]
            if data["add"] == 1:
                chatbox.append(data["chat"])
                print(chatbox)
        send(sock, dat)
        add = 0
        input_rect, send_rect = GameScreen(w1,w2,w3,w4,screen)
        t = t + 0.01
        ######### BUTTONS ##########################

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if send_rect.collidepoint(event.pos):
                    chat = user_message
                    user_message = ''
                    chatbox.append(chat)
                    add = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if active:
                        # get text input from 0 to -1 i.e. end.
                        user_message = user_message[:-1]
                else:
                    if active:
                        user_message += event.unicode
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

