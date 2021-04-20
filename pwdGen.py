from tkinter import *
import random,string


root=Tk()

root.option_add('*Font','Times 10')
root.geometry("380x280")
root.title("pwdGen")

#Introduction Text
title=StringVar()
label=Label(root,textvariable=title).pack()
title.set("Strength of the p4$$w0rD:\n")

#button definition
def selection():
	selection=choice.get()

choice=IntVar()
R1=Radiobutton(root,text="WEAK",variable=choice,value=1,command=selection).pack(anchor=CENTER)
R2=Radiobutton(root,text="MEDIUM",variable=choice,value=2,command=selection).pack(anchor=CENTER)
R3=Radiobutton(root,text="STRONG",variable=choice,value=3,command=selection).pack(anchor=CENTER)

labelchoice=Label(root)
labelchoice.pack()

#Password Length
lenlabel=StringVar()
lenlabel.set("p4$$w0rD Length:")
lentitle=Label(root,textvariable=lenlabel).pack()

val=IntVar()
spinlength=Spinbox(root,from_=9,to_=27,textvariable=val,width=13).pack()


#Callback Function
def callback():
	lsum.config(text=passgen())

passgenButton=Button(root,text="Generate Password",background="blue",fg="white",bd=10,height=2,command=callback,pady=5)
passgenButton.pack()
#passgenButton.grid(column=5, row=5)
password=str(callback)

lsum=Label(root,text="")
lsum.pack(side=BOTTOM)

############Password Generation Logic
weak = string.ascii_uppercase + string.ascii_lowercase				#only letters
medium = string.ascii_uppercase + string.ascii_lowercase + string.digits	#letters and digits
symbols="""'~`!@#$%^&*()_+={}[]\|;:,/?<>."""					#letters, digits and symbols
strong=weak+medium+symbols


#Password Genaration Function
def passgen():
	if choice.get()==1:
		return"".join(random.sample(weak,val.get()))
	elif choice.get()==2:
		return"".join(random.sample(medium,val.get()))
	elif choice.get()==3:
		return"".join(random.sample(strong,val.get()))


root.mainloop()
	
