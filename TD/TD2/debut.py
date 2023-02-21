msg = "hello world"
print(msg.capitalize())

import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Tk(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
tk.create_line(x0, y, x1, y)
tk.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
tk.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
tk.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
    # Fin de votre code

root.grid()
root.mainloop()