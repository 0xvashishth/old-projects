from tkinter import *


def btnclick (numbers):
	global operator
	operator = operator + str(numbers)
	text_input.set(operator)

def btncleardisplay():
	global operator
	operator =''
	text_input.set('')

def btnresultinput():
	global operator
	sumup = str(eval(operator))
	text_input.set(sumup)
	operator = ''


cal = Tk()
cal.title('Calculator By PyCoder')
operator=''
text_input=StringVar()


txtDisplay = Entry(cal, font=('ds-digital' , 25 , 'bold') , textvariable=text_input , bd=30 , insertwidth=4 , bg='white' , fg='red' ,justify='right').grid(columnspan=4)


btn7=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='7' , command = lambda:btnclick(7) , bg='powder blue' ).grid(row=1 , column=0)
btn8=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='8' , command = lambda:btnclick(8) , bg='powder blue' ).grid(row=1 , column=1)
btn9=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='9' , command = lambda:btnclick(9) , bg='powder blue' ).grid(row=1 , column=2)
Division=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='/' , command = lambda:btnclick('/') , bg='powder blue' ).grid(row=1 , column=3)
#************************************************************************************************************************************************************************
btn4=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='4' , command = lambda:btnclick(4) , bg='powder blue' ).grid(row=2 , column=0)
btn5=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='5' , command = lambda:btnclick(5) , bg='powder blue' ).grid(row=2 , column=1)
btn6=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='6' , command = lambda:btnclick(6) , bg='powder blue' ).grid(row=2 , column=2)
multiplection=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='*' , command = lambda:btnclick('*') , bg='powder blue' ).grid(row=2 , column=3)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
btn1=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='1' , command = lambda:btnclick(1) , bg='powder blue' ).grid(row=3 , column=0)
btn2=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='2' , command = lambda:btnclick(2) , bg='powder blue' ).grid(row=3 , column=1)
btn3=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='7' , command = lambda:btnclick(3) , bg='powder blue' ).grid(row=3 , column=2)
minus=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='-' , command = lambda:btnclick('-') , bg='powder blue' ).grid(row=3 , column=3)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
btn0=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='0' , command = lambda:btnclick(0) , bg='powder blue' ).grid(row=4 , column=0)
btnC=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='C' , command = btncleardisplay  , bg='powder blue' ).grid(row=4 , column=1)
result=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='=' , command = btnresultinput , bg='powder blue' ).grid(row=4 , column=2)
addition=Button(cal, padx=16 , bd=8 , fg='red' , font=('arial' , 20 , 'bold') , text='+' , command = lambda:btnclick('+') , bg='powder blue' ).grid(row=4 , column=3)
#!!!!!!!!!!!!****************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


cal.mainloop()