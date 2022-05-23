from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk

a = tk.Tk()
a.geometry("1800x850")
frame =Frame(a,width = 1800,height=950)

frame.place(anchor='center',relx=0.5,rely=0.5)


img =ImageTk.PhotoImage(Image.open("C:\\Users\\nikhi\\OneDrive\\Desktop\\Tourism\\4.jpg"))

label = Label(frame,image=img)

chat = Label(a,text="TOURISM",bg='snow2')
chat.config(font = ("Times New Roman",45))

a.title('Tourism Started')
button = tk.Button(a,text="Let's Start the Journey",bg='PeachPuff2',width=25,activebackground='black',activeforeground='medium orchid',command=a.destroy)




button.pack()
button.place(relx=0.82,rely=0.89, relwidth=0.20,relheight=0.05)
chat.pack()
chat.place(relx=0.38,rely=0.029, relwidth=0.20, relheight=0.08)
frame.pack()
label.pack()
a.mainloop()
