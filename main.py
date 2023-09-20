from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
# from tkinter.tix import IMAGETEXT

def openImage():
    filepath=filedialog.askopenfilename(title="Select Dataset",
                                        filetypes=(("Images (.jpg)","*.jpg"),
                                        ("Videos (.mp4)","*.mp4")))
    file = Image.open(filepath)
    file=ImageTk.PhotoImage(file)
    imageLabel.configure(image=file,width=250,height=250)
    imageLabel.image=file
    # file.close()

def openVideo():
    filepath=filedialog.askopenfilename(title="Select Dataset",
                                        filetypes=(("Images (.jpg)","*.jpg"),
                                        ("Videos (.mp4)","*.mp4")))
    file = Image.open(filepath)
    file=ImageTk.PhotoImage(file)
    videoLabel.configure(image=file,width=250,height=250)
    videoLabel.image=file
    # file.close()

def classifyME():
    filepath=filedialog.askopenfilename(title="Select Dataset",
                                        filetypes=(("Images (.jpg)","*.jpg"),
                                        ("Videos (.mp4)","*.mp4")))
    file = open(filepath, 'r')
    file.close()

# Window
window = Tk()
window.title("Micro-Expression Detection using CNN-LBP")
window.geometry("700x500+250+180")
window.resizable(False,False)
window.configure(bg="#2f4155")


# First Frame
frame1 = Frame(window,bd=3,bg="grey", width=340, height=280,relief=GROOVE)
frame1.place(x=10,y=80)

# Label to place image in frame1
imageLabel = Label(frame1,bg="grey")
imageLabel.place(x=40,y=10)

videoLabel = Label(frame1,bg="grey")
videoLabel.place(x=40,y=10)

# Second Frame
frame2 = Frame(window,bd=3,bg="grey", width=340, height=280,relief=GROOVE)
frame2.place(x=350,y=80)

# Frame for Open button
frame3 = Frame(window,bd=3,bg="grey", width=330, height=100,relief=GROOVE)
frame3.place(x=10,y=370)

# Open button
Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=openImage).place(x=20,y=20)
Button(frame3,text="Open Video",width=10,height=2,font="arial 14 bold",command=openVideo).place(x=180,y=20)

# Frame for Classify button
frame4 = Frame(window,bd=3,bg="grey", width=330, height=100,relief=GROOVE)
frame4.place(x=360,y=370)

# Classify button
Button(frame4,text="Classify Img",width=10,height=2,font="arial 14 bold",command=classifyME).place(x=20,y=20)
Button(frame4,text="Classify Vid",width=10,height=2,font="arial 14 bold",command=classifyME).place(x=180,y=20)

window.mainloop()

# comment