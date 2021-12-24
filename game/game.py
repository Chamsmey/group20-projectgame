import tkinter as tk
import winsound
from random import choice, randrange
root=tk.Tk()
root.geometry("758x650")
frame=tk.Frame()
frame.master.title("Game eater")
canvasImage=tk.Canvas(root,width=100,height=100)
bg=tk.PhotoImage(file="image\dd.png")
lives=tk.PhotoImage(file="image\live.png")

def Disply():
    moveFruit()
canvas=tk.Canvas(frame,width=500,height=550)
canvas.create_image(0,0,image=bg,anchor="nw")
x=20
y=20
text=canvas.create_text(40,50,text=" Score:",font=("",15))
for i in range(5):
    canvas.create_image(x,y,image=lives)
    x+=30
    # y+=20
##button----------------------------------------------------

buttonPlay=tk.Button(frame,text="Play",bg="blue",fg="white",width=20,height=0,command=Disply)
buttonExit=tk.Button(frame,text="Exit",bg="blue",width=5,height=0,command=root.destroy)
##call file image---------------

##global variable------------------
score=0
grid=[
        [0,3,0,0,4,0,0,0,3,0,4,0,0,3,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    ]

    ##disply grid----------------------------------------------------------------------------------
def displayGrid():
    canvas.delete("all")
    global grid,positionfruit,  score
    canvas.create_image(0,0,image=bg,anchor="nw")
    x=20
    y=20
    text=canvas.create_text(40,50,text=" Score:"+str(score),font=("",15))
    for i in range(5):
        canvas.create_image(x,y,image=lives)
        x+=30
    # canvas.create_image(width=100,height=100,image=bg)
    
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
            
            elif col==4:
                canvas.create_rectangle(x1,y1,x2,y2,fill="green")
            
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
    displayGrid()
##move food ==------------------------------------
def moveFruit():
    
    global grid,score
    Fruitgrid=[
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row<len(grid)-1:
                if (grid[row][col]==3) and (grid[row+1][col]==1):
                    grid[row][col]=0
                    Fruitgrid[row+1][col]=1
                    score+=1
                    
                elif (grid[row][col]==3) and (grid[row+1][col]!=1):
                    grid[row][col]=0
                    Fruitgrid[row+1][col]=3
                elif (grid[row][col]==4) and (grid[row+1][col]!=1):
                    grid[row][col]=0
                    Fruitgrid[row+1][col]=4
                elif (grid[row][col]==4) and (grid[row+1][col]==1):
                    score-=1
                    Fruitgrid[row+1][col]=4
            elif (grid[row][col]==1):
                Fruitgrid[row][col]=1
    grid=Fruitgrid    
        
    displayGrid()  
    canvas.after(1000,lambda:moveFruit())    
    
##move left character----------------------------------
def moveLeft(event):
    global grid,score
    stop=False
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col]==1 ) and (grid[row][col-1]==3):
                score+=1
            elif (grid[row][col]==1 ) and (grid[row][col-1]==4):
                score-=1
            if (grid[row][col]==1 ) and (not stop) and (col>0):
                grid[row][col]=0
                grid[row][col-1]=1
                stop=True
    displayGrid()
##move right character----------------------------------
def moveRight(event):

    global grid,score
    stop=False
    for row in range(len(grid)):
        for col in range(len(grid[row])-1):
            if (grid[row][col]==1 ) and (grid[row][col+1]==3):
                score+=1
            if (grid[row][col]==1 ) and (grid[row][col+1]==4):
                score-=1
            if (grid[row][col]==1 ) and (not stop) :
                grid[row][col]=0
                grid[row][col+1]=1
                stop=True
    displayGrid()   
    winsound.PlaySound("sound\eat.wav",winsound.SND_FILENAME)
##call function-----------

##animation-------------------------------
root.bind("<Left>",moveLeft)
root.bind("<Right>",moveRight)
##---------------------------------
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
buttonPlay.pack()
buttonExit.pack()
root.mainloop()