from tkinter import *


window=Tk()
#tieu de
window.title("Grid view")
#kich thuong
#window.configure(width=500, height=600)
#window.geometry("500x600+0+50")
#khongthay doi kich thuoc
window.resizable(width=False,height=False)
#kich thuoc theo man hinh
#lay kich thuoc man hifnh
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

Label(window, text="Doan van 1", font="Times 20", bg="red").grid(row=0 , column=0, )
Label(window, text="Doan van 2", font="Times 20", bg="brown").grid(row=0 , column=1)
Label(window, text="Doan van 3", font="Times 20", bg="blue").grid(row=1 , column=0)
Label(window, text="Doan van 4", font="Times 20", bg="green").grid(row=1 , column=1)
Label(window, text="Doan van 5", font="Times 20", bg="yellow").grid(row=2 , column=0)
Label(window, text="Doan van 6", font="Times 20", bg="purple").grid(row=2 , column=1)
window.mainloop()