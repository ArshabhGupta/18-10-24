from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x400")

def Handle_Keypress(event):
    print(event.char)
    root.bind("<Key>", Handle_Keypress)

def Handle_Click(event):
    print("The button was clicked")

button = Button(text = "Click Me!")
button.pack()
button.bind("<Button-1>", Handle_Click)
root.mainloop()