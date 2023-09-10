from tkinter import *
from tkinter import filedialog

def openFile():
    filepath=filedialog.askopenfilename(title="Select Dataset",
                                        filetypes=(("Images","*.jpg"),
                                        ("Videos","*.mp4")))
    file = open(filepath, 'r')
    file.close()


window = Tk()
button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()

