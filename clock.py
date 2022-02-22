from tkinter import *
from tkinter.ttk import *

from time import strftime
from datetime import*



root1 = Tk()
root1.title('Clock By Vashishth chaudhary')

def time():
	string = strftime('Time : %H:%M:%S:%p \nDate : %D')
	label.config(text=string)
	label.after(1000 , time)

	
label = Label(root1, font =('Ds-Digital' , 100) , background ='yellow', foreground ='red' )
label.pack(anchor ='center')
time()
mainloop()

