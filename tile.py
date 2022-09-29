import tkinter as tk
import color as c
import random




score = 0


class tileGame(tk.Frame): 						
        def __init__(self):
                # erstellt das Fenster für das Spiel
                tk.Frame.__init__(self)
                self.grid()
                self.master.title("2048")

                self.main_grid = tk.Frame(
                        self, bg=c .GRID_COLOR, bd=3, width=600, height=600
                        )
			
                self.main_grid.grid(pady=(100, 0))
                self.make_GUI()
                self.start()
                # sind die Tasten
                self.master.bind("<Left>", self.left)
                self.master.bind("<Right>", self.right)
                self.master.bind("<Up>", self.up)
                self.master.bind("<Down>", self.down)
		
                self.mainloop()
                
	# macht das 4x4 Muster	
        def make_GUI(self):   						
                self.cells = []
                for x in range(4):
                        row = []
                        for y in range (4):
                                cell_frame = tk.Frame(
                                        self.main_grid,
                                        bg=c . EMPTY_CELL_COLOR,
                                        width=150,
                                        height=150
                                )
                                cell_frame.grid(row=x, column=y, padx=5, pady=5)
                                cell_nummber = tk.Label(self.main_grid, bg=c.EMPTY_CELL_COLOR)
                                cell_nummber.grid(row=x, column=y)
                                cell_data = {"frame": cell_frame, "number": cell_nummber}
                                row.append(cell_data)
                        self.cells.append(row)
			
                        
        # fügt zu Beginn des Spiels 2 2er Teiler hinzu
        def start(self):
                self.matrix = [[0] * 4 for _ in range(4)]               

                row = random.randint(0, 3)
                colum = random.randint(0, 3)
                self.matrix[row][colum] = 2
                self.cells[row][colum]["frame"].configure(bg=c.CELL_COLORS[2])
                self.cells[row][colum]["number"].configure(
                        bg=c.CELL_COLORS[2],
                        font=c.CELL_NUMBER_FONT[2],
                        text="2"
                        )
                while(self.matrix[row][colum] != 0):
                        row = random.randint(0, 3)
                        colum = random.randint(0, 3)
                self.matrix[row][colum] = 2
                self.cells[row][colum]["frame"].configure(bg=c.CELL_COLORS[2])
                self.cells[row][colum]["number"].configure(
                        bg=c.CELL_COLORS[2],
                        font=c.CELL_NUMBER_FONT[2],
                        text="2"
                                )
                



        # nimmt alle blöcke um sie alle gleichzeitig zu bewegen
        def stack(self):
                new_matrix = [[0] * 4 for _ in range (4)]
                for x in range(4):
                        fill_position = 0
                        for y in range (4):
                                if self.matrix[x][y] != 0:
                                        new_matrix[x][fill_position] = self.matrix[x][y]
                                        fill_position += 1
                self.matrix = new_matrix
        # kombiniert die werte wenn sie aufeinander treffen und rechnet sie mal 2
        def merge(self):
                for x in range(4):
                        for y in range(3):
                                if self.matrix[x][y] != 0 and self.matrix[x][y] == self.matrix[x][y + 1]:
                                        self.matrix[x][y] *= 2
                                        self.matrix[x][y + 1] = 0
                                        
        # 2 90 grad drehungen
        def two_spin(self):
                new_matrix = []
                for x in range(4):
                        new_matrix.append([])
                        for y in range(4):
                                new_matrix[x].append(self.matrix[x][3 - y])
                self.matrix = new_matrix
        # 1 90 grad drehungen
        def one_spin(self):
                new_matrix = [[0] * 4 for _ in range(4)]
                for x in range(4):
                        for y in range(4):
                                new_matrix[x][y] = self.matrix[y][x]
                self.matrix = new_matrix

        # fügt ein Teil hinzu welches entweder 2 oder 4 ist (indviduel einstellbar)
        def new_tile(self):
                row = random.randint(0, 3)
                colum = random.randint(0, 3)
                while(self.matrix[row][colum] != 0):
                        row = random.randint(0, 3)
                        colum = random.randint(0, 3)
                self.matrix[row][colum] = random.choice([2, 4])
                
        # wie der name schon sagt updatet er das GUI
        def update_gui(self):
                for x in range(4):
                        for y in range(4):
                                cell_value = self.matrix[x][y]
                                if cell_value == 0:
                                        self.cells[x][y]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                                        self.cells[x][y]["number"].configure(bg=c.EMPTY_CELL_COLOR, text="")
                                else:
                                        self.cells[x][y]["frame"].configure(bg=c.CELL_COLORS[cell_value])
                                        self.cells[x][y]["number"].configure(
                                                bg=c.CELL_COLORS[cell_value],
                                                fg=c.CELL_NUMBER_COLORS[cell_value],
                                                font=c.CELL_NUMBER_FONT[cell_value],
                                                text=str(cell_value)
                                                )

        def check_score(self):
                global score
                score = score
               
                
                
                score_frame = tk.Frame(self)                            # schreibt den Score je nach dem welche die höchste Zahl auf dem Feld ist
                score_frame.place(relx=0.5, y=45, anchor="center")
                tk.Label(
                        score_frame,
                        text="Deine Annette-Punkte betragen",
                        font=c.SCORE_LABEL_FONT
                        ).grid(row=0)
                # sucht die höchste Zahl
                if any (2 in row for row in self.matrix):
                        score = 2
                        
                if any (4 in row for row in self.matrix):
                        score = 4
                        
                if any (8 in row for row in self.matrix):
                        score = 8
                        
                if any (16 in row for row in self.matrix):
                        score = 16
                        
                if any (32 in row for row in self.matrix):
                        score = 32
                        
                if any (64 in row for row in self.matrix):
                        score = 64
                        
                if any (128 in row for row in self.matrix):
                        score = 128
                        
                if any (256 in row for row in self.matrix):
                        score = 256
                        
                if any (512 in row for row in self.matrix):
                        score = 512
                        
                if any (1024 in row for row in self.matrix):
                        score = 1024
                        
                if any (2048 in row for row in self.matrix):
                        score = 2048
                # schreibt den score
                self.score_label = tk.Label(score_frame, text=(score) , font=c.SCORE_FONT)
                self.score_label.grid(row=1)
                
                        
                        
        # fragt ab ob noch ein zug auf der X Achse möglich ist
        def move_exist_x(self):
                for x in range(4):
                        for y in range(3):
                                if self.matrix[x][y] == self.matrix[x][y + 1]:
                                        return True
                return False

        # fragt ab ob noch ein zug auf der Y Achse möglich ist
        def move_exist_y(self):
                for x in range(3):
                        for y in range(4):
                                if self.matrix[x][y] == self.matrix[x + 1][y]:
                                        return True
                return False
        
                                
                
        # fragt ab das spiel gewonnen oder verloren ist im Fall Gewonnen muss ein 2048er Teil auf dem Feld sein
        # und im Fall Verloren ist es nicht mehr möglich irgendein Teil zu bewegen
        
        def game_over(self):
                if any (2048 in row for row in self.matrix):
                        game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
                        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
                        tk.Label(
                                game_over_frame,
                                text="Du hast Gewonnen!",
                                bg=c.WINNER_BG,
                                fg=c.GAME_OVER_FONT_COLOR,
                                font=c.GAME_OVER_FONT
                        ).pack()
                elif not any (0 in row for row in self.matrix) and not self.move_exist_x() and not self.move_exist_y():
                        game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
                        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
                        tk.Label(
                                game_over_frame,
                                text="Du hast leider Verloren!",
                                bg=c.LOSER_BG,
                                fg=c.GAME_OVER_FONT_COLOR,
                                font=c.GAME_OVER_FONT
                        ).pack()
                                
                                
                
                
        # ist für die Abfolge der Auführungen zuständig
        def left(self, event):
                self.stack()
                self.merge()
                self.stack()
                self.new_tile()
                self.update_gui()
                self.game_over()
                self.check_score()
                
        def right(self, event):
                self.two_spin()
                self.stack()
                self.merge()
                self.stack()
                self.two_spin()
                self.new_tile()
                self.update_gui()
                self.game_over()
                self.check_score()
                
                
        def up(self, event):
                self.one_spin()
                self.stack()
                self.merge()
                self.stack()
                self.one_spin()
                self.new_tile()
                self.update_gui()
                self.game_over()
                self.check_score()
                
        def down(self, event):
                self.one_spin()
                self.two_spin()
                self.stack()
                self.merge()
                self.stack()
                self.two_spin()
                self.one_spin()
                self.new_tile()
                self.update_gui()
                self.game_over()
                self.check_score()

        

        
# für die endlos Schleife 
if __name__ == "__main__":
        Game()
                                
                
                
                

        






        

        
			
			
				
		
		
