import pandas
import numpy as np
from collections import OrderedDict
from sklearn.model_selection import train_test_split

# Original data csv from "https://github.com/deedy/gradcafe_data/blob/master/all_uisc_cleanback.csv"
# Modified original by removing first two columns of row id
# Added header found on next line to file
# uni_name,major,degree,season,decision,decision_method,decision_date,decision_timestamp,ugrad_gpa,gre_verbal,gre_quant,gre_writing,is_new_gre,gre_subject,status,post_data,post_timestamp,comments


# Attempted to clean data of major types, but too many outliers
def clean():
    data = pandas.read_csv("data/all/uisc_cleanback.csv")
    with open("data/majors_replace.txt", "r") as file:
        first_line = False
        major = ""
        for line in file:
            if line.strip() == '':
                first_line = True
            elif first_line:
                major = line.strip()
                first_line = False
            else:
                data = data.replace(line.strip(), major)
    data.to_csv("data/all/majors_clean.csv", index=False)


# Filtered out unnecessary features and removed any invalid examples
def filter_all(file_name):
    data = pandas.read_csv("data/all/" + file_name + ".csv")

    # Filter data to only include New GRE scores
    data_new_gre = data[data.is_new_gre == True]

    # Remove unnecessary columns
    headers = ["uni_name", "degree", "decision", "ugrad_gpa", "gre_verbal", "gre_quant", "gre_writing", "status"]
    data_filter_col = data_new_gre[headers]

    # Filter out examples with "Other" in decision and filter out Interview and Wait listed
    data_decision = data_filter_col[data_filter_col["decision"] != "Other"]
    data_decision = data_decision.replace("Interview", np.nan)
    data_decision = data_decision.replace("Wait listed", np.nan)
    # Make decision a binary True False
    data_decision = data_decision.replace("Accepted", True)
    data_decision = data_decision.replace("Rejected", False)

    # Filter out examples with any NaN
    data_no_nan = data_decision.dropna(how='any')

    # Filter out uncommon degrees
    data_degree = data_no_nan[data_no_nan["degree"] != "MEng"]
    data_degree = data_degree[data_degree["degree"] != "MA"]

    # Filter out GPAs above 4 and below 2
    data_gpa = data_degree[data_degree['ugrad_gpa'] <= 4.0]
    data_gpa = data_gpa[data_gpa['ugrad_gpa'] >= 2.0]

    # Write new filtered data set to file
    data_gpa.to_csv("data/filter/" + file_name + ".csv", header=headers, index=False)


# Count how many times each school appears in data
def count_school(directory, file_name):
    data = pandas.read_csv("data/" + directory + '/' + file_name + ".csv")
    counter = {}
    school_count = data.uni_name.value_counts()
    for name, count in school_count.iteritems():
        counter[name] = count
    return OrderedDict(sorted(counter.items(), key=lambda t: t[1], reverse=True))


# Remove any schools that don't appear above threshold
def filter_school(directory, file_name, threshold):
    data = pandas.read_csv("data/" + directory + '/' + file_name + ".csv")
    counter = count_school(directory, file_name)
    first = True
    for name, count in counter.items():
        if count >= threshold:
            uni_frame = data[data.uni_name == name]
            if first:
                uni_frame.to_csv("data/filter/" + file_name + "_uni.csv", index=False)
                first = False
            else:
                uni_frame.to_csv("data/filter/" + file_name + "_uni.csv", header=False, index=False, mode='a')
        else:
            break


# One hot the data
def one_hot(directory, file_name):
    data = pandas.read_csv("data/" + directory + '/' + file_name + ".csv")
    data_new = pandas.get_dummies(data)
    data_new.to_csv("data/" + directory + '/' + file_name + "_one_hot.csv", index=False)


# Split data into train and test, test size is a float of what percent you want size of test data to be
def filter_train_test(directory, file_name, test_size):
    data = pandas.read_csv("data/" + directory + '/' + file_name + ".csv")
    counter = count_school(directory, file_name)
    first = True
    for name, count in counter.items():
        uni_frame = data[data.uni_name == name]
        uni_accept = uni_frame[uni_frame.decision == True]
        uni_reject = uni_frame[uni_frame.decision == False]

        train_accept, test_accept = train_test_split(uni_accept, test_size=test_size)
        train_reject, test_reject = train_test_split(uni_reject, test_size=test_size)

        if first:
            train_accept.to_csv("data/train/" + file_name + ".csv", index=False)
            test_accept.to_csv("data/test/" + file_name + ".csv", index=False)

            train_reject.to_csv("data/train/" + file_name + ".csv", header=False, index=False, mode='a')
            test_reject.to_csv("data/test/" + file_name + ".csv", header=False, index=False, mode='a')

            first = False
        else:
            train_accept.to_csv("data/train/" + file_name + ".csv", header=False, index=False, mode='a')
            test_accept.to_csv("data/test/" + file_name + ".csv", header=False, index=False, mode='a')

            train_reject.to_csv("data/train/" + file_name + ".csv", header=False, index=False, mode='a')
            test_reject.to_csv("data/test/" + file_name + ".csv", header=False, index=False, mode='a')


def main():
    # clean()
    filter_all("grad")
    filter_school("filter", "grad", 100)
    one_hot("filter", "grad_uni")

    filter_train_test("filter", "grad_uni", 0.2)
    one_hot("train", "grad_uni")
    one_hot("test", "grad_uni")


if __name__ == "__main__":
    main()
