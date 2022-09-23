from snake import Snake
# Importieren der Pygame-Bibliothek
import pygame


def drawGrid(blockSize):
    for x in range(0, 1000, blockSize):
        for y in range(0, 1000, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, GREY, rect, 1)

# initialisieren von pygame
pygame.init()

# genutzte Farbe
RED     = ( 255, 0, 0)
GREEN   = ( 0, 214, 0)
BLACK   = ( 0, 0, 0)
WHITE   = (255, 255, 255)
GREY    = (100, 100, 100)


speed = 10
blockSize = 40


# Fenster öffnen
screen = pygame.display.set_mode((1004, 1004))
pygame.display.set_caption("Snake")

# instanz der Snake kreieren
mySnake = Snake()

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while(spielaktiv):
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
        # uberpruefe tastatureingaben
        # je nach eingabe aendere richtung der snake
        elif event.type == pygame.KEYDOWN:
            safedx = mySnake.dx
            safedy = mySnake.dy
            if event.key == pygame.K_d:
                mySnake.dx = 1
                mySnake.dy = 0
            elif event.key == pygame.K_a:
                mySnake.dx = -1
                mySnake.dy = 0
            elif event.key == pygame.K_s:
                mySnake.dx = 0
                mySnake.dy = 1
            elif event.key == pygame.K_w:
                mySnake.dx = 0
                mySnake.dy = -1
            if (-1 * safedx == mySnake.dx):
                mySnake.dx = safedx
            if (-1 * safedy == mySnake.dy):
                mySnake.dy = safedy


    # Spiellogik hier integrieren
    mySnake.movement()
    mySnake.checkCollisionWall()
    mySnake.checkCollisionSelf()
    mySnake.checkCollisionItem()


    # Spielfeld löschen
    screen.fill(BLACK)
    drawGrid(blockSize)

    # Spielfeld/figuren zeichnen
    mySnake.draw(40, screen, GREEN)

    # myApple.draw()

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(speed)

pygame.quit()
