import numpy as np
import pandas as pd
import keras.models
from keras.layers import Dense
from sklearn.model_selection import train_test_split

np.random.seed(7)

# data = pd.read_csv("data/filter/grad_uni_one_hot.csv")
# train, test = train_test_split(data, test_size=0.2)

train = pd.read_csv("data/train/grad_uni_one_hot.csv")
test = pd.read_csv("data/test/grad_uni_one_hot.csv")

column_name = list(train)
features = column_name[1:]
target = column_name[0]

train_features = train[features]
train_target = train[target]

test_features = test[features]
test_target = test[target]

try:
    model = keras.models.load_model("nn.h5")
except:
    # Create the model
    model = keras.models.Sequential()
    model.add(Dense(20, input_dim=len(train_features.columns), activation='relu'))
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
    model.fit(train_features, train_target, epochs=150, batch_size=30)

    model.save("nn.h5")

# Test the model
print("Prediction: " + str(model.evaluate(test_features, test_target)))
