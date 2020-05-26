from tkinter import *
from tkinter import filedialog


window = Tk()

def len():
    file = filedialog.askopenfilename(filetypes = (("All files","*.*"),("Text files","*.txt")))
    print(file)
    print("Len")

def trai():
    print("Trai")

def phai():
    print("Phai")

def xuong():
    Xuongbtn.config(bg="yellow")
    print("Xuong")

fram1 = Frame(window)
fram1.pack()

fram2 = Frame(window)
fram2.pack()

fram3 = Frame(window)
fram3.pack()

Lenbtn = Button(fram1,text="Open", command=len, bg='blue',fg='white')
Lenbtn.pack()

Traibtn = Button(fram2,text="Trai",command=trai, bg='green',fg='white')
Traibtn.pack(side=LEFT)

Phaibtn = Button(fram2,text="Phai",command=phai, bg='red',fg='white')
Phaibtn.pack(side=RIGHT)

Xuongbtn = Button(fram3,text="Xuong",command=xuong, bg='black',fg='white')
Xuongbtn.pack()




window.mainloop()