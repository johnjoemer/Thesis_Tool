from tkinter import ttk
import tkinter as tk
import cv2
from skimage import feature
import numpy as np
import joblib

def compute_lbp(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lbp = feature.local_binary_pattern(gray, P=8, R=1, method="uniform")

    lbp_features_flat = lbp.flatten()[:90]

    return lbp_features_flat

def classifyME(imagePath, svmModelPath, progress_var):
    counter = 100
    app = tk.Tk()
    app.title("Classifying Micro-Expression")
    app.geometry("250x50")

    progress = ttk.Progressbar(
        app,
        orient="horizontal",
        length=200,
        mode="determinate",
        variable=progress_var
    )
    image = cv2.imread(imagePath)

    lbpfeatures = compute_lbp(image)

    if len(lbpfeatures) != 90:
        print(f"Error: Expected 90 features, but got {len(lbpfeatures)} features.")
        return None, None

    lbpfeatures = np.array([lbpfeatures])

    trained_SVM_Model = joblib.load(svmModelPath)

    # Use predict_proba instead of predict
    probabilities = trained_SVM_Model.predict_proba(lbpfeatures)

    # Assuming your SVM model has classes like 'happy', 'sad', etc.
    class_labels = trained_SVM_Model.classes_

    # Map class labels to probabilities
    probabilities_dict = {class_labels[i]: probabilities[0][i] for i in range(len(class_labels))}

    # Sort the probabilites by descending order
    sorted_probabilities = dict(sorted(probabilities_dict.items(), key=lambda item: item[1], reverse=True))

    # Get the predicted ME
    predicted_class = trained_SVM_Model.predict(lbpfeatures)[0]

    # Update the progress bar
    progress_var.set(counter)
    app.update_idletasks()
    progress.destroy()
    app.destroy()

    return predicted_class, sorted_probabilities
