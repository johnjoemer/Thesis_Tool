import tkinter as tk
import customtkinter
from tkinter import filedialog

from PreProcessing import *
from LBPSVMClassifier import *
from CNN_ApexFrame import *

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
            Duration = getDuration(FilePath)
            if Duration <= 5:
                ImagePath = ShowVideo(FilePath)
                SelectedImage = ShowImage(ImagePath)

                current_image_label = customtkinter.CTkLabel(master=app, image=SelectedImage, text="")
                current_image_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
            else:
                textbox2.delete("0.0", "end")
                textboxOutput = "Video file too long. Please choose another file"
                textbox2.insert("0.0", f"{textboxOutput}")
                print("Video file too long. Please choose another file")


def ModelRunner():
    try:
        DirectoryPath = filedialog.askdirectory()
        print(f"Selected Directory: {DirectoryPath}")

        # Initialize Progress Bar
        progress_var = tk.DoubleVar()

        # CNN Model
        imagePath = SpotME(DirectoryPath, progress_var)

        # Load SVM Model
        svm_model_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/SVM_Classifier_Model/SVM_Not_Including_Others_Emotion_90Features.joblib'

        if imagePath is not None:
            # Stores the classified ME to local variable
            predictedME = classifyME(imagePath, svm_model_path, progress_var)

            SelectedImage = ShowImage(imagePath)

            current_image_label = customtkinter.CTkLabel(master=app, image=SelectedImage, text="")
            current_image_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

            # Outputs to textbox2 and console
            textbox2.delete("0.0", "end")
            textboxOutput = predictedME[0]
            textbox2.insert("0.0", f"Micro-Expression Present is: {textboxOutput}")
            print(f"Micro-Expression Present is: {textboxOutput}")
        else:
            textbox2.delete("0.0", "end")
            textboxOutput = "Error Finding Apex Frame at Chosen Directory"
            textbox2.insert("0.0", f"{textboxOutput}")
            print("Error Finding Apex Frame at Chosen Directory")

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
