import csv

# link to data, https://github.com/deedy/gradcafe_data, add header to first line in order to work correctly 
# rowid,uni_name,major,degree,season,decision,decision_method,decision_date,decision_timestamp,ugrad_gpa,gre_verbal,gre_quant,gre_writing,is_new_gre,gre_subject,status,post_data,post_timestamp,comments
headers = ["rowid1","rowid2","uni_name","major","degree","season","decision",
           "decision_method","decision_date","decision_timestamp",
           "ugrad_gpa","gre_verbal","gre_quant","gre_writing",
           "is_new_gre","gre_subject","status","post_data",
           "post_timestamp","comments"]

read = open("all_filter_new_gre.csv",'r')
write = open("school_filter_new_gre.csv",'w')
name = open("university.txt", 'r')

common = []
for line in name:
	common.append(line.strip('\n'))

print common

reader = csv.DictReader(read)
writer = csv.DictWriter(write, fieldnames=headers)
writer.writeheader()
for row in reader:
    if row["uni_name"] in common: 
        writer.writerow(row)

read.close()
write.close()
