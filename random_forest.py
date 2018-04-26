import pandas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

target = "decision"
data = pandas.read_csv("all_filter.csv")
column_name = list(data)
features = column_name[1:-1]
target = column_name[0]

train_features, test_features, train_target, test_target = train_test_split(data[features], data[target])

clf = RandomForestClassifier()
clf.fit(train_features, train_target)

predictions = clf.predict(test_features)
actual = list(test_target)

correct = 0.0
for i in range(len(predictions)):
    if predictions[i] == actual[i]:
        correct += 1.0

print(correct / len(predictions))
