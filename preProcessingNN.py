import pandas as pd
import numpy as np
data = pd.read_excel("all.xls")

#data is with University
data = data.drop('comments',1)
data = data.drop('post_date', 1)
data = data.drop('post_timestamp', 1)
data = data.drop('decision_date', 1)
data = data.drop('decision_timestamp', 1)
data = data.drop('is_new_gre', 1)
data = data.drop('gre_subject', 1)

#data is when I removed university along with other features
data = data.drop('uni_name', 1)

data.to_pickle("data.pickle")
data = data.drop('rowid', 1)
data = data.drop('season', 1)
data = data.drop('major', 1)
data = data.replace(np.nan, 0)
data = data.replace('Accepted', 1)
data = data.replace('Rejected', 0)
data = data.replace('Other', 0)
data = data.replace('Interview', 0)
data = data.replace('Wait listed', 0)

columns = {'status':[], 'decision_method':[], 'degree':[]}

for idx, row in data.iterrows():
    for c in columns:
        val = data.loc[idx, c]
        if val not in columns[c]:
            columns[c].append(val)

for key, l in columns.items():
    for i, word in enumerate(l, start=1):
        data = data.replace(word, i)

data.to_pickle("data_minusUniv.pickle")
