import csv
import pandas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from collections import Counter
from itertools import imap
from operator import  itemgetter

with open('all_filter_new_gre.csv') as f:
    next(f) # skip the header
    cn = Counter(imap(itemgetter(2), csv.reader(f)))
    cn.most_common()
    for t in cn.most_common():
        print("{} appears {} times".format(*t))


