'''
Tạo giao diện cơ bản
nhập text từ cmd hiện lên TK
dung kỹ thuật phân luồng  threading
'''
from tkinter import *
#chia luong du lieu
import threading

window=Tk()

myLabel1 = Label(window,text = "Hello!")
myLabel1.pack(side=LEFT)
myLabel2 = Label(window,text = "Xin chao!")
myLabel2.pack(side=RIGHT)

def setText():
	while(True):
		content = str(input("Nhap text: "))
		myLabel1.config(text=content)

setTextThr = threading.Thread(target=setText)
setTextThr.start()

#doi text sau 1 khaong thoi gian
#window.after(500,setText)

window.mainloop()