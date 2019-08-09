# The GUI library. I'm using Tkinter as I know it best and it's cross platform
import tkinter as tk

class Window:

    # When creating a window we pass in the dimensions and the name of the window then create the window and get focus
    def __init__(self, width, height, title):

        # Save the variables for later use
        self.width = width
        self.height = height
        self.title = title

        # Create the window and matching canvas
        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(0,0)
        self.root.title(title)
        self.can = tk.Canvas(self.root, width=self.width, height=self.height, bg='grey80')

        # Fit the canvas onto window
        self.can.grid(row=0, column=0)

        # Focus onto the window
        self.can.focus_set()

    # This method is used to call updates to the current canvas
    def updateCanvas(self):
        self.can.update()

    # This method is used to call updates to the main window
    def updateRoot(self):
        self.root.update_idletasks()
        self.root.update()

    
