from ctypes import windll
from tkinter import Button, Label, Tk
import time
import math
import tkinter

# set gui size and title
window = Tk()
window.title("Clock")
window.geometry("550x200")
window.resizable(1,1)



# sets "sytle" for screen gui
font= ('Times', 68, 'italic')
background = "light blue"
forground= "black"
border = 25
button = Button(text='Switch Clock',fg='Black',bg='light green')
label = Label(window, font=font, bg=background, fg=forground, bd=border) 
label.grid(row=0, column=1)
button.grid(row=3, column=1)

#  displays actual time
def clock(): 
   time_live = time.strftime("%I:%M:%S %p")
   label.config(text=time_live) 
   label.after(200, clock)

# def anolog_clock():

   
clock()
window.mainloop()
