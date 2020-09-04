# -*- coding: utf-8 -*-
"""
This code was created as a means of automatically analyzing the saved
Zoom chat transcripts for student participation.

It measures the number of times a student comments in the chat thread
and the total number characters they type. What you do with this information
is obviously course and grading rubric specific. I plan on using this
at a minimum to take attendence.

This code considers all the folders in your Zoom folder and only analyzes
those that contain our course name, assuming you set up your reoccuring
Zoom meeting with a consistent name. See the "req_string" variable.

Created on Fri Sep  4 08:41:27 2020
GNU GENERAL PUBLIC LICENSE
@author: Christopher V. Kelly, cvkelly@wayne.edu
"""
# %%

import numpy as np
from os import listdir, getcwd
import csv

# %%

student_names = ['Nora Jones',
                 'Jimmy Page',
                 'Frederic Chopin',
                 'Stevie Ray Vaughan',
                 'Neil Young',
                 'Mandarin Orange',
                 'Carolina Chocolate Drops',
                 'Alice Cooper',
                 'Eric Clapton']  # must be unique

# super-folder that contains all Zoom chats saved as .txt files
# in which there is one sub-folder per class time
fold_in = getcwd()

# a required text string within the sub-folder
# folders that don't have this string will be ignored
req_string = 'Biological Physics'

# folder and file name into which the resulting CSV file will be saved
fold_save = fold_in
file_save = req_string + ' Chat Participation Data.csv'

# name of .txt file saved by Zoom
file = 'meeting_saved_chat.txt'

# %% initialize some parameters
num_comments = np.zeros((len(student_names),1000))
num_total_char = np.zeros((len(student_names),1000))
class_num = -1
class_date_list = []
t1 = ' From '
t2 = ' : '

# %% analyze all chat transcripts
for fold2 in listdir(fold_in):  # loop over each subfolder
    a = fold2.find(req_string)
    if a > -1:  # keep only those that are for your class of interest
        class_num += 1
        class_date_list.append(fold2[:11])
        f = open(fold_in+'\\'+fold2+'\\'+file,'r')
        line = '00'
        while len(line)>0: # keep going as long as there are new lines in the transcript
            line = f.readline()
            for snum,stud in enumerate(student_names):  # loop over each student
                if line.find(t1+stud)>0 or line.find(t1+' '+stud)>0:
                    num_comments[snum,class_num] += 1
                    num_char = len(line)-line.find(t2)-2
                    num_total_char[snum,class_num] += num_char
        f.close()
        # print(class_date)

num_comments = num_comments[:,:class_num+1] # reduce the array size for the appropriate number of classes
num_total_char = num_total_char[:,:class_num+1] # reduce the array size for the appropriate number of classes

# %% Have a quick look at the data to ensure it makes sense
# You may want to comment out these lines if you have a large class
print('num_comments')
print(num_comments)

print('num_total_char')
print(num_total_char)


# %% Write the results in to a CSV file that can be easily viewed and analyzed with Excel
fwrite1 = open(fold_save + '\\' + file_save,'w',newline='')
fwrite2 = csv.writer(fwrite1)

# write the data for the number of chats per student
fwrite2.writerow(['NUMBER OF CHATS']+class_date_list)
for snum,stud in enumerate(student_names):
    fwrite2.writerow([stud]+list(num_comments[snum,:]))
fwrite2.writerow([' ']*(num_comments.shape[1]+1))

# write the data for the number of characters per student
fwrite2.writerow(['NUMBER OF CHARACTERS']+class_date_list)
for snum,stud in enumerate(student_names):
    fwrite2.writerow([stud]+list(num_total_char[snum,:]))

fwrite1.close()
