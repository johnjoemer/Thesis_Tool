from tkinter import ttk
import tkinter as tk
import customtkinter
from PIL import Image
import os
import cv2
import dlib
from moviepy.editor import VideoFileClip
from ExtractImage import extract_frames
import cv2

def getDuration(video_path):
    clip = VideoFileClip(video_path)
    duration = clip.duration
    clip.close()
    return duration

def extract_frames(videoFile, times, sequencePath, progress_var):
    if not os.path.exists(sequencePath):
        os.makedirs(sequencePath)

    clip = VideoFileClip(videoFile)
    original_filename = os.path.splitext(os.path.basename(videoFile))[0]

    total_frames = len(times)
    counter = 0

    app = tk.Tk()
    app.title("Extracting Frames")
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

    for i, t in enumerate(times):
        frame_path = os.path.join(sequencePath, f'{original_filename}_frame{i+1}.jpg')
        clip.save_frame(frame_path, t)
    
        # Increment counter for the next face
        counter += 1

        # Update the progress bar
        progress_var.set(counter)
        app.update_idletasks()

    progress.destroy()
    app.destroy()
    print("Done Extracting Frames")

def CropFaces(input_folder, output_folder, progress_var):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    total_frames = 35

    app = tk.Tk()
    app.title("Cropping Frames")
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
                margin = 1
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

                # Update the progress bar
                progress_var.set(counter)
                app.update_idletasks()
    progress.destroy()
    app.destroy()
    print("Done Cropping Extracted Frames")


def ShowImage(ImagePath):
    try:
        image = customtkinter.CTkImage(dark_image=Image.open(ImagePath), size=(200, 200))

        return image

    except Exception as e:
        print(f"Error opening image: {e}")


def ShowVideo(VideoPath):
    # Takes original filename to create a new folder every time a new file is selected
    original_filename = os.path.splitext(os.path.basename(VideoPath))[0]
    
    ExtractedPath = os.path.join(os.path.dirname(VideoPath), f'{original_filename}_Extracted')
    os.makedirs(ExtractedPath, exist_ok=True)

    clip = VideoFileClip(VideoPath)
    times = [i/clip.fps for i in range(int(clip.fps * clip.duration))]
    progress_var = tk.DoubleVar()
    extract_frames(VideoPath, times, ExtractedPath, progress_var)

    croppedPath = os.path.join(os.path.dirname(VideoPath), f'{original_filename}_Cropped')
    CropFaces(ExtractedPath, croppedPath, progress_var)

    # Takes original filename and appends what frame it is to the end
    frame_path = os.path.join(croppedPath, f'{os.path.splitext(os.path.basename(VideoPath))[0]}_frame1_Cropped.jpg')
    # ShowImage(frame_path)
    return frame_path