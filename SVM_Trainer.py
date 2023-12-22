import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score
import joblib

data = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/10 Fold Cross Validation CSV/Iteration_1_Training_ComputedLBP.csv'
df = pd.read_csv(data)

print(type(df['Computed LBP'][0]))

df['Computed LBP'] = df['Computed LBP'].apply(lambda x: list(map(float, x.split(','))) if pd.notnull(x) else x)
df['Computed LBP'] = df['Computed LBP'].apply(lambda x: np.array(x).flatten() if isinstance(x, list) else x)
print(type(df['Computed LBP'][0]))

X = df['Computed LBP'].to_list()
X = np.array(X)

y = df['Estimated Emotion']


print(df.at[0, 'Computed LBP'])
print(df.at[0, 'Estimated Emotion'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Classifier initialization
svm_classifier = SVC(kernel='linear', C=1.0)
svm_classifier = SVC(probability=True)

# Training the Classifier
svm_classifier.fit(X_train, y_train)
joblib.dump(svm_classifier, '/Users/jj/Documents/COLLEGE_DOCS/CASME2/SVM_Model_10foldcross/SVM_Iteration_1')
trained_SVM_Model = joblib.load('/Users/jj/Documents/COLLEGE_DOCS/CASME2/SVM_Model_10foldcross/SVM_Iteration_1')

# Test prediction using Test sample 
predictions = trained_SVM_Model.predict(X_test)
# predictions = svm_classifier.predict(X_test)

print(predictions)

accuracy = accuracy_score(y_test, predictions)
print (f"Accuracy: {accuracy * 100: .2f}%")