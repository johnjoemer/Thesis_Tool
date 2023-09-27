import tkinter as tk
import customtkinter
from tkinter import filedialog
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

def OpenFile():
    FilePath = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov"), ("Image Files", "*.jpg *.jpeg *.png")])
    if FilePath:
        if FilePath.lower().endswith((".jpg", "jpeg", ".png")):
            ShowImage(FilePath)

def ShowImage(ImagePath):
    image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(ImagePath)),
                                   size=(200, 200))
    image_label = customtkinter.CTkLabel(master=app, image=image, text="")
    image_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


def ClassifyME():
    textbox2.delete("0.0", "200.0")
    result = "Classification: Happiness"
    textbox2.insert("0.0", result)

# Create the main window
app = customtkinter.CTk()
app.geometry("600x550")

# Create container for Apex Frame
textbox = customtkinter.CTkTextbox(master=app, width=250, height=250)
textbox.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Create textbox for result
textbox2 = customtkinter.CTkTextbox(master=app, width=300, height=45)
textbox2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Create a button to open files
btn = customtkinter.CTkButton(master=app, text="Input File", command=OpenFile)
btn.place(relx=0.5, rely=0.6125, anchor=tk.CENTER)

# Create a button to classify micro-expression
btn2 = customtkinter.CTkButton(master=app, text="Classify ME", command=ClassifyME)
btn2.place(relx=0.5, rely=0.6825, anchor=tk.CENTER)

# Run the Tkinter main loop
app.mainloop()
