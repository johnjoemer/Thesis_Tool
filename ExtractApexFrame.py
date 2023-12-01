import os
import cv2
import pandas as pd
import shutil

# Change csv_path, source_root_folder, output_folder values before running

csv_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CodingForSVMTrainingV3.csv'
df = pd.read_csv(csv_path)

# Specify the source folder for images
source_root_folder = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/Cropped/'

# Specify the output folder for copied images
output_folder = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/Extracted_ApexFrames/'

# Create the output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Iterates thru each row in the CSV
for index, row in df.iterrows():
    subject = str(row['Subject']).zfill(2)
    filename = row['Filename']
    apex_frame = row['ApexFrame']

    # Construct the source and destination file paths
    source_path = os.path.join(source_root_folder, f'sub{subject}', filename, f'reg_img{apex_frame}.jpg')
    output_path = os.path.join(output_folder, f'{filename}_frame{apex_frame}.jpg')

    # Check if the source image file exists
    if os.path.exists(source_path):
        # Copy the image to the output folder
        shutil.copy(source_path, output_path)
    else:
        print(f"Source image not found: {source_path}")