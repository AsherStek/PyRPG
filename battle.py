# This class is the main battle system. It will save the information of the current world so the player can return after the battle has ended

import random as rng
import tkinter as tk

class Battle(tk.Frame):
    def __init__(self, master, width, height):
        super().__init__(master=master, width=width, height=height)
        self.grid(row=0, column=0)

        print(f"Width: {width} Height: {height}")

        self.area = tk.Canvas(self, width=width, height=height, bg='black')
        self.area.create_window(32, 32, anchor='center')
        self.area.grid(row=0, column=0)

        self.area.update()

        self.update()
    
    def endBattle(self):
        self.destroy()
