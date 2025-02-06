from tkinter import *



for i in range(4):
    for j in range(3):
        btn = Button (text=f"{i}{j}")
        btn.grid(row=i, column=j)

mainloop()