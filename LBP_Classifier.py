from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import cv2
from skimage import feature
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization

data = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CASME2-coding-20140508.csv'
df = pd.read_csv(data)

def compute_lbp(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lbp = feature.local_binary_pattern(gray, P=8, R=1, method="uniform")
    return lbp


def SVM_Classify(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Classifier initialization
    svm_classifier = SVC(kernel='linear', C=1.0)

    # Training the Classifier
    svm_classifier.fit(X_train, y_train)

    # Test prediction using Test sample 
    predictions = svm_classifier.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print (f"Accuracy: {accuracy * 100: .2f}%")


if __name__ == "__main__":
    # copy the apex frame path to be used for LBP computing and SVM classifying.
    image_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CASME2_preprocessed_Li Xiaobai/Cropped/sub01/EP02_01f/reg_img46.jpg' # this should come from the output of CNN model
    img = cv2.imread(image_path)
    labels = [0, 1, 1, 0]

    if img is None:
        print(f"Error: Unable to load the image from {image_path}")
    
    else:
        lbp_features = compute_lbp(img)
        print("LBP Features Shape: ", lbp_features.shape)

        # SVM_Classify(lbp_features, labels)
