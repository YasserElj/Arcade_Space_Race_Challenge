import pygame

class Rock:
    def __init__(self, x, y, velocity, rect=pygame.Rect(0, 0, 4, 4)):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.rect = rect

    def update(self, deltaTime):
        self.x = self.x + self.velocity * deltaTime/1000

    def draw(self, screen):  
        self.rect = pygame.Rect(self.x, self.y, 4, 4)
        pygame.draw.rect(screen, (255,255,255), self.rect)
