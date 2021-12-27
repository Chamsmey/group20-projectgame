import tkinter as tk
import winsound
from random import choice, randrange
root=tk.Tk()
root.geometry("758x600")
frame=tk.Frame()
frame.master.title("Game eater")
canvas=tk.Canvas(frame,width=100,height=100)
canvasButton=tk.Canvas(canvas,width=100,height=100)
bg=tk.PhotoImage(file="image\grounds.png")
lives=tk.PhotoImage(file="image\live.png")

def Disply():
    moveFruit()
canvas=tk.Canvas(frame,width=500,height=550)
canvas.create_image(0,0,image=bg,anchor="nw")
img=canvasButton.create_rectangle(200,200,250,250,fill="red")
x=20
y=20
text=canvas.create_text(40,50,text=" Score:",font=("",15))
for i in range(5):
    canvas.create_image(x,y,image=lives)
    x+=30
    # y+=20
##button----------------------------------------------------

buttonPlay=tk.Button(canvas,text="Play",bg="blue",fg="white",width=5,height=0,command=Disply)
buttonExit=tk.Button(canvas,text="Exit",bg="blue",width=5,height=0,command=root.destroy)
##call file image---------------

##global variable------------------
score=0
grid=[
        [0,3,0,0,4,0,0,4,3,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0,0]
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
    
    x1=100
    x2=150
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
        x1=100
        x2=150
##rendom----------------------------------------
def ramdomFruit():
    global grid
    enemys=[3,4]
    enemy=choice(enemys)
    posiF=randrange(0,10)

    grid[0][posiF]=enemy          
    print(posiF)
    displayGrid()
##move food ==------------------------------------
def moveFruit():
    global grid,score
    time=1000
    messagelovel=""
    Fruitgrid=[
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
    
    ]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if score < 10:
                time=500
            elif score<20:
                time=400
                messagelovel="Level-2"
            elif score<60:
                time=300
                messagelovel="Level-3"
            elif score < 90:
                time=200
                messagelovel="Level-4"
            elif score < 100:
                time =100
                messagelovel="Level-5"
            else:
                time=50
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
            elif( grid[row][col]==1):
                Fruitgrid[row][col]=1
    grid=Fruitgrid    
    displayGrid()  
    canvas.after(time,lambda:moveFruit())    
    canvas.after(5000,lambda:ramdomFruit())    
##move left character--------------cl--------------------
def moveChar(char):
    global grid,score
    stop=False
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col]==1 ) and (grid[row][col-1]==3):
                score+=1
            elif (grid[row][col]==1 ) and (grid[row][col-1]==4):
                score-=1
            if (grid[row][col]==1 ) and (not stop) and (col>0) and char==-1:
                grid[row][col]=0
                grid[row][col-1]=1
                stop=True
            elif (grid[row][col]==1 ) and (not stop) and (col<len(grid[row])-1) and char==1:
                grid[row][col]=0
                grid[row][col+1]=1
                stop=True
    displayGrid()        
def moveLeft(event):
    moveChar(-1)
##move right character----------------------------------
def moveRight(event):
    moveChar(1)
##call function-----------
##animation-------------------------------
root.bind("<Left>",moveLeft)
root.bind("<Right>",moveRight)
##---------------------------------
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
buttonPlay.pack(side="bottom")
buttonExit.pack(side="bottom")
root.mainloop()