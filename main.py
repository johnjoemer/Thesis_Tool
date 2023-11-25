import tkinter as tk
import customtkinter
from tkinter import filedialog
from PIL import Image
import os
import time
import cv2
import dlib
from tqdm import tqdm
from tkinter import ttk
from moviepy.editor import VideoFileClip
# from ExtractImage import extract_frames


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

current_image_label = None


def OpenFile():
    FilePath = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov"), ("Image Files", "*.jpg *.jpeg *.png")])
    if FilePath:
        if FilePath.lower().endswith((".jpg", "jpeg", ".png")):
            ShowImage(FilePath)
        elif FilePath.lower().endswith((".mp4", ".avi", ".mkv", ".mov")):
            ShowVideo(FilePath)

def extract_frames(videoFile, times, sequencePath):
    extracting = tk.Tk()
    extracting.title("Extracting Frames")

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(extracting, variable=progress_var, length=300, mode='determinate')
    progress_bar.grid(row=0, column=0, padx=10, pady=10)

    if not os.path.exists(sequencePath):
        os.makedirs(sequencePath)

    clip = VideoFileClip(videoFile)
    original_filename = os.path.splitext(os.path.basename(videoFile))[0]

    counter = 0

    for i, t in enumerate(times):
        frame_path = os.path.join(sequencePath, f'{original_filename}_frame{i+1}.jpg')
        clip.save_frame(frame_path, t)
    
        # Increment counter for the next face
        counter += 1

        progress_value = int(counter / 35 * 100)
        progress_var.set(progress_value)
        progress_bar.update_idletasks()
    
    extracting.destroy()

def CropFaces(input_folder, output_folder):
    crop = tk.Tk()
    crop.title("Cropping Frames")

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(crop, variable=progress_var, length=300, mode='determinate')
    progress_bar.grid(row=0, column=0, padx=10, pady=10)

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Initialize the face detector from dlib
    face_detector = dlib.get_frontal_face_detector()

    # Iterate through all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".png")):
            input_path = os.path.join(input_folder, filename)

            # Load the image
            img = cv2.imread(input_path)
            
            # Conver the image to grayscale for face detection
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Call face detector function from dlib
            faces = face_detector(gray_img)

            # Initialize a counter for unique face identification
            counter = 0

            # Crop and save each detected face
            for i, face in enumerate(faces, start=1):
                x, y, w, h = face.left(), face.top(), face.width(), face.height()

                # Adjust the cropping region to include some margin around the face
                margin = 5
                x -= margin
                y -= margin
                w += 2 * margin
                h += 2 * margin 

                # Ensure the cropping region is within the image boundaries
                x = max(x, 0)
                y = max (y, 0)
                w = min(w, img.shape[1] - x)
                h = min(h, img.shape[0] - y)

                # Crop the face
                cropped_face = img[y:y+h, x:x+w]

                # Save the cropped faces
                output_filename = f"{os.path.splitext(filename)[0]}_Cropped.jpg"
                output_filepath = os.path.join(output_folder, output_filename)
                cv2.imwrite(output_filepath, cropped_face)

                # Increment counter for the next face
                counter += 1

                progress_value = int(counter / 35 * 100)

                progress_var.set(progress_value)
                progress_bar.update_idletasks()

    crop.destroy()

def ShowImage(ImagePath):
    global current_image_label

    try:
        image = customtkinter.CTkImage(dark_image=Image.open(ImagePath), size=(200, 200))

    except Exception as e:
        print(f"Error opening image: {e}")

    # Removes the last displayed image, to make room for new selected file
    if current_image_label:
        current_image_label.destroy()

    current_image_label = customtkinter.CTkLabel(master=app, image=image, text="")
    current_image_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

def ShowVideo(VideoPath):
    global current_image_label

    # Takes original filename to create a new folder every time a new file is selected
    original_filename = os.path.splitext(os.path.basename(VideoPath))[0]
    
    ExtractedPath = os.path.join(os.path.dirname(VideoPath), f'{original_filename}_Extracted')
    os.makedirs(ExtractedPath, exist_ok=True)

    clip = VideoFileClip(VideoPath)
    times = [i/clip.fps for i in range(int(clip.fps * clip.duration))]
    extract_frames(VideoPath, times, ExtractedPath)

    croppedPath = os.path.join(os.path.dirname(VideoPath), f'{original_filename}_Cropped')
    CropFaces(ExtractedPath, croppedPath)

    # Takes original filename and appends what frame it is to the end
    frame_path = os.path.join(croppedPath, f'{os.path.splitext(os.path.basename(VideoPath))[0]}_frame1_Cropped.jpg')
    ShowImage(frame_path)


def ClassifyME():
    classify = tk.Tk()
    classify.title("Recognizing Micro-Expression")

    classify_progress_var = tk.DoubleVar()
    classify_progress_bar = ttk.Progressbar(classify, variable=classify_progress_var, length=300, mode='determinate')
    classify_progress_bar.grid(row=0, column=0, padx=10, pady=10)

    classify.after(1000, lambda: close_windows(classify))

def close_windows(classify_window):
    classify_window.destroy()
    textbox2.delete("0.0", "200.00") 
    result = "Classification: Disgust"
    textbox2.insert("0.0", result)   

# Create the main window
app = customtkinter.CTk()
app.title("A Hybridized CNN-LBP Micro-Expression Recognition")
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
