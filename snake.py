import random
import pygame

class Snake():
    head = []
    body = [] # beinhaltet kopf
    score = 0
    append = 0 # anzahl der bloecke, die die Snake noch laenger werden soll
    dy = 0
    dx = 0
    headColor = (121, 255, 97)

    def __init__(self, boardSize):
        self.head = [random.randint(4,boardSize - 4), random.randint(4,boardSize - 4)]

    def draw(self, blockSize, screen, color, offset):
        pygame.draw.rect(screen, self.headColor, pygame.Rect(self.head[0] * blockSize + offset[0], self.head[1] * blockSize + offset[1], blockSize, blockSize))
        for i in self.body:
            pygame.draw.rect(screen, color, pygame.Rect(i[0] * blockSize + offset[0], i[1] * blockSize + offset[1], blockSize, blockSize))
    def setDirection(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def movement(self):
        self.body.append(list(self.head)) # elemente an der ersten stellen einzufuegen ist nicht sehr ressourcen sparend, obwohl hat python linked lists?

        if self.append == 0:
            if len(self.body) > 0:
                self.body.pop(0)
        else:
            self.append -= 1
        self.moveHead()

    def moveHead(self):
        # snake einen block in seine richtung bewegen
        self.head[0] += self.dx
        self.head[1] += self.dy

    def appendBlock(self, multiplicator):
        # snake laenge um einen block verlaengern
        self.append += 1
        self.score += 1 * multiplicator

    def checkCollisionItem(self, itemPoints, multiplicator):
        # Kollision mit Item z.b. apfel
        for i in itemPoints:
            if i == self.head:
                self.appendBlock(multiplicator)
                return i
        return False

    def checkCollisionWall(self, boardSize):
        # kollision mit wand
        if self.head[0] > (boardSize - 1):
            return True
        if self.head[1] > (boardSize - 1):
            return True
        if self.head[0] < 0:
            return True
        if self.head[1] < 0:
            return True

    def checkCollisionSelf(self):
        # Kollision mit sich selbst
        for i in self.body:
            if i == self.head:
                return True

    def reset(self, boardSize, length):
        self.score = 0
        self.dx = 0
        self.dy = 0
        self.body = []
        self.head = [random.randint(4, boardSize -4), random.randint(4, boardSize - 4)]
        self.append = length
