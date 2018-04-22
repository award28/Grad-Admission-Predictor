import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(7)

# dataset:
# https://github.com/ga-students/sf-dat-21/blob/master/unit-projects/dataset/admissions.csv
# data = pd.read_csv("admissions.titled.csv")

'''
y_train = data['admit'].head(300)
y_test = data['admit'].tail(100)
x_train = data.drop('admit', axis=1).head(300)
x_test = data.drop('admit', axis=1).tail(100)
'''


dataset = np.loadtxt("admissions.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,1:4]
Y = dataset[:,0]


model = Sequential()
model.add(Dense(10, input_dim=3, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(
        loss='binary_crossentropy', 
        optimizer='adam', 
        metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=15, batch_size=10)


print(model.evaluate(X, Y))
