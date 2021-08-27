"""
The author of this code is Ranukesh R Sah
"""
import sys
from subprocess import call
import os
from tkinter import *
import tkinter
import tkinter.messagebox
ranukesh=tkinter.Tk()
ranukesh.title("School Management System by Ranukesh")
ranukesh.geometry("1000x700")

ranukesh.resizable(False, False) 
title=Label(ranukesh,text="Database Management System",bd=1,relief=GROOVE,font=("arial",24,"bold"),bg="yellow",fg="green")
title.pack(side=TOP,fill=X)



def helloCallBack():
    os.system('python call1.py')
    
def helloCallBack2():
    os.system('python call2.py')




"""Frame1 ongoing"""

frame1=Frame(ranukesh,width=400,height=700,borderwidth=1,bg="lightblue")
frame1.pack(side="left",fill="y")

m_title=Label(frame1,text="Project Information:",bg="lightblue",fg="black",bd=10,font=("arial",24,"bold"),width=15)
m_title.grid(row=0,columnspan=1,pady=0,padx=0,)

frame2=Frame(frame1,width=400,height=800,borderwidth=1,bg="lightblue")
frame2.grid(row=1,column=0,pady=0,padx=0)

roll=Label(frame1,text="Done by:\nName: ranukesh Raj Sah\nSID: 210280\n Coventry Id: n/a\nModule Title: Programming and Algorithms 1\n Module Code: ST4061CEM\nModule Leader: Shyam Sundar Khatiwada\nCoursework Type: An Individual Project",bg="white",fg="black",bd=5,font=("helvetica",15,"normal"),width=40)
roll.grid(row=1,column=0,pady=0,padx=5,sticky='n')

"""
REVIEW
here is the other frame
"""

frame3=Frame(ranukesh,bd=1,bg="lightblue")
frame3.place(x=450,y=34,width=550,height=700)

search=Label(frame3,text="Database Management For Colleges",bg="blue",fg="white",font=("arial",17,))
search.place(x=40,y=20)

search1=Label(frame3,text="Select The Entry:",bg="lightblue",fg="black",font=("arial",17))
search1.place(x=35,y=60)

B=tkinter.Button(frame3,text="Student Information Management",command= helloCallBack,width=50,height=5)
B.place(x=40,y=100)

B2=tkinter.Button(frame3,text="Finance Management",command= helloCallBack2,width=50,height=5)
B2.place(x=40,y=205)


















ranukesh.mainloop()