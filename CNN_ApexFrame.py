from tkinter import ttk
import tkinter as tk
from keras.preprocessing import image
from keras.models import load_model
import os
import numpy as np

def SpotME(folder_path, progress_var):
    total_frames = 35
    counter = 0

    app = tk.Tk()
    app.title("Finding Apex Frame")
    app.geometry("250x50")

    progress = ttk.Progressbar(
        app,
        orient="horizontal",
        length=200,
        mode="determinate",
        variable=progress_var
    )
    progress.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    progress["maximum"] = total_frames

    loaded_model = load_model('/Users/jj/Documents/COLLEGE_DOCS/CASME2/Iteration_5/CNN_Model_Iteration_5/CNN_Model_Iteration_5.keras')
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            img = image.load_img(file_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.
            label_pred = loaded_model.predict(img_array.reshape(1, 224, 224, 3))
            print(file_path)
            print(label_pred)
            label_pred = label_pred > 0.5

            if (label_pred == 0):
                print("Apex Frame Spotted\n")
                print(f"Apex Frame Path: {file_path}\n")
                
                # Update the progress bar
                progress.destroy()
                app.destroy()
                return file_path
            else:
                print(file_path)
                pred = 'No Apex Frame spotted'
                print(pred)

                # Increment counter for the next face
                counter += 1

                # Update the progress bar
                progress_var.set(counter)
                app.update_idletasks()

    progress.destroy()
    app.destroy()
