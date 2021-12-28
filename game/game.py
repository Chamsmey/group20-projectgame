import tkinter as tk
import winsound
from random import choice, randrange
root=tk.Tk()
root.geometry("758x600")
frame=tk.Frame(root,bg="red")
frame.master.title("Game eater")
canvas=tk.Canvas(frame,width=100,height=100)
bg=tk.PhotoImage(file="image\grounde.png")
bg2=tk.PhotoImage(file="image\Pro.png")
canvas=tk.Canvas(frame,width=500,height=550)

def play():
    global isPlay 
    isPlay=True
    displayGrid()
    global buttonPlay
    moveFruit()
    
##button----------------------------------------------------

##global variable------------------
isPlay=False
score=0
lives=5
grid=[
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0,0]
    ]
##disply grid----------------------------------------------------------------------------------
def displayGrid():
    canvas.delete("all")
    global grid,positionfruit,  score ,lives ,isPlay
    ##-bg-------------------------------------------------------------------------------------------
    if not isPlay:
        canvas.create_image(0,0,image=bg2,anchor="nw")
        canvas.create_text(350,100,text="Welcome to the best eater",font=("",30),fill="white")
        buttonPlay=tk.Button(canvas,text="Play",bg="#64ffda",bd=1,fg="white",font=("",15),padx=10,pady=0,width=5,height=0,command=play)
        buttonExit=tk.Button(canvas,text="Exit",bg="#64ffda",bd=1,fg="white",font=("",15),padx=10,pady=0,width=5,height=0,command=root.destroy)
        buttonExit.pack(side="bottom")
        buttonPlay.pack(side="bottom")
    else:
        canvas.create_image(0,0,image=bg,anchor="nw")
        ##--score--------------------------------------
        text=canvas.create_text(40,50,text=" Score:"+str(score),font=("",15))
        
        ##grid--------------------
        x1=100
        x2=150
        y1=100
        y2=150
        for row in grid:
            for col in row:
                canvas.create_image(x2-25,y2-25,image=wall)
                if col==1:
                    canvas.create_image(x2-25,y2-25,image=robot)
                elif col==4:
                    canvas.create_image(x2-25,y2-25,image=fruits[0])
                elif col==5:
                    canvas.create_image(x2-25,y2-25,image=fruits[1])
                elif col==6:
                    canvas.create_image(x2-25,y2-25,image=fruits[2])
                elif col==7:
                    canvas.create_image(x2-25,y2-25,image=fruits[3])
                elif col==8:
                    canvas.create_image(x2-25,y2-25,image=fruits[4])
                elif col==9:
                    canvas.create_image(x2-25,y2-25,image=fruits[5])
                elif col==10:
                    canvas.create_image(x2-25,y2-25,image=fruits[6])
                elif col==11:
                    canvas.create_image(x2-25,y2-25,image=fruits[7])
                elif col==3:
                    canvas.create_image(x2-25,y2-25,image=bomb)
                x1=x2
                x2+=50  
            y1=y2
            y2+=50
            x1=100
            x2=150

        ## lives -------------------
        x=20
        y=20
        for i in range(lives):
            canvas.create_image(x,y,image=heart)
            x+=30
    ##----------Button--------------------------
    
##rendom----------------------------------------
def ramdomFruit():
    global grid
    enemys=[3,4,5,6,7,8,9,10,11]
    enemy=choice(enemys)
    posiF=randrange(0,10)
    grid[0][posiF]=enemy          
    print(posiF)
    displayGrid()
