import os
from tkinter import *
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
#chia luong du lieu
import threading
from tkinter import filedialog

#tai liệu tkinter
#https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Setting-window-size

window = Tk()
window.geometry("1400x700+50+50")
window.resizable(width=False,height=False)
window.title("Do an From")

#tao header menu
class App(Frame):
   
	def __init__(self, parent):
		Frame.__init__(self, parent)   
		
		self.parent = parent
		#khung chua danh sách toán tử điểm và tham số toán tử
		self.fram1 = Frame(parent)
		self.fram1.pack()
		#khung chua label ảnh
		self.fram2 = Frame(parent)
		self.fram2.pack()
		#khung chua cavas 2 ảnh
		self.fram3 = Frame(parent)
		self.fram3.pack()
		#khung chứa label histogram
		self.fram4 = Frame(parent)
		self.fram4.pack()
		#khung chưa in4 histogram 
		self.fram5 = Frame(parent)
		self.fram5.pack()
		self.fram6 = Frame(parent)
		self.fram6.pack()

		self.initUI()
 
	#hàm thiết lập giao diện
	def initUI(self):

		menubar = Menu(self.parent)
		self.parent.config(menu=menubar)
		
		fileMenu = Menu(menubar)       
		
		submenu = Menu(fileMenu)
		fileMenu.add_command(label="Open", command=self.openfile)
		#submenu.add_command(label="Open")
		#fileMenu.add_cascade(label='import', menu=submenu)

		#fileMenu.add_separator()
		fileMenu.add_command(label="Save", command=self.blur_image)
		fileMenu.add_command(label="Exit", command=self.onExit)
		menubar.add_cascade(label="File", menu=fileMenu)
		self.labelvd=Label(self.fram1,text="Hello SmallBird!", bg="blue",fg="white")
		#ipad thuoc tinh bg rong hep theo x va y
		# nen cach cua so padx va pady ( chua khoang trong)
		self.labelvd.pack(side=BOTTOM)
		self.lb_path1=Label(self.fram2,text="Path: ",fg="black")
		self.lb_path1.pack(side=LEFT)
		self.lb_be4=Label(self.fram2,text="Before",fg="black")
		self.lb_be4.pack(side=LEFT)


	#thoat
	def onExit(self):
		self.quit()


	def openfile(self):
		#mo file
		self.path = filedialog.askopenfilenames(
			initialdir='C:/Users/SB/Desktop/tkinter/',
			initialfile='tmp',
			filetypes=[
				("All files", "*"),
				("PNG", "*.png"),
				("JPEG", "*.jpg")])
		print(self.path)
		self.image_path=str(self.path)
		self.image_path=self.image_path[2:-3]
		print(self.image_path)
		print("image_path: ",type(self.image_path))



		#label
		
		
		self.lb_image_path=Label(self.fram2,text=self.image_path,fg="black")
		self.lb_image_path.pack(side=RIGHT)

		#process
		#self.image_path='images-001.jpg'
		#Read 16-bit / channel Color Image nên dùng cv2.IMREAD_ANYCOLOR
		self.cv_img = cv2.cvtColor(cv2.imread(self.image_path),cv2.IMREAD_ANYCOLOR)
		self.height, self.width, no_channels = self.cv_img.shape
		#tạo 2 canvas chua anh
		self.canvas = tkinter.Canvas(self.fram3, width = self.width, height = self.height)
		self.canvas.pack(side = LEFT)
		self.canvas1 = tkinter.Canvas(self.fram3, width = self.width, height = self.height)
		self.canvas1.pack(side = RIGHT)
		# dùng PIL (Pillow) để convert mảng NumPy ndarray sang PhotoImage
		self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
		self.photo1 = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
		# Thêm 1 PhotoImage vào Canvas
		# self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
		self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
		self.canvas1.create_image(0, 0, image=self.photo1, anchor=tkinter.NW)


	def blur_image(self):
		self.cv_img = cv2.blur(self.cv_img, (3, 3))
		self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
		self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

app = App(window)
window.mainloop()