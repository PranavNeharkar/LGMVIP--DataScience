# -*- coding: utf-8 -*-
"""2..Intermediate Level Task _2.Prediction using Decision Tree Algorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aN5lGoqMtLPmbPcSLhOKWWP8AvCtslwk

**NAME : Pranav Nivrutti Neharkar**

LGM VIP: Data Science Internship

2.Intermediate Level Task -2.Prediction using Decision Tree  Algorithm  

Language-Python

Software-Google Colab

Dataset-https://bit.ly/3kXTdox

**Importing Required Libraries**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import sklearn.metrics as sm
import seaborn as sns
import matplotlib.pyplot as mt
# %matplotlib inline

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score
from matplotlib.pyplot import rcParams


import warnings
warnings.filterwarnings("ignore")

"""**Dataset reading**"""

dat = pd.read_csv('/content/Iris.csv')
dat

dat.describe()

"""**Checking Null Values**"""

dat.isna().sum()

dat.describe()

"""**Data Visualization & Cor-relation Matrix**"""

sns.pairplot(dat, hue='Species')

sns.heatmap(dat.corr(),annot=True)

"""**Data Preprocessing**"""

X=dat.iloc[:,[0,1,2,3]]
y=dat.Species
y
dat.shape

X.shape

y.shape

"""**Train,Test,Split**"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train.shape

X_test.shape

"""**Decision Tree**"""

clf = DecisionTreeClassifier(criterion='entropy')

clf.fit(X_train, y_train)

y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)

pd.DataFrame(dat.Species).value_counts()

accuracy_score(y_train, y_pred_train)

accuracy_score(y_test, y_pred_test)

rcParams['figure.figsize'] = 80, 50
plot_tree(clf,precision=5,rounded=True,filled=True);