
import os
import glob
from natsort import natsorted
import os.path
from os import path
classes = ['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']

root_dir = 'train'
# # Get list of all files in a given directory sorted by name
# list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
#                         os.listdir(dir_name) ) )
# # Iterate over sorted list of files and print the file paths 
# # one by one.
# for file_path in list_of_files:
#      if file_path.endswith(".jpg"):
#         f1.write('data/IOC/train/{}'.format(file_path))
#         f1.write("\n")
for tmpclass in classes:
    dir_name = root_dir+'/'+tmpclass
    list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
            os.listdir(dir_name) ) )
    for file_path in list_of_files:
        if file_path.endswith(".jpg"):
            # print(os.path.isfile('train/'+tmpclass+'/'+file_path[:-4]+'.txt'))
            # path.exists('train/'+tmpclass+'/'+file_path[:-4])
            if(os.path.isfile('train/'+tmpclass+'/'+file_path[:-4]+'.txt') == False):
                fp = open('train/'+tmpclass+'/'+file_path[:-4]+".txt", "w")
                # fp = open('result/'+file_path[:-4]+".txt", "w")
            