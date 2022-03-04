class Player :
    def __init__(self,x,y):
        self.running = 1
        while self.running:
            self.road(x,y)
            self.check_collision()
            self.check_button()
    def road(self,x1,y1):
        self.result = x1+y1
        print(self.result)
    def check_collision(self):
        b=3
        print(b)
    def check_button(self):
        a=5
        print(a)