import pandas
import numpy as np
from collections import OrderedDict
from sklearn.model_selection import train_test_split

header_str = "uni_name,degree,decision,ugrad_gpa,gre_verbal,gre_quant,gre_writing,status\n"
headers = ["uni_name", "degree", "decision", "ugrad_gpa", "gre_verbal", "gre_quant", "gre_writing", "status"]
dtype = {"uni_name": "category", "degree": "category", "decision": bool, "ugrad_gpa": float,
         "gre_verbal": int, "gre_quant": int, "gre_writing": float, "status": "category"}


def filter_all():
    data = pandas.read_csv("all_uisc_cleanback.csv")

    data_new_gre = data[data.is_new_gre == True]

    data_filter_col = data_new_gre[headers]

    data_decision = data_filter_col[data_filter_col["decision"] != "Other"]
    data_decision = data_decision.replace("Interview", np.nan)
    data_decision = data_decision.replace("Wait listed", np.nan)

    data_no_nan = data_decision.dropna(how='any')

    data_degree = data_no_nan[data_no_nan["degree"] != "MEng"]
    data_degree = data_degree[data_degree["degree"] != "MA"]

    data_decision_binary = data_degree.replace("Accepted", True)
    data_decision_binary = data_decision_binary.replace("Rejected", False)
    # data_decision_binary = data_decision_binary.replace("Wait listed", False)

    data_below_4 = data_decision_binary[data_decision_binary['ugrad_gpa'] <= 4.0]
    data_above_2 = data_below_4[data_below_4['ugrad_gpa'] >= 2.0]
    data_above_2.to_csv("all_filter_col.csv", header=headers, index=False)


def count_school(file_name):
    data = pandas.read_csv(file_name)
    counter = {}
    school_count = data.uni_name.value_counts()
    for name, count in school_count.iteritems():
        counter[name] = count
    return OrderedDict(sorted(counter.items(), key=lambda t: t[1], reverse=True))


def filter_school(counter, threshold):
    data = pandas.read_csv("all_filter_col.csv")
    with open("all_filter_uni.csv", 'a') as output:
        output.write(header_str)
        for name, count in counter.items():
            if count >= threshold:
                uni_frame = data[data.uni_name == name]
                uni_frame.to_csv(output, header=False, index=False)


def filter_train_test(counter, test_size):
    data = pandas.read_csv("all_filter_uni.csv")
    with open("train.csv", 'a') as train, open("test.csv", 'a') as test:
        train.write(header_str)
        test.write(header_str)
        for name, count in counter.items():
            uni_frame = data[data.uni_name == name]
            uni_accept = uni_frame[uni_frame.decision == True]
            uni_reject = uni_frame[uni_frame.decision == False]

            train_accept, test_accept = train_test_split(uni_accept, test_size=test_size)
            train_accept.to_csv(train, header=False, index=False)
            test_accept.to_csv(test, header=False, index=False)

            train_reject, test_reject = train_test_split(uni_reject, test_size=test_size)
            train_reject.to_csv(train, header=False, index=False)
            test_reject.to_csv(test, header=False, index=False)


def one_hot(file_name):
    data = pandas.read_csv(file_name + ".csv")
    data_new = pandas.get_dummies(data)
    data_new.to_csv(file_name + "_one_hot.csv", index=False)


def main():
    filter_all()
    counter = count_school("all_filter_col.csv")
    filter_school(counter, 100)

    counter = count_school("all.csv")
    filter_train_test(counter, 0.2)
    one_hot("train")
    one_hot("test")
    one_hot("all_filter_uni")


if __name__ == "__main__":
    main()
