from tkinter import *
import sys
import time
# font.families

def timer():
    curr_time=time.strftime("%H:%M:%S")
    digital_clock.config(text=curr_time)
    digital_clock.after(300,timer)

root=Tk()
root.title("Digital Clock")
root.geometry("348x100")
root.maxsize(width="348",height="100")
root.minsize(width="348",height="100")
digital_clock = Label(root,font=('courier',50,"bold","italic"),bg="black",foreground="white")
digital_clock.grid(padx=10,pady=10)
timer()

root.mainloop()
