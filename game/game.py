import tkinter as tk
root=tk.Tk()
root.geometry("1000x500")
frame=tk.Frame()
canvas=tk.Canvas(frame)
bg=tk.PhotoImage(file="image\dd.png")
canvas.create_image(0,0,image=bg,anchor="nw")

fruit=tk.PhotoImage(file="image\jj.png")
##call file image---------------
grid=[
        [0,0,0,0,2,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    ]

    ##disply grid ----------------------------------------------------------------------------------
def displayGrid():
    canvas.delete("all")
    canvas.create_image(0,0,image=bg)
    global grid
    x1=50
    x2=90
    y1=50
    y2=90
    for row in grid:
        for col in row:
            if col==1:
                canvas.create_rectangle(x1,y1,x2,y2,fill="red")
            elif col==2:
                canvas.create_image(x2-20,y2-20,image=fruit)
            else:
                canvas.create_rectangle(x1,y1,x2,y2,fill="blue")
            x1=x2
            x2+=40  
        y1=y2
        y2+=40
        x1=50
        x2=90
    ##move left ----------------------------------
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
    ##move right ----------------------------------
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
displayGrid()
##animation-------------------------------
root.bind("<w>",moveLeft)
root.bind("<e>",moveRight)
##---------------------------------
canvas.pack(expand=True,fill="both")
frame.pack

root.mainloop()