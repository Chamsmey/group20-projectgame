import tkinter as tk
root=tk.Tk()
root.geometry("600x600")
frame=tk.Frame()
frame.master.title("Game eater")
canvas=tk.Canvas(frame)
bg=tk.PhotoImage(file="image\dd.png")
# bg_label=tk.Label(root,image=bg)
# bg_label.place(relwidth=1,relheight=1)
canvas.create_image(0,0,image=bg,anchor="nw")
canvas.create_rectangle(0,0,100,100 ,fill="red")
# # def show():

button=tk.Button(canvas,text="click me if you can")
button.pack(ipadx=0,ipady=5,expand=True)

canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()

