from tkinter import *
#chia luong du lieu
import threading
from tkinter import filedialog

#https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Setting-window-size

window = Tk()
window.geometry("1200x700+50+50")
window.title("Do an From")

def printt():
	print("Demo tkinter")

def exit1():
	exit()

myLb1=Label(window, text="Registrtion From:", relief="solid", width=20, font=("arial",19,"bold"))
myLb1.place(x=90,y=53)

myLb2=Label(window, text="First name:",  width=20, font=("arial",10,"bold"))
myLb2.place(x=80,y=130)

myLb3=Label(window, text="Last name:",  width=20, font=("arial",10,"bold"))
myLb3.place(x=80,y=160)

btn1 = Button(window,text="login", width=12,bg="brown",fg="white",command=printt)
btn1.place(x=100, y=210)

btn2 = Button(window,text="Quit", width=12,bg="brown",fg="white",command=exit)
btn2.place(x=300, y=210)
window.mainloop()