import random
import pygame

class Snake:
    head = []
    body = 0 # beinhaltet kopf
    score = 0
    dy = 0
    dx = 0

    def __init__(self):
        self.reset()
    def draw(self, size, screen, color):
        pygame.draw.rect(screen, color, pygame.Rect(self.head[0] * size, self.head[1] * size, size, size))
    def movement(self):
        # snake einen block in seine richtung bewegen
        self.head[0] += self.dx
        self.head[1] += self.dy

    def appendBlock(self):
        # snake laenge um einen block verlaengern
        pass
    def checkCollisionItem(self):
        # Kollision mit Item z.b. apfel
        pass
    def checkCollisionWall(self):
        # kollision mit wand
        pass
    def checkCollisionSelf(self):
        # Kollision mit sich selbst
        pass
    def reset(self):
        self.score = 0
        self.dy = 0
        self.dx = 0
        self.body = []
        self.head = [0, 0]
