import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score

df = pd.read_csv('lab7\data.csv')

X = np.array(df[["radius_mean", "texture_mean", "perimeter_mean", "smoothness_mean"]])
Y = np.array(df["diagnosis"])


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25,  random_state=42)
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
clf = SGDClassifier(loss='log_loss', max_iter=1000, random_state=42)
clf.fit(X_train, Y_train)

Y_pred = clf.predict(X_test)

print("Точність: ", accuracy_score(Y_test, Y_pred))
print("Загальна точність: ", precision_score(Y_test, Y_pred, pos_label = "B"))
print("Матриця помилок: ", "\n", confusion_matrix(Y_test, Y_pred))