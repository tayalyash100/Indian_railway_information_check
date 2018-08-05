from tkinter import *
from PIL import ImageTk
import Image
from pnrF import ppnnrr
import requests, json
from StationCode import std
from CancelTrains import can
from YashTrainFE import liv




root=Tk()

root.geometry('500x500')

lable1=Label(root,text="Developed by Yash Tayal")
lable1.pack(side=BOTTOM,fill=X)


lable0=Label(root,text="Welcome to Indian Railway Online Panel",fg="purple")
lable0.config(font=("Comic Sans MS",18,'bold'))
lable0.pack(fill=X)


lable2=Label(root,text="Hello friends we have tried to develop a user friendly railway app")
lable2.config(font=('none',12,'bold'))
lable2.pack(fill=X,)
img=ImageTk.PhotoImage(Image.open("train.jpg"))


lable=Label(root,image=img)

lable.pack(side=TOP)

frame=Frame(root)
frame.pack(side=TOP)

pnr=Button(frame,text="PNR status",command=ppnnrr).grid()
status=Button(frame,text="Train status",comman=liv).grid(row=0,column=1,padx=10)
station=Button(frame,text="Station Code",command=std).grid(row=0,column=2,padx=10)
cancel=Button(frame,text="Cancelled Trains",command=can).grid(row=0,column=3,padx=10)





















root.config(bg="lavender")

root.mainloop()