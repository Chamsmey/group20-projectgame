# Import module 
from tkinter import *
# Create object
root = Tk()
# Adjust size 
root.geometry("1000x600")
# Add image file
bg = PhotoImage(file = "image/dd.png")
# Create Canvas
canvas1 = Canvas( root, width = 1000,height = 500)
canvas1.pack(fill = "both", expand = True)
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
# Add Text
canvas1.create_text( 500, 50, text = "Welcome",font=("",50))
# Create Buttons
button1 = Button( root, text = "Exit",font=("",15))
button2 = Button( root, text = "Reset",font=("",15))
button3 = Button( root, text = "Start",font=("",15))
# Display Buttons
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
    global grid
    canvas1.delete("all")
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    button1_canvas = canvas1.create_window( 20, 550, anchor = "nw",window = button1)
    button2_canvas = canvas1.create_window( 500, 550,anchor = "nw",window = button2)
  
    button3_canvas = canvas1.create_window( 920, 550, anchor = "nw",window = button3)
    x1=50
    x2=90
    y1=50
    y2=90
    for row in grid:
        for col in row:
            if col==1:
                canvas1.create_rectangle(x1,y1,x2,y2,fill="red")
            else:
                canvas1.create_rectangle(x1,y1,x2,y2,fill="blue")
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
def Start(event):
    displayGrid()
root.bind("<w>",moveLeft)
root.bind("<e>",moveRight)
canvas1.tag_bind("buttonStart","<Button-1>",Start)
button1_canvas = canvas1.create_window( 20, 550, anchor = "nw",window = button1)
button2_canvas = canvas1.create_window( 500, 550,anchor = "nw",window = button2)
  
button3_canvas = canvas1.create_window( 920, 550, anchor = "nw",window = button3)
  
# Execute tkinter
root.mainloop()

