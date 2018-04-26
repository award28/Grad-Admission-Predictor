import pandas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# data = pandas.read_csv("all_filter_col.csv")
# column_name = list(data)
# features = column_name[1:-1]
# target = column_name[0]
# train_features, test_features, train_target, test_target = train_test_split(data[features], data[target],
#                                                                              test_size=0.2, random_state=42)

dtype = {"decision": bool, "ugrad_gpa": float, "gre_verbal": int, "gre_quant": int, "gre_writing": float}
train = pandas.read_csv("train_one_hot.csv", dtype=dtype)
test = pandas.read_csv("test_one_hot.csv", dtype=dtype)

column_name = list(train)
features = column_name[1:-1]
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
