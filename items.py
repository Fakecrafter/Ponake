import pygame
import random

class Item:
    x = 5
    y = 19
    itemType = ''
    color = ''
    def draw(self, size, screen, offset):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x * size + offset[0], self.y * size + offset[1], size, size))
    def reset(self, avoidPoints, size):
        self.x = random.randint(0, size)
        self.y = random.randint(0, size)
        for i in avoidPoints:
            if [self.x, self.y] == i:
                self.reset(avoidPoints, size)
        

class Apple(Item):
    color = (205, 92, 92)

class Rosine(Item):
# hard to see this one
    color = (10,0,10)
    getSmaller = 10
    def action(self, boardSize):
        if boardSize == 10:
            return False
        if self.getSmaller == 0:
            self.getSmaller = 10
            return True
        else:
            self.getSmaller -= 1
            return None
        

