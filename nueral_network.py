import pickle
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(7)

try:
    model = keras.models.load_model("nn.h5")
except:
    # df = pd.read_pickle("data.pickle")
    data = pd.read_pickle("data_minusUniv.pickle")
    print(data.head())
    
    q = len(data)//4
    train = data[:len(data) - q]
    test = data[len(data) - q:]
    
    train_y = train['decision']
    train_x = train.drop('decision', 1)
    
    test_y = test['decision']
    test_x = test.drop('decision', 1)

    print(data.head())
    
    # Create the model
    model = Sequential()
    model.add(Dense(20, input_dim=len(train_x.columns), activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    # Compile model
    model.compile(
            loss='binary_crossentropy', 
            optimizer='adam', 
            metrics=['accuracy']
            )
    
    # Fit the model
    model.fit(train_x, train_y, epochs=150, batch_size=30)

    model.save("nn.h5")

# Test the model
print("Prediction: " + str(model.evaluate(test_x, test_y)))
