import tkinter as tk
from random import choice, randrange
root=tk.Tk()
root.geometry("758x650")
frame=tk.Frame()
frame.master.title("Game eater")
canvas=tk.Canvas(frame)

character=canvas.create_rectangle(100,300,150,350,fill="blue")
##call function-----------

x=0
y=0

enemy=canvas.create_oval(10,10,20,20,fill="red")
def moveEnemy():
    global x,y
    canvas.move(enemy,x,y+5)
    canvas.after(100,lambda:moveEnemy())
moveEnemy()
def moveLeft(evnet):
    global x,y
    canvas.move(character,x-10,y)
def moveRight(event):
    global x,y
    canvas.move(character,x+10,y)
##animation-------------------------------
root.bind("<Left>",moveLeft)
root.bind("<Right>",moveRight)
##---------------------------------
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()

