# This class is the main battle system. It will save the information of the current world so the player can return after the battle has ended

import random as rng
import tkinter as tk

class Battle(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0)

        self.area = tk.Canvas(self, width=master.winfo_width() - 64, height=master.winfo_height() - 64, bg='grey10')
        self.area.create_window(32, 32, anchor='center')

        self.area.update()

        self.update()
    
    def endBattle(self):
        self.destroy()
