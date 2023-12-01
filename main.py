# script for apex frame extraction >
# iterate thru the image sequence to spot apex frame >
# train CNN using extracted apex frames >
# train SVM >
# Use the estimated emotion "others" as "No Micro-Expression" value >
# Connect the 2 models to the interface
# Add three buttons for "Process Images" "Spot Apex Frame" "Classify ME"

import tkinter as tk
import customtkinter
from tkinter import filedialog
from ExtractImage import extract_frames

from PreProcessing import *
from LBPSVMClassifier import *

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

def PreprocessRunner():
    FilePath = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov"), ("Image Files", "*.jpg *.jpeg *.png")])
    if FilePath:
        if FilePath.lower().endswith((".jpg", "jpeg", ".png")):
            SelectedImage = ShowImage(FilePath)

            current_image_label = customtkinter.CTkLabel(master=app, image=SelectedImage, text="")
            current_image_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        elif FilePath.lower().endswith((".mp4", ".avi", ".mkv", ".mov")):
            ImagePath = ShowVideo(FilePath)
            SelectedImage = ShowImage(ImagePath)

            current_image_label = customtkinter.CTkLabel(master=app, image=SelectedImage, text="")
            current_image_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


def ModelRunner():
    try:
        DirectoryPath = filedialog.askdirectory()
        print(f"Selected Directory: {DirectoryPath}")

        # CNN Model
        
        # imagePath = cnnModel(DirectoryPath)
        imagePath = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/Extracted_ApexFrames/EP06_07_frame225.jpg'
        svm_model_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/SVM_Classifier_Model/SVM_Model_ApexFrameV6_37percent.joblib'
        progress_var = tk.DoubleVar()

        # Stores the classified ME to local variable
        predictedME = classifyME(imagePath, svm_model_path, progress_var)

        # Outputs to textbox2 and console
        textbox2.delete("0.0", "200.00")
        textbox2.insert("0.0", predictedME)
        print(f"Micro-Expression Present is: {predictedME}")

    except tk.TclError:
        print("Invalid Directory")
    

# Create the main window
app = customtkinter.CTk()
app.title("A Hybridized CNN-LBP Micro-Expression Recognition")
app.geometry("600x550")

# Create container to display selected image
textbox = customtkinter.CTkTextbox(master=app, width=250, height=250)
textbox.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Create a button to preprocess the input video
btn1 = customtkinter.CTkButton(master=app, text="Input File", command=PreprocessRunner)
btn1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Create a button to spot the apex frame and classify ME
btn2 = customtkinter.CTkButton(master=app, text="Spot and Classify", command=ModelRunner)
btn2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)


# Create textbox for result
textbox2 = customtkinter.CTkTextbox(master=app, width=300, height=45)
textbox2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Run the Tkinter main loop
app.mainloop()
