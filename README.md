# ZoomParticipation

This code was created as a means of automatically analyzing the saved
Zoom chat transcripts for student participation.

It measures the number of times a student comments in the chat thread
and the total number characters they type. What you do with this information
is obviously course and grading rubric specific. I plan on using this
at a minimum to take attendence.

This code considers all the folders in your Zoom folder and only analyzes
those that contain our course name, assuming you set up your reoccuring
Zoom meeting with a consistent name. See the "req_string" variable.

Included here are the chat threads from my first two classes this semester 
(with names changed to protect the innocent) and the output .csv file 
created by this code. 

I welcome feedback.

Python script: Analyse_Zoom_Chats.py
Input files are 'meeting_saved_chat.txt' within the subfolders
Output file: Biological Physics Chat Participation Data.csv

Created on Fri Sep  4 08:41:27 2020
@author: Christopher V. Kelly, cvkelly@wayne.edu
