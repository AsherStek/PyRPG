# This is the main file for implementing the features we've created. For now it'll be a barebones RPG using the systems as we make them.
# It also will contain our main loop for update and render calls

# Python imports
import time as t
import tkinter as tk

# Our class imports
import window as win
import keyCalls as keys
import player as ply
import world as wr

# Loop Variables
THROTTLE = 10000
MILLION = 1000000
BILLION = 1000000000
lastFpsTime = 0
fps = 0
running = True

# Dictionaries for storing ingame objects for easier access and modification
objects = {}
sprites = {}

# Loop Nanotime method as python does not have a built in nanotime
def nanoTime():
    return ((1000 * t.perf_counter()) / 10000) * 100

# Initialize any of our classes that we need
w = win.Window(640, 640, "PyRPG Example")
kc = keys.KeyCalls()
mp = wr.world(20, 20, 0, 0, 32)
mp.testPrint()

# These methods are here to actually control the game. This is where the actual game logic resides
def update(delta):

    # Anything called here will update every loop. Used for game logic
    pass

def render(delta, canvas):
    for key in objects.values():
        canvas.coords(sprites[key.name], key.x1, key.y1, key.x2, key.y2)

def createObj(entity):
    objects[f'{entity.name}'] = entity

def createSpr(entity, canvas):
    sprites[f'{entity.name}'] = canvas.create_rectangle(entity.x1, entity.y1, entity.x2, entity.y2, fill=entity.color)

# Populate the objects and sprites
createObj(ply.Player(0,0,32,32,"Player", 32, 'red'))
createSpr(objects[f'{"Player"}'], w.can)
objects["Player"].placeInMap(mp)

# This area is used to bind our keys
w.root.bind("<Escape>", lambda e: kc.quitOut(e, w.root))
w.root.bind("<KeyPress-w>", lambda e, p=objects["Player"]: kc.playerMove(e, p))
w.root.bind("<KeyPress-s>", lambda e, p=objects["Player"]: kc.playerMove(e, p))
w.root.bind("<KeyPress-a>", lambda e, p=objects["Player"]: kc.playerMove(e, p))
w.root.bind("<KeyPress-d>", lambda e, p=objects["Player"]: kc.playerMove(e, p))

while running:

    # Essential loop variables
    lastLoopTime = nanoTime()
    TARGET_FPS = 15
    OPTIMAL_TIME = BILLION / TARGET_FPS

    # I contain everything inside a try loop to stop the program from causing a stack trace error on close
    try:

        # This series of updates is to find out has fast the game is executing and to throttle it to the speed that we want
        now = nanoTime()
        updateLength = now - lastLoopTime
        lastLoopTime = now
        delta = float(updateLength / OPTIMAL_TIME)
        lastFpsTime += (updateLength * BILLION)
        fps += 1
        if (lastFpsTime >= BILLION / THROTTLE):
            lastFpsTime = 0
            fps = 0

        # Update and Render calls
        update(delta)
        render(delta, w.can)
        
        # Determin how long to have the program sleep to maintain the proper execution speed
        sleepFor = int((lastLoopTime - nanoTime() + OPTIMAL_TIME) / MILLION)
        if (sleepFor < 0):
            sleepFor *= -1
        t.sleep(1/1/sleepFor)

        # Finally we update the main window which allows all changes that have occured in this loop to be happen
        w.updateRoot()

    # This happens when you either close the program or it crashes.
    except tk.TclError:
        print("The program was either closed or crashed. Check previous prints for info")
        running = False
