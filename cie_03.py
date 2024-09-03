# -*- coding: utf-8 -*-
"""CIE-03

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HzcUv0a1rUkA1uMsqsQ-Y9HRrz_myo5y
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = data.iris
y= data.target
X
y

df['species'] = pd.Categorical.from_codes(y, iris.target_names)
print(df.head())
print(df.describe())
print(df['species'].value_counts())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2,random_state=42)

df.info()

df. describe ()

df.isnull(). sum()

X_train

y_train

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of the Decision Tree model: {accuracy:.2f}')