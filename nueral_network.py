import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(7)

data = pd.read_csv("admissions.csv")
y_train = data['admit']
x_train = data.drop('admit', axis=1)

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=3))
model.add(Dense(units=1, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=2, batch_size=16, verbose=2)