##move fruit ==------------------------------------
def moveFruit():
    global grid,score ,lives, isPlay
    
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
    time=1000
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if score < 10:
                time=500
            elif score<20:
                time=400
            elif score<60:
                time=300
            elif score < 90:
                time=200
            elif score < 100:
                time =100
            elif score < 150:
                time = 50
            else:
                time=25 
            if row<len(grid)-1:
                if (grid[row][col]==3) and (grid[row+1][col]==1):
                    grid[row][col]=0
                    Fruitgrid[row+1][col]=1
                    lives-=1
                elif (grid[row][col]!=3) and (grid[row][col]!=0) and (grid[row+1][col]==1):
                    score+=1
                elif (grid[row][col]==3) and (grid[row+1][col]!=1):
                    grid[row][col]=0
                    Fruitgrid[row+1][col]=3
                elif (grid[row][col]==4) and (grid[row+1][col]!=1):
                    grid[row][col]=0
                    Fruitgrid[row+1][col]=4
                elif (grid[row][col]==5) and (grid[row+1][col]!=1):
                    Fruitgrid[row+1][col]=5
                elif (grid[row][col]==6) and (grid[row+1][col]!=1):
                    Fruitgrid[row+1][col]=6
                elif (grid[row][col]==7) and (grid[row+1][col]!=1):
                    Fruitgrid[row+1][col]=7
                elif (grid[row][col]==8) and (grid[row+1][col]!=1):
                    Fruitgrid[row+1][col]=8
                elif (grid[row][col]==9) and (grid[row+1][col]!=1):
                    Fruitgrid[row+1][col]=9
                elif (grid[row][col]==10) and (grid[row+1][col]!=1):
                    Fruitgrid[row+1][col]=10
                elif (grid[row][col]==11) and (grid[row+1][col]!=1):
                    Fruitgrid[row+1][col]=11
            elif( grid[row][col]==1):
                Fruitgrid[row][col]=1
    grid=Fruitgrid   
    displayGrid()
    canvas.after(time,lambda:moveFruit()) 
    canvas.after(5000,lambda:ramdomFruit())    
##movecharacter----------------------------------
def moveChar(char):
    global grid,score, lives
    stop=False
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (col<len(grid[row])-1):
                if (grid[row][col]==1 ) and (grid[row][col+1]!=3) and (grid[row][col+1]!=0):
                    score+=1
                elif (grid[row][col]==1 ) and (grid[row][col+1]==3):
                    lives-=1
                else:
                    if (grid[row][col]==1 ) and (grid[row][col-1]!=3) and (grid[row][col-1]!=0):
                        score+=1
                    elif (grid[row][col]==1 ) and (grid[row][col-1]==3):
                        lives-=1
            if (grid[row][col]==1 ) and (not stop) and (col>0) and (char==-1):
                grid[row][col]=0
                grid[row][col-1]=1
                stop=True
            if (grid[row][col]==1 ) and (not stop) and (col<len(grid[row])-1) and (char==1):
                grid[row][col]=0
                grid[row][col+1]=1
                stop=True
    displayGrid()
##move right character----------------------------------
def moveLeft(event):
    moveChar(-1)
def moveRight(event):
    moveChar(1)
##call function------------------------------------------
displayGrid()
##Event-------------------------------
root.bind("<Left>",moveLeft)
root.bind("<Right>",moveRight)
##------------------------------------
wall=tk.PhotoImage(file="image\wall.png")
heart=tk.PhotoImage(file="image\live.png")
fruit1=tk.PhotoImage(file="icons\lemon.png")
fruit2=tk.PhotoImage(file="icons\onion.png")
fruit3=tk.PhotoImage(file="icons\pear.png")
fruit4=tk.PhotoImage(file="icons\plum.png")
fruit5=tk.PhotoImage(file="icons\mango.png")
fruit6=tk.PhotoImage(file="icons\orange-juice.png")
fruit7=tk.PhotoImage(file="icons\lime.png")
fruit8=tk.PhotoImage(file="icons\strawberry.png")
fruit9=tk.PhotoImage(file="icons\grapes.png")
fruits=[fruit1,fruit2,fruit3,fruit4,fruit5,fruit6,fruit7,fruit8,fruit9]
bomb=tk.PhotoImage(file="icons\omb.png")
char=tk.PhotoImage(file="icons\cutt.png")
robot=tk.PhotoImage(file="image\jing.png")
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()