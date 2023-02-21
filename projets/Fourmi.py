from tkinter import *

SIDE = 1000
WIDTH = SIDE
HEIGHT = SIDE
DIM = 95
UNIT = SIDE // DIM
DELAY = 1
COLOR_ON = 'gray30'
COLOR_OFF = 'LightSteelBlue1'


def draw_square(i, j):
    x, y = j * UNIT, i * UNIT
    square = cnv.create_rectangle((x, y), (x + UNIT, y + UNIT),
                                  fill=COLOR_ON,
                                  outline='')
    return square


def draw(pos, drn, items):
    (ii, jj), ndrn = bouger(pos, drn, items)
    i, j = pos
    square = items[i][j]

    if square == 0:
        square = draw_square(i, j)
        items[i][j] = square
    else:
        cnv.delete(square)
        items[i][j] = 0

    return (ii, jj), ndrn


def bouger(pos, drn, items):
    i, j = pos

    if items[i][j] == 0:
        if drn == "N":
            r = (i, j + 1), "E"
        elif drn == "S":
            r = (i, j - 1), "W"
        elif drn == "E":
            r = (i + 1, j), "S"
        elif drn == "W":
            r = (i - 1, j), "N"
    else:
        if drn == "S":
            r = (i, j + 1), "E"
        elif drn == "N":
            r = (i, j - 1), "W"
        elif drn == "W":
            r = (i + 1, j), "S"
        elif drn == "E":
            r = (i - 1, j), "N"
    return r


def anim():
    global pos, drn
    pos, drn = draw(pos, drn, items)
    root.after(DELAY, anim)


root = Tk()
cnv = Canvas(root, width=WIDTH, height=HEIGHT, background=COLOR_OFF)
cnv.pack(side=LEFT)

nwidth = WIDTH // UNIT
nheight = HEIGHT // UNIT

items = [[0] * nwidth for _ in range(nheight)]
pos = (nheight // 2-10, nwidth // 2+19)
drn = "N"
anim()
print(DIM, nwidth, nheight)

root.mainloop()