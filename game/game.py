import tkinter as tk
from random import choice, randrange
root=tk.Tk()
root.geometry("758x650")
frame=tk.Frame()
frame.master.title("Game eater")
canvasImage=tk.Canvas(root,width=100,height=100)
canvas=tk.Canvas(root,width=500,height=550)
bg=tk.PhotoImage(file="image\dd.png")
lives=tk.PhotoImage(file="image\live.png")
canvas.create_image(0,0,image=bg,anchor="nw")
x=20
y=20
text=canvas.create_text(40,50,text=" Score:",font=("",15))
for i in range(5):
    canvas.create_image(x,y,image=lives)
    x+=30
    # y+=20
def Disply():
    displayGrid()
##button----------------------------------------------------

buttonPlay=tk.Button(frame,text="Play",bg="blue",width=5,height=0,command=Disply)
buttonExit=tk.Button(frame,text="Exit",bg="blue",width=5,height=0,command=root.destroy)
##call file image---------------


grid=[
        [0,0,0,0,2,0,0,2,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    ]

    ##disply grid----------------------------------------------------------------------------------
def displayGrid():
    canvas.delete("all")
    
    canvas.create_image(0,0,image=bg,anchor="nw")
    x=20
    y=20
    text=canvas.create_text(40,50,text=" Score:",font=("",15))
    for i in range(5):
        canvas.create_image(x,y,image=lives)
        x+=30
    # canvas.create_image(width=100,height=100,image=bg)
    global grid,positionfruit
    
    x1=3
    x2=53
    y1=100
    y2=150
    for row in grid:
        for col in row:
            if col==1:
                canvas.create_rectangle(x1,y1,x2,y2,fill="red")
        
            # elif col==2:
            #     canvas.create_image(x2-25,y2-25,image=fruit)
            elif col==3:
                canvas.create_rectangle(x1,y1,x2,y2,fill="Blue")
            
            else:
                canvas.create_rectangle(x1,y1,x2,y2,fill="")
            x1=x2
            x2+=50  
        y1=y2
        y2+=50
        x1=3
        x2=53
        

##rendom----------------------------------------
def ramdomFruit():
    global grid
    posiF=randrange(0,14)
    grid[0][posiF]=3
                
    print(posiF)
##move food ==
ramdomFruit()
def moveFruit():
    global grid
    stopMove=False
    for row in range(len(grid)-1):
        for col in range(len(grid[row])):
            if (grid[row][col]==3) and (not stopMove):
                grid[row][col]=0
                grid[row+1][col]=3
                stopMove=True
    displayGrid()
    canvas.after(2000,lambda:moveFruit())    


    
    
##move left character----------------------------------
def moveLeft(event):
    global grid
    stop=False
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col]==1 ) and (not stop) and (col>0):
                grid[row][col]=0
                grid[row][col-1]=1
                stop=True
    displayGrid()
##move right character----------------------------------
def moveRight(event):

    global grid
    stop=False
    for row in range(len(grid)):
        for col in range(len(grid[row])-1):
            if (grid[row][col]==1 ) and (not stop) :
                grid[row][col]=0
                grid[row][col+1]=1
                stop=True
    displayGrid()
##call function-----------
moveFruit()
##animation-------------------------------
root.bind("<Left>",moveLeft)
root.bind("<Right>",moveRight)
##---------------------------------
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
buttonPlay.pack()
buttonExit.pack()

root.mainloop()