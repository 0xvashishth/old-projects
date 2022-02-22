from tkinter import*
from PIL import ImageTk
from tkinter import ttk,messagebox





class register:
	def __init__(self,root):
		self.root=root
		self.root=root
		self.root.title('Student Registration System')
		self.root.geometry('1350x700+0+0')


		#@@@@@@@@@@@Bg Image
		self.bg=ImageTk.PhotoImage(file='wallpaper\\5.jpg')
		bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

		#=====left image===
		self.left=PhotoImage(file='wallpaper\\11.PNG')
		left=Label(self.root,image=self.left).place(x=70,y=100,width=350,height=550)
		title1=Label(root,text='SHRI K. M. PATEL\nVIDHYAMANDIR, IDAR', font=('times new roman', 20 , 'bold') ).place(x=98,y=110)

		#@@@@@@@@@@@@@REGISTER FRAME############
		frame1=Frame(self.root,bg='white')
		frame1.place(x=420,y=100,width=600,height=550)



		title=Label(frame1,text='REGISTER HERE:-',font=('times new roman',25,'bold'),bg='white',fg='black').place(x=20,y=20)

		#!!!!!!!!!!!!!!!!!!!11111111111111111111111111111111111111111111111111111111111111111111111111111111



		f_name=Label(frame1,text='First Name',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=20,y=100)
		self.txt_fname=Entry(frame1,font=('times new roman',15),bd=5,bg='light gray')
		self.txt_fname.place(x=20,y=130,width=250)


		l_name=Label(frame1,text='Last Name',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=320,y=100)
		self.txt_lname=Entry(frame1,font=('times new roman',15),bd=5,bg='light gray')
		self.txt_lname.place(x=320,y=130,width=250)


		#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

		father_name=Label(frame1,text='Father Name',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=20,y=180)
		self.txt_faname=Entry(frame1,font=('times new roman',15),bd=5,bg='light gray')
		self.txt_faname.place(x=20,y=210,width=250)
		mother_name=Label(frame1,text='Mother Name',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=320,y=180)
		self.txt_moname=Entry(frame1,font=('times new roman',15),bd=5,bg='light gray')
		self.txt_moname.place(x=320,y=210,width=250)

		#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

		
		contact_number=Label(frame1,text='Contact Number',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=20,y=250)
		self.txt_contact=Entry(frame1,font=('times new roman',15),bd=5,bg='light gray')
		self.txt_contact.place(x=20,y=280,width=250)

		GR=Label(frame1,text='Gr No.',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=320,y=250)
		self.txt_GR=Entry(frame1,font=('times new roman',15),bd=5,bg='light gray')
		self.txt_GR.place(x=320,y=280,width=250)



		#4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

		Standerd=Label(frame1,text='Standerd',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=20,y=320)
		self.cmd_std=ttk.Combobox(frame1,font=('times new roman',15),state='readonly',justify=CENTER)
		self.cmd_std['values']=('Select','11 science','12 science')
		self.cmd_std.place(x=20,y=350,width=250)
		self.cmd_std.current(0)

		Division=Label(frame1,text='Division',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=320,y=320)
		self.cmd_div=ttk.Combobox(frame1,font=('times new roman',15),state='readonly',justify=CENTER)
		self.cmd_div['values']=('Select','A','B','C')
		self.cmd_div.place(x=320,y=350,width=250)
		self.cmd_div.current(0)

		#555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555


		Email=Label(frame1,text='Email',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=20,y=390)
		self.txt_email=Entry(frame1,font=('times new roman',15),bd=5,bg='light gray')
		self.txt_email.place(x=20,y=420,width=250)


		Dob=Label(frame1,text='Date Of Birth',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=320,y=390)
		self.txt_Dob=Entry(frame1,font=('times new roman',15),bd=5,bg='light gray')
		self.txt_Dob.place(x=320,y=420,width=250)



		#6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666

		adhar=Label(frame1,text='Adhaar No.',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=20,y=460)
		self.txt_adhar=Entry(frame1,font=('times new roman',15),bd=5,bg='light gray')
		self.txt_adhar.place(x=20,y=490,width=250)

		category=Label(frame1,text='Category',font=('times new roman',15,'bold'),bg='white',fg='black').place(x=320,y=460)
		self.cmd_cat=ttk.Combobox(frame1,font=('times new roman',15),state='readonly',justify=CENTER)
		self.cmd_cat['values']=('Select','General','Gen-Ews','OBC','ST','SC','Minority')
		self.cmd_cat.place(x=320,y=490,width=250)
		self.cmd_cat.current(0)

		#1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		self.var_chk=IntVar()
		chk=Checkbutton(root,text='I Agree The Terms&Condition',cursor='hand2',font=('times new roman',9,'bold'),variable=self.var_chk,onvalue=1,offvalue=0).place(x=150,y=550)

		self.btn_img=PhotoImage(file='Register1.png')
		btn=Button(root,image=self.btn_img,bd=0,cursor='hand2',command=self.register_data).place(x=110,y=590,height=50,width=270)



	
	def register_data(self):
		
		if self.txt_fname.get()=='' or self.txt_faname.get()=='' or self.txt_moname.get()=='' or self.txt_contact.get()=='' or self.txt_GR.get()=='' or self.cmd_std.get()=='' or self.cmd_div.get()=='' or self.txt_email.get()=='' or  self.txt_Dob.get()=='' or self.txt_Dob.get()=='' or  self.txt_adhar.get()=='' or self.cmd_cat.get()=='' or self.txt_lname.get()=='' :
			messagebox.showerror('Error', 'All Fields Are Required!!', parent=self.root)


		elif  self.var_chk.get()==0:
			messagebox.showerror('Error', 'Please Agree Our Terms&Condition', parent=self.root)

		else:
			messagebox.showinfo('Success' , 'Register Successfully' , parent=self.root)
		#print('first name')
		print(self.txt_fname.get(),
		self.txt_lname.get(),
		self.txt_faname.get(),
		self.txt_moname.get(),
		self.txt_contact.get(),
		self.txt_GR.get(),
		self.cmd_std.get(),
		self.cmd_div.get(),
		self.txt_email.get(),
		self.txt_Dob.get(),
		self.txt_adhar.get(),
		self.cmd_cat.get())







root=Tk()
obj=register(root)
root.mainloop()