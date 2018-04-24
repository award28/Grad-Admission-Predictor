import pandas as pd
data = pd.read_excel("all.xls")

#data is with University
data = data.drop('comments',1)
data = data.drop('post_date', 1)
data = data.drop('post_timestamp', 1)
data = data.drop('decision_date', 1)
data = data.drop('decision_timestamp', 1)
data = data.drop('is_new_gre', 1)
data = data.drop('gre_subject', 1)

#data_minusUniv is when I removed university along with other features
data_minusUniv = pd.read_excel("all.xls")

data_minusUniv = data_minusUniv.drop('comments',1)
data_minusUniv = data_minusUniv.drop('post_date', 1)
data_minusUniv = data_minusUniv.drop('post_timestamp', 1)
data_minusUniv = data_minusUniv.drop('decision_date', 1)
data_minusUniv = data_minusUniv.drop('decision_timestamp', 1)
data_minusUniv = data_minusUniv.drop('is_new_gre', 1)
data_minusUniv = data_minusUniv.drop('gre_subject', 1)
data_minusUniv = data_minusUniv.drop('uni_name', 1)
