import random



class board:
    def __init__(self):
        self.status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.X_points = 0
        self.O_points = 0

    def make_printable(self, ziffer):
        if ziffer == 0:
            return " "
        elif ziffer == 1:
            return "X"
        else:
            return "O"

    def print_points_for_X(self):
        self.X_points += 1
        print()
        print(self.X_points, ' - ', self.O_points)
        print()

    def print_points_for_O(self):
        self.O_points += 1
        print()           
        print(self.X_points, ' - ', self.O_points)
        print()


    def input_abfrage(self, spieler):
        while True: #Spieler ZUG abfrage

            Zug = input('\nSpieler' + spieler + ' ist dran:   Wo möchtest du setzen(1-9):    ')
            print()

            if len(Zug) != 1:
                Zug = ''
                continue

            elif Zug in 'abcdefghijklmnopqrstuvwxyzäüöß,.-;:_!"§$%&/()=?{[]}<>\\ \'#+*~²³^°ABCDEFGHIJKLMNOPQRSTUVWXYZÖÄÜ':
                Zug = ''
                continue

            elif Zug == '0':
                Zug = ''
                continue

            elif board1.status[int(Zug) - 1] == 0  :
                Zug = int(Zug)
                return Zug

            else:
                continue

#     def Ki_zug(self):
#         if self.status[0, 1] == spieler2.symbol:
#             return 2
#         elif self.status[0, 2] == spieler2.symbol:
#             return 1
#         elif self.status[2, 1] == spieler2.symbol:
#             return 0
#         elif self.status[0, 3] == spieler2.symbol:
#             return 6
#         elif self.status[0, 6] == spieler2.symbol:
#             return 3
#         elif self.status[3, 6] == spieler2.symbol:
#             return 0
#         elif self.status[4, 1] == spieler2.symbol:
#             return 7
#         elif self.status[1, 7] == spieler2.symbol:
#             return 4
#         elif self.status[4, 7] == spieler2.symbol:
#             return 1
#         elif self.status[2, 5] == spieler2.symbol:
#             return 8
#         elif self.status[2, 8] == spieler2.symbol:
#             return 5
#         elif self.status[8, 5] == spieler2.symbol:
#             return 2
#         elif self.status[3, 4] == spieler2.symbol:
#             return 5
#         elif self.status[3, 5] == spieler2.symbol:
#             return 4
#         elif self.status[5, 4] == spieler2.symbol:
#             return 3
#         elif self.status[7, 6] == spieler2.symbol:
#             return 8
#         elif self.status[6, 8] == spieler2.symbol:
#             return 7
#         elif self.status[7, 8] == spieler2.symbol:
#             return 6
#         elif self.status[0, 4] == spieler2.symbol:
#             return 8
#         elif self.status[0, 8] == spieler2.symbol:
#             return 4
#         elif self.status[4, 8] == spieler2.symbol:
#             return 0
#         elif self.status[6, 4] == spieler2.symbol:
#             return 2
#         elif self.status[6, 2] == spieler2.symbol:
#             return 4
#         elif self.status[2, 4] == spieler2.symbol:
#             return 6
# 
#             #gegner zug auf win überprüfen
#         elif self.status[0, 1] == spieler1.symbol:
#             return 2
#         elif self.status[0, 2] == spieler1.symbol:
#             return 1
#         elif self.status[2, 1] == spieler1.symbol:
#             return 0
#         elif self.status[0, 3] == spieler1.symbol:
#             return 6
#         elif self.status[0, 6] == spieler1.symbol:
#             return 3
#         elif self.status[3, 6] == spieler1.symbol:
#             return 0
#         elif self.status[4, 1] == spieler1.symbol:
#             return 7
#         elif self.status[1, 7] == spieler1.symbol:
#             return 4
#         elif self.status[4, 7] == spieler1.symbol:
#             return 1
#         elif self.status[2, 5] == spieler1.symbol:
#             return 8
#         elif self.status[2, 8] == spieler1.symbol:
#             return 5
#         elif self.status[8, 5] == spieler1.symbol:
#             return 2
#         elif self.status[3, 4] == spieler1.symbol:
#             return 5
#         elif self.status[3, 5] == spieler1.symbol:
#             return 4
#         elif self.status[5, 4] == spieler1.symbol:
#             return 3
#         elif self.status[7, 6] == spieler1.symbol:
#             return 8
#         elif self.status[6, 8] == spieler1.symbol:
#             return 7
#         elif self.status[7, 8] == spieler1.symbol:
#             return 6
#         elif self.status[0, 4] == spieler1.symbol:
#             return 8
#         elif self.status[0, 8] == spieler1.symbol:
#             return 4
#         elif self.status[4, 8] == spieler1.symbol:
#             return 0
#         elif self.status[6, 4] == spieler1.symbol:
#             return 2
#         elif self.status[6, 2] == spieler1.symbol:
#             return 4
#         elif self.status[2, 4] == spieler1.symbol:
#             return 6
#         
#         elif self.status[0] == 0:
#             return 0
#         elif self.status[8] == 0:
#             return 8
#         elif self.status[2] == 0:
#             return 2
#         elif self.status[6] == 0:
#             return 6
#         elif self.status[1] == 0:
#             return 1
#         elif self.status[5] == 0:
#             return 5
#         elif self.status[3] == 0:
#             return 3
#         elif self.status[7] == 0:
#             return 7
#         elif self.status[4] == 0:
#             return 4


    def print_board(self):
        print("",self.make_printable(self.status[0]), " | ", self.make_printable(self.status[1]), " | ", self.make_printable(self.status[2]), "\n----------------\n",self.make_printable(self.status[3]), " | ", self.make_printable(self.status[4]), " | ", self.make_printable(self.status[5]),"\n----------------\n",self.make_printable(self.status[6]), " | ", self.make_printable(self.status[7]), " | ", self.make_printable(self.status[8])
             )

    def spieler_zug(self, zelle, spieler):
        self.status[int(zelle) - 1] = spieler.symbol

    def check_win(self, symbol):
        if   self.status[0] == symbol and self.status[1] == symbol and self.status[2] == symbol:
            return True
        elif self.status[3] == symbol and self.status[4] == symbol and self.status[5] == symbol:
            return True
        elif self.status[6] == symbol and self.status[7] == symbol and self.status[8] == symbol:
            return True
        elif self.status[0] == symbol and self.status[3] == symbol and self.status[6] == symbol:
            return True
        elif self.status[1] == symbol and self.status[4] == symbol and self.status[7] == symbol:
            return True
        elif self.status[2] == symbol and self.status[5] == symbol and self.status[8] == symbol:
            return True
        elif self.status[0] == symbol and self.status[4] == symbol and self.status[8] == symbol:
            return True
        elif self.status[2] == symbol and self.status[4] == symbol and self.status[6] == symbol:
            return True
        else:
            return False

    
