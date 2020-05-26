from tkinter import *
window = Tk()

labelvd=Label(window,text="Hello SmallBird!", bg="blue",fg="white")
#ipad thuoc tinh bg rong hep theo x va y
# nen cach cua so padx va pady ( chua khoang trong)
labelvd.pack(side=BOTTOM, ipadx=50,ipady=50,padx=50,pady=50,)


window.mainloop()