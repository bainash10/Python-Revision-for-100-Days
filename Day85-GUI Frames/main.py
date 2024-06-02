# frame = a rectangular container to group and hold widgets

from tkinter import *

window=Tk()

frame=Frame(window,bg="green",bd=5,relief=RAISED)
frame.pack(side=BOTTOM)   
# frame.place(x=100,y=100)   #--->giving coordinates


button=Button(frame,text="W",font=("Consolas",25),width=3)
button.pack(side=TOP)

#In short form
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

window.mainloop()