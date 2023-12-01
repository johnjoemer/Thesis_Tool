# Script to extract LBP Features and append it to the CSV file

import os
import cv2
import pandas as pd
from skimage import feature

def compute_lbp(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lbp = feature.local_binary_pattern(gray, P=8, R=1, method="uniform")
    return lbp

csv_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CodingForSVMTrainingV2.csv'
df = pd.read_csv(csv_path)

# Stores the computed LBP features
df['Computed LBP'] = ""

# Iterates thru each row in the CSV
for index, row in df.iterrows():
    subject = str(row['Subject']).zfill(2)
    filename = row['Filename']
    apex_frame = row['ApexFrame']

    # Construct the actual image path to be used
    image_path = f'/Users/jj/Documents/COLLEGE_DOCS/CASME2/Extracted_ApexFrames/{filename}_frame{apex_frame}.jpg'



def iterateApex(sourcepath):
    # Check if the image file exists
    if os.path.exists(image_path):
        # Read the image
        image = cv2.imread(image_path)

        # compute for the LBP features
        lbp_features = compute_lbp(image)

        lbp_features_flat = lbp_features.flatten()

        # Update the "Computed LBP" column in the DataFrame
        df.at[index, 'Computed LBP'] = ','.join(map(str, lbp_features_flat[:120])) # Only takes the first 120 elements of the array | too long, causes an error

    else:
        print(f"Image not found: {image_path}")

# Save the updated DataFrame to a new CSV file
output_csv_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/Coding with Computed LBP Features 120features.csv'
df.to_csv(output_csv_path, index=False)
