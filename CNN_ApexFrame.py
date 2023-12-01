from keras.preprocessing import image
from keras.models import load_model
import os
import numpy as np

def SpotME(folder_path):
    # folder_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CASME2_compressed/sub04/EP13_06f_Cropped'
    loaded_model = load_model('/Users/jj/Documents/GitHub/Thesis_Tool/CNN_model.keras')
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            img = image.load_img(file_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.
            label_pred = loaded_model.predict(img_array.reshape(1, 224, 224, 3))
            print(label_pred)
            label_pred = label_pred > 0.5

            if (label_pred == 0):
                print("Apex Frame Spotted")
                return file_path
            else:
                pred = 'No Apex Frame spotted'
                print(pred)

# folder_path = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CASME2_compressed/sub04/EP13_06f_Cropped/'
# loaded_model = load_model('/Users/jj/Documents/GitHub/Thesis_Tool/CNN_model.keras')
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         file_path = os.path.join(root, file)
#         img = image.load_img(file_path, target_size=(224, 224))
#         img_array = image.img_to_array(img)
#         img_array = np.expand_dims(img_array, axis=0)
#         img_array /= 255.
#         label_pred = loaded_model.predict(img_array.reshape(1, 224, 224, 3))
#         print(label_pred)
#         label_pred = label_pred > 0.5

#         if (label_pred == 0):
#             print("Apex Frame Spotted")
#             # return file_path
#         else:
#             pred = 'No Apex Frame spotted'
#             print(pred)