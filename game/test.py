import tkinter as tk
# import tkMessageBox

# import tkMessageBox
# import Tkinter

top = tk.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = tk.Button(top, text ="Hello", command = helloCallBack)

B.pack()
B.place( relx=1,rely=1,relheight=100, relwidth=100)
top.mainloop()