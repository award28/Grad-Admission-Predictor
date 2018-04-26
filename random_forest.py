import pandas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

features = ["uni_name","ugrad_gpa", "gre_verbal", "gre_quant"]
target = "decision"
data = pandas.read_csv("school_filter_new_gre.csv")

le = preprocessing.LabelEncoder()
column_name = "uni_name"
for column_name in data.columns:
    if data[column_name].dtype == object:
        data[column_name] = le.fit_transform(data[column_name])
    else:
        pass
print(data)

train_features, test_features, train_target, test_target = train_test_split(data[features], data[target])

clf = RandomForestClassifier()
clf.fit(train_features, train_target)
print(clf)

predictions = clf.predict(test_features)
actual = list(test_target)

correct = 0.0
for i in range(len(predictions)):
    if predictions[i] == actual[i]:
        correct += 1.0

print(correct / len(predictions))
