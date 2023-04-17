# student_marks.csv contains the marks and other details for some students.
# Write a python program to:
# 1- Open the file in read mode
# 2- Create a dictionary from the given data
# 3- Add a new field to the dictionary `total_marks` and store the total marks of the students.
# 4- Add a new field to the dictionary `Average` and store the average marks of the students.
# 5- Create a new file and write this information to the new file
# (https://www.kaggle.com/arunkumar413/student-marks)

student_record = {} # empty dictionary

with open('student_marks.csv','r') as f:
     f.read() #read file once

     f.seek(0) # go to first postion again

     keys = f.readline() # read first line of file and treat them as keys.

     keys = keys.split(',')
     keys[-1] =  keys[-1][:-1]

     for key in keys:
          student_record[key] = []

     print(student_record) # print dictionaries with keys

     for line in f.readlines():
          data = line.split(',')
          data[-1] = data[-1][:-1]

          j=0
          for key in student_record:
               student_record[key].append(data[j])
               j+=1



     print(student_record) #print entire dictionary

# Create new field "total_marks"
     student_record['total_marks']=[]
     for key,data in student_record.items():
          total = data
     print(student_record)