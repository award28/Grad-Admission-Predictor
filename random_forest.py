import pandas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

features = ["gre", "gpa", "prestige"]
target = "admit"
data = pandas.read_csv("admissions.csv")
train_features, test_features, train_target, test_target = train_test_split(data[features], data[target])

clf = RandomForestClassifier()
clf.fit(train_features, train_target)
predictions = clf.predict(test_features)
actual = list(test_target)

correct = 0
for i in range(len(predictions)):
    if predictions[i] == actual[i]:
        correct += 1

print(correct / 100)  # split makes 100 training examples
