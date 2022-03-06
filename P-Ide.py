from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from tkinter import messagebox

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background='gray')

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.28, rely=0.03, anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46, rely=0.03, anchor=CENTER)

my_text=Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)


#name = ""
#def openFile():
  #  global name
    
  
open_buttom=Button(root,image=open_img,text="OpenFile",commamd=openFile)
open_button.place(rex=0.5,rely=0.3,anchor=CENTER)   
save_button=Button(root,image=open_img,text="SaveFile",commamd=openFile)
save_button.place(rex=0.11,rely=0.3,anchor=CENTER)  
exit_buttom=Button(root,image=open_img,text="ExitFile",commamd=openFile)
exit_button.place(rex=0.17,rely=0.3,anchor=CENTER)   

root.mainloop()