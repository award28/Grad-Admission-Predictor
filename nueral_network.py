import pickle
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(7)

try:
    model = pickle.load(open('model.pickle', 'rb'))
except:
    # df = pd.read_pickle("data.pickle")
    data = pd.read_pickle("data_minusUniv.pickle")
    
    print(data.head())
    mid = len(data)//2
    train = data[:mid]
    test = data[mid:]
    
    train_y = train['decision']
    train_x = train.drop('decision', 1)
    
    test_y = test['decision']
    test_x = test.drop('decision', 1)
    
    # Create the model
    model = Sequential()
    model.add(Dense(10, input_dim=len(train_x.columns), activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    # Compile model
    model.compile(
            loss='binary_crossentropy', 
            optimizer='adam', 
            metrics=['accuracy']
            )
    
    # Fit the model
    model.fit(train_x, train_y, epochs=25, batch_size=100)

    with open('model.pickle', 'wb') as p:
        pickle.dump(model, p)

# Test the model
print("Prediction: " + str(model.evaluate(test_x, test_y)))
