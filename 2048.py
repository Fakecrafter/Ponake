import tkinter as tk
import color as c
import random




global score
score = 0

global Spiel
Spiel = 1

class Board (tk.Frame): 						# erstellt das Fenster für das Spiel
        def __init__(self):
                tk.Frame.__init__(self)
                self.grid()
                self.master.title("2048")

                self.main_grid = tk.Frame(
                        self, bg=c .GRID_COLOR, bd=3, width=600, height=600
                        )
			
                self.main_grid.grid(pady=(100, 0))
                self.make_GUI()
		
                self.mainloop()
		
        def make_GUI(self):   						# macht das 4x4 Muster
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
			
                        score_frame = tk.Frame(self)                    # schreibt den Score
                        score_frame.place(relx=0.5, y=45, anchor="center")
                        tk.Label(
                                score_frame,
                                text="Deine Annette-Punkte betragen",
                                font=c.SCORE_LABEL_FONT
                        ).grid(row=0)
                        
                        self.score_label = tk.Label(score_frame, text=(score) , font=c.SCORE_FONT)
                        self.score_label.grid(row=1)


        
        #def spawn_tile(self):                           #lässt nach jedem zug ein neues Teil spawnen
                row = random.randint(0, 3)
                colum = random.randint(0, 3)
                while(self.matrix[row][colum] !=0):
                        row = random.randint(0, 3)
                        colum = random.randint(0, 3)
                self.matrix[row][colum] = random.choice([2, 4])

        def spawn_tile(self):  						
               

        

        def update_gui(self):
                for x in range(4):
                        for y in range(4):
                                cell_value = self.matrix[x][y]
                                if cell_value == 0:
                                        self.cell[x][y]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                                        self.cell[x][y]["number"].configure(bg=c.EMPTY_CELL_COLOR, text="")
                                else:
                                        self.cell[x][y]["frame"].configure(bg=c.EMPTY_CELL_COLOR[cell_value])
                                        self.cell[x][y]["frame"].configure
                                        (
                                                bg==c.CELL_COLORS[cell_value],
                                                fg==c.CELL_NUMBER_COLORS[cell_value],
                                                font==c.CELL_NUMBER_FONT[cell_value],
                                                text==str(cell_value)
                                                )
                self.score_lable.configure(text=self.score)
                self.update_idletast()

        
Board()
spawn_tile()



        

        
			
			
				
		
		
