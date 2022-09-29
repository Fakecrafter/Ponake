from snake import Snake
from items import *
from tictactoe import *
import tkinter as tk
import tile
from tile import *
import color as c
import pygame

def gameSelection():
    print("Annette Spielebibliothek:")
    print()
    print("1) Snake")
    print("2) 2048")
    print("3) Tic-Tac-Toe")
    print()
    while True:
        selection = input("Choose a game (1-3): ")
        if selection in {"1", "2", "3"}:
            return int(selection)
        else:
            print("You must type in a number in range 1 to 3")


def gameReset():
    global rowscolumns
    global moving_time
    global decreasingState
    global scoreMultiplicator
    global inputdx
    global inputdy
    global highScore
    global mySnake
    if mySnake.score > highScore:
        highScore = mySnake.score
    inputdx = 0
    inputdy = 0
    rowscolumns = 25
    moving_time = 0
    decreasingState = False
    scoreMultiplicator = 1
    mySnake.reset(rowscolumns - 1, 0)
    myApple.reset(mySnake.head + mySnake.body,rowscolumns - 1)
    myRosine.reset(mySnake.head + mySnake.body,rowscolumns - 1)
    pygame.time.wait(400)


def snakeGame():
    ### INIT ###
    # initialisieren von pygame
    pygame.init()
    pygame.font.init()

    # genutzte Farbe
    GREEN   = ( 0, 214, 0)
    BLACK   = ( 0, 0, 0)
    WHITE   = (255, 255, 255)
    GREY    = (100, 100, 100)

    # koennte wichtig sein wenn das Spielfeld NICHT bei 0,0 beginnt
    offsetX = 40
    offsetY = 40

    global rowscolumns
    global moving_time
    global decreasingState
    global scoreMultiplicator
    global inputdx
    global inputdy
    global highScore
    highScore = 0
    decreasingState = False
    moving_time = 0
    blockSize = 40
    rowscolumns = 25
    scoreMultiplicator = 1


    # Fenster öffnen
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Snake")

    # instanz der Snake kreieren
    global mySnake
    global myApple
    global myRosine
    mySnake = Snake(rowscolumns - 1)
    myApple = Apple()
    myApple.reset(mySnake.head + mySnake.body,rowscolumns - 1)
    myRosine = Rosine()
    myRosine.reset(mySnake.head + mySnake.body,rowscolumns - 1)

    # Font
    myFont = pygame.font.SysFont("arial", 40)

    # solange die Variable True ist, soll das Spiel laufen
    spielaktiv = True

    # Bildschirm Aktualisierungen einstellen
    clock = pygame.time.Clock()
    inputdx = 0
    inputdy = 0

    # GAMELOOP #
    while(spielaktiv):
        # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
        ### INPUT ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False
            # uberpruefe tastatureingaben
            # je nach eingabe aendere richtung der snake
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if mySnake.dx != -1:
                        inputdx = 1
                        inputdy = 0
                if event.key == pygame.K_a:
                    if mySnake.dx != 1:
                        inputdx = -1
                        inputdy = 0
                if event.key == pygame.K_s:
                    if mySnake.dy != -1:
                        inputdx = 0
                        inputdy = 1
                if event.key == pygame.K_w:
                    if mySnake.dy != 1:
                        inputdx = 0
                        inputdy = -1



        ### LOGIC ### 
        # die Schlange soll nur alle 4 Frames "ausgefuehrt" werden
        if moving_time == 0:
            mySnake.setDirection(inputdx, inputdy)
            if mySnake.dx != 0 or mySnake.dy != 0:

                if decreasingState == True:
                    command = myRosine.action(rowscolumns)
                    if command == True:
                        rowscolumns -= 1
                    if command == False:
                        deacreasingState = False
                        scoreMultiplicator = 1

                # move the snake one block forward
                mySnake.movement()

                # ueberpruefe ob die Snake gestorben ist
                if mySnake.checkCollisionWall(rowscolumns) == True:
                    gameReset()
                if mySnake.checkCollisionSelf() == True:
                    gameReset()

                # wenn die Snake (Kopf) auf ein Item stoesst wird es in Item gespeichert
                Item = mySnake.checkCollisionItem([[myApple.x, myApple.y], [myRosine.x, myRosine.y]], scoreMultiplicator)
                # ueberpruefe ob auf Apfel getroffen
                if Item == [myApple.x, myApple.y]:
                    myApple.reset(mySnake.head + mySnake.body,rowscolumns - 1)
                # ueberpruefe ob auf Rosine getroffen
                if Item == [myRosine.x, myRosine.y]:
                    # dumb way to make the Rosine dissappear
                    myRosine.x = -2
                    myRosine.y = -2
                    decreasingState = True
                    scoreMultiplicator = 4
                # 
                moving_time = 4
        else:
            moving_time -= 1
        myApple.checkOutside(rowscolumns)
        myRosine.checkOutside(rowscolumns)

        ### DRAW ###

        # Spielfeld löschen
        screen.fill(BLACK)

        # Spielfeld/figuren zeichnen
        for x in range(0, blockSize * rowscolumns, blockSize):
            for y in range(0, blockSize * rowscolumns, blockSize):
                rect = pygame.Rect(x + offsetX, y + offsetY, blockSize, blockSize)
                pygame.draw.rect(screen, GREY, rect, 1)
        mySnake.draw(40, screen, GREEN, [offsetX, offsetY])
        myApple.draw(40, screen, [offsetX, offsetY])
        myRosine.draw(40, screen, [offsetX, offsetY])
        screen.blit(myFont.render("Score        " + str(mySnake.score), '1', (255, 255, 255)), dest=(1200, 200))
        screen.blit(myFont.render("Highscore  " + str(highScore), '1', (255, 255, 255)), dest=(1200, 300))

        # Fenster aktualisieren
        pygame.display.flip()

        # Refresh-Zeiten festlegen
        clock.tick(60)

    pygame.font.quit()
    pygame.quit()

selection = gameSelection()
if selection == 1:
    snakeGame()
if selection == 2:
    tileGame()
if selection == 3:
    tictactoeGame()
    
