import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import os
import random
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.preprocessing import image
from sklearn.model_selection import train_test_split

# Function to load and preprocess CASME2 data
def load_and_preprocess_casme2_data(dataset_path, image_size):
    images = []
    labels = []

    classes = sorted(os.listdir(dataset_path))
    for i, class_name in enumerate(classes):
        class_path = os.path.join(dataset_path, class_name)
        for image_file in os.listdir(class_path):
            image_path = os.path.join(class_path, image_file)

            # Read and resize the image using OpenCV
            img = cv2.imread(image_path)
            img = cv2.resize(img, (image_size, image_size))  # Resize to desired dimensions
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Append the preprocessed image and its label to the lists
            images.append(img)
            labels.append(i)  # Assigning labels based on class index

    # Convert lists to numpy arrays
    images = np.array(images)
    labels = np.array(labels)

    return images, labels

# Example usage:
# dataset_path = r'C:\Users\Obey\OneDrive - Polytechnic University of the Philippines\Desktop\Thesis Tool\Dataset 5'
dataset_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/Dataset_5'
image_size = 224  # Adjust the image size as needed

# Load and preprocess CASME2 data
images, labels = load_and_preprocess_casme2_data(dataset_path, image_size)

# Split the data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

Y_train = Y_train.reshape(len(Y_train), 1)
Y_test = Y_test.reshape(len(Y_test), 1)

X_train = X_train/255.0
X_test = X_test/255.0

model = Sequential()

model.add(Conv2D(107, (3,3), activation='relu', input_shape=(224, 224, 3)))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(50, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(23, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(10, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=10, batch_size=64)

model.evaluate(X_test, Y_test)