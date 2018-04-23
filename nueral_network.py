import numpy as np
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(7)

# dataset:
# https://github.com/ga-students/sf-dat-21/blob/master/unit-projects/dataset/admissions.csv

dataset = np.loadtxt("admissions.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,1:4]
Y = dataset[:,0]


model = Sequential()
model.add(Dense(10, input_dim=3, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(
        loss='binary_crossentropy', 
        optimizer='adam', 
        metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=30, batch_size=10)

print("Prediction: " + str(model.predict(X)))

''' NOT WORKING
gre = int(input("gre: "))
gpa = float(input("gpa: "))
prestige = int(input("prestige: "))

p = np.array([gre, gpa, prestige])
print("Prediction: " + str(model.predict(p)))
'''
