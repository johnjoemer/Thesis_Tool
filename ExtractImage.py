# from moviepy.editor import VideoFileClip
# import os
# import time
# from tqdm import tqdm
# from tkinter import ttk
# import tkinter as tk
# import customtkinter

# def extract_frames(videoFile, times, sequencePath):
#     extracting = tk.Tk()
#     extracting.title("Extracting Frames")

#     progress_var = tk.DoubleVar()
#     progress_bar = ttk.Progressbar(extracting, variable=progress_var, length=300, mode='determinate')
#     progress_bar.grid(row=0, column=0, padx=10, pady=10)
#     extracting.mainloop()

#     if not os.path.exists(sequencePath):
#         os.makedirs(sequencePath)

#     clip = VideoFileClip(videoFile)
#     original_filename = os.path.splitext(os.path.basename(videoFile))[0]

#     counter = 0

#     for i, t in enumerate(times):
#         frame_path = os.path.join(sequencePath, f'{original_filename}_frame{i+1}.jpg')
#         clip.save_frame(frame_path, t)
    
#         # Increment counter for the next face
#         counter += 1

#         progress_value = int(counter / 35 * 100)
#         progress_var.set(progress_value)
#         progress_bar.update_idletasks()
    
#     extracting.destroy()

#     # for time in tqdm(times, desc="Extracting images", unit="frame", leave=False):
#     #     extract_frames(videoFile, [time], sequencePath)
        

# # movie = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CASME2_compressed/sub01/EP02_01f.avi'
# # sequencePath = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CASME2_compressed/sub01/Extracted'
# # clip = VideoFileClip(movie)
# # times = [i/clip.fps for i in range(int(clip.fps * clip.duration))]
# # extract_frames(movie, times, sequencePath)