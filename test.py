# import os, sys, glob

# mypath = "train"
# img_names=[]
# img_classes=[]  
# classes = ["LAG", "DOL", "OTHER", "BET", "ALB", "NoF", "YFT", "SHARK"]
# for cl in classes:
#     class_dir =mypath+ "/"+ cl + "/"
#     filepaths = glob.glob(class_dir + "*.jpg")
#     for filepath in filepaths:
#         img_names.append(os.path.basename(filepath)[4:-4])
#         img_classes.append(str(classes.index(cl)))
#         break
# print(img_classes)
# print(img_names)
# from os import walk
# mypath = "TEST"

# f = []
# for (dirpath, dirnames, filenames) in walk(mypath):
#     f.extend(filenames)
#     # print(filenames)
#     break
# print(f[0],f[1])


# import pandas as pd
# import csv   
# # reading the csv file
# # df = pd.read_csv("submission.csv")
# df = pd.read_csv('submission.csv', delim_whitespace=True)
# # df['image'] = df['image'].replace({'image': 'img'})
  
# # writing into the file
# # df.to_csv("AllDetails.csv", index=False)
# r = csv.reader(open('submission.csv')) # Here your csv file
# lines = list(r)
# writer = csv.writer(open('newsubmission.csv', 'w'))
# writer.writerows(lines)
# for tmp in lines:
#     # print(tmp[0])
#     tmp[0] =  tmp[0].replace("image", "img")
#     # print(tmp[0])
# writer = csv.writer(open('newsubmission.csv', 'w'))
# writer.writerows(lines)
#     # break
# # print(lines)
from tempfile import NamedTemporaryFile
import shutil
import csv

filename = 'submission.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['image','ALB','BET','DOL','LAG','NoF','OTHER','SHARK','YFT']

with open(filename, 'r') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        # if row['ID'] == str(stud_ID):
        #     print('updating row', row['ID'])
        #     row['Name'], row['Course'], row['Year'] = stud_name, stud_course, stud_year
        row = {fields[0]: row[fields[0]].replace("image", "test_stg2/image"), 
        fields[1]: row[fields[1]], 
        fields[2]: row[fields[2]],
        fields[3]: row[fields[3]],
        fields[4]: row[fields[4]],
        fields[5]: row[fields[5]],
        fields[6]: row[fields[6]],
        fields[7]: row[fields[7]],
        fields[8]: row[fields[8]]}
        writer.writerow(row)

shutil.move(tempfile.name, 'newsubmission.csv')
# import csv

with open('newsubmission.csv') as input, open('newsubmission1.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)

    