from tkinter import*

def hienthi():
    Label(window,text=entName.get() + "\n"+ entNum.get(),font="Times 24 bold",fg="blue").pack()


window=Tk()
entName=Entry(window,font="Times 24 bold")
entName.pack()
entName.focus()
entNum=Entry(window,font="Times 24 bold")
entNum.pack()

showBtn=Button(window,text="Enter", font="Times 28 bold",command=hienthi)
showBtn.pack()

window.mainloop()