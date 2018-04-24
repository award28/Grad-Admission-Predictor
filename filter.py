import csv

# link to data, https://github.com/deedy/gradcafe_data, add header to first line in order to work correctly 
# rowid,uni_name,major,degree,season,decision,decision_method,decision_date,decision_timestamp,ugrad_gpa,gre_verbal,gre_quant,gre_writing,is_new_gre,gre_subject,status,post_data,post_timestamp,comments
headers = ["rowid","uni_name","major","degree","season","decision",
           "decision_method","decision_date","decision_timestamp",
           "ugrad_gpa","gre_verbal","gre_quant","gre_writing",
           "is_new_gre","gre_subject","status","post_data",
           "post_timestamp","comments"]

read = open("cs_clean.csv",'r',newline='')
write = open("cs_filtered.csv",'w',newline='')

reader = csv.DictReader(read)
writer = csv.DictWriter(write, fieldnames=headers)
writer.writeheader()
for row in reader:
    if (row["decision"] == "Accepted" or row["decision"] == "Rejected") and (row["ugrad_gpa"] != '') and (row["gre_quant"] != ''):
        writer.writerow(row)

read.close()
write.close()
