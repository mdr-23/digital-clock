""" THE CLOCK REPLIES THE TIME OF THE COMPUTER AND SHOW IT IN THE SCREEN """

from tkinter import *
from time import strftime #this module replies my computer's time

root = Tk() #window
root.title("Digital Clock") #title of the project

def time(): #this function will show the time of the computer
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000, time)

#add styles to the lable widget that will display the clock
lbl = Label(root, font = ("Night Machine", 160), bg="black", fg="#A738D5")

#pack method of tkinter shows the widget in rows or columns
lbl.pack(anchor = "center", fill = "both", expand = 1)

#I call the function
time()


#runs the application
mainloop()