class spieler():
    def __init__(self, symbol):
        self.symbol = symbol


        
#die Main-Methode
def tictactoeGame():
    print()
    print()
    print()
    print()
    print()

    print('Willkommen zu Tic-Tac-Toe')
    print('_________________________')
    print('''\nBei Tic-Tac-Toe musst du drei deines Symbols in eine Reihe bringen. Ob horizontal, vertikal oder diagonal.
    Dann wirst du aufgefordert eine Zahl zwischen 1 und 9 einzugeben, dabei ist 1 oben links und 9 unten rechts:
    1  |  2  |  3  
  -----------------
    4  |  5  |  6  
  -----------------
    7  |  8  |  9  
    ''')


    global board1
    board1 = board()

    spieler2 = spieler(2)
    spieler1 = spieler(1)
    


    while True:#Die Hauptschleife

        
        board1.print_board()
    
        board1.spieler_zug(board1.input_abfrage('1'), spieler1)
        board1.print_board()

        if board1.check_win(1):
            print('\nSpieler 1, du hast gewonnen!  :)')
            board1.print_points_for_X()
            
            weiterspielen = input('Willst du weiterspielen(ja oder nein):   ')
            if weiterspielen.startswith('j'):
                weiterspielen = ''
                board1.status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                continue
            else:
                break
            
        #unentschieden überprüfen
        if 0 not in board1.status:
            print('\nUnentschieden!')
            print( 'Weiterhin ', board1.X_points, ' - ', board1.O_points)
            weiterspielen = input('Willst du weiterspielen(ja oder nein):   ')
            if weiterspielen.startswith('j'):
                weiterspielen = ''
                board1.status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                continue
            else:
                break

            

        #Zug 2 ausführen und win überprüfen
        board1.spieler_zug(board1.input_abfrage('2'), spieler2)
        if board1.check_win(2):
            board1.print_board()
            print('\nSpieler 2, du hast gewonnen!   :)')
            board1.print_points_for_O
            weiterspielen = input('Willst du weiterspielen(ja oder nein):   ')
            if weiterspielen.startswith('j'):
                weiterspielen = ''
                board1.status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                continue
            else:
                break
        
        if 0 not in board1.status:
            print('\nUnentschieden!')
            print( 'Weiterhin ', board1.X_points, ' - ', board1.O_points)
            weiterspielen = input('Willst du weiterspielen(ja oder nein):   ')
            if weiterspielen.startswith('j'):
                weiterspielen = ''
                board1.status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                continue
            else:
                break
