# Circular Motion Animation
# Rotating Balls Animation

import math
import time
import tkinter as tk

intervalTime = 40
balls = 8
maxstep = 64

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
step = 0
start_time = time.time()

def animateWorld():
    canvas.delete("all")  # Clear canvas before drawing
    createBase()
    global step
    elapsed_time = time.time() - start_time
    step = int((elapsed_time * 1000 / intervalTime) % maxstep)
    centerX = canvas.winfo_width() / 2 + 115 * math.cos(step * 2 / maxstep * math.pi)
    centerY = canvas.winfo_height() / 2 + 115 * math.sin(step * 2 / maxstep * math.pi)

    for i in range(balls):
        drawCircle(centerX + 115 * math.cos((i * 2 / balls - step * 2 / maxstep) * math.pi),
                   centerY + 115 * math.sin((i * 2 / balls - step * 2 / maxstep) * math.pi), 10, '#FFFFFF')

    root.after(intervalTime, animateWorld)

def createBase():
    drawCircle(canvas.winfo_width() / 2, canvas.winfo_height() / 2, 240, '#000000')
    for i in range(balls * 2):
        drawLine(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                 canvas.winfo_width() / 2 + 240 * math.cos(i / balls * math.pi),
                 canvas.winfo_height() / 2 + 240 * math.sin(i / balls * math.pi), '#FFFFFF')

def drawLine(x1, y1, x2, y2, c):
    canvas.create_line(x1, y1, x2, y2, width=3, fill=c)

def drawCircle(x, y, r, c):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=c)

animateWorld()
root.mainloop()
