from tkinter import *
root = Tk()
root.title("Pil and Tkinter")
#tao 1 widget label
my_label1 = Label(root, text="Hello Word! line 00")
my_label2 = Label(root, text="Hello Word! line 01")
my_label3 = Label(root, text="Hello Word! line 10").grid(row=1, column=0)
my_label4 = Label(root, text="Hello Word! line 11").grid(row=1, column=1)
#dua text ra man hinh
my_label1.grid(row=0, column=0)
my_label2.grid(row=0, column=1)

root.mainloop()