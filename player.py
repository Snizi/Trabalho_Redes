import pygame

class Player():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.color = color
        self.rect = (x,y,self.width,self.height)
        self.vel = 3
        self.history = [[self.x, self.y]]

    def draw(self, win):
        for i in range(len(self.history)):
                pygame.draw.rect(win, self.color, (self.history[i][0], self.history[i][1], self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.history.append([self.x, self.y])
        if len(self.history) > 70:
            self.history.pop(0)
        self.update()
        

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
