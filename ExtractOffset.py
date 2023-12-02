import os
import cv2
import pandas as pd
import shutil

# Change csv_path, source_root_folder, output_folder values before running
csv_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CodingForSVMTrainingV4_DoesntIncludeOthersEmotion.csv'
df = pd.read_csv(csv_path)

# Specify the source folder for images
source_root_folder = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/Cropped/'

# Specify the output folder for copied images
output_folder = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/Extracted_OffsetFrames/'

# Create the output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Iterates thru each row in the CSV
for index, row in df.iterrows():
    subject = str(row['Subject']).zfill(2)
    filename = row['Filename']
    offset_frame = row['OffsetFrame']

    # Construct the source and destination file paths
    source_path = os.path.join(source_root_folder, f'sub{subject}', filename, f'reg_img{offset_frame}.jpg')
    output_path = os.path.join(output_folder, f'{filename}_frame{offset_frame}.jpg')

    # Check if the source image file exists
    if os.path.exists(source_path):
        # Copy all images in the source folder to the output folder
        for file_name in os.listdir(os.path.dirname(source_path)):
            if file_name == f'reg_img{offset_frame}.jpg':
                source_file_path = os.path.join(os.path.dirname(source_path), file_name)
                output_file_path = os.path.join(output_folder, f'sub{subject}_{file_name}')
                shutil.copy(source_file_path, output_file_path)
    else:
        print(f"Source image not found: {source_path}")
