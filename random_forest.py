import pandas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# data = pandas.read_csv("data/filter/grad_uni_one_hot.csv")
# train, test = train_test_split(data, test_size=0.2)

train = pandas.read_csv("data/train/grad_uni_one_hot.csv")
test = pandas.read_csv("data/test/grad_uni_one_hot.csv")

column_name = list(train)
features = column_name[1:]
target = column_name[0]

train_features = train[features]
train_target = train[target]

test_features = test[features]
test_target = test[target]

clf = RandomForestClassifier(n_estimators=145, max_features="log2", min_samples_split=20, random_state=14)
clf.fit(train_features, train_target)

predictions = clf.predict(test_features)
actual = list(test_target)

correct = 0.0
for i in range(len(predictions)):
    if predictions[i] == actual[i]:
        correct += 1.0

print(correct / len(predictions))
