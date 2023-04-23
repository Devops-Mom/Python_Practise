# student_marks.csv contains the marks and other details for some students.
# Write a python program to:
# 1- Open the file in read mode
# 2- Create a dictionary from the given data
# 3- Add a new field to the dictionary `total_marks` and store the total marks of the students.
# 4- Add a new field to the dictionary `Average` and store the average marks of the students.
# 5- Create a new file and write this information to the new file
# (https://www.kaggle.com/arunkumar413/student-marks)

student_record = {}   # empty dictionary

with open("student_marks.csv", "r") as f:
     f.read() # read the content of file

     f.seek(0) #goto the start of file

     d = {}
     keys = f.readline() #read 1st line as it contains keys

     #print(keys)
     '''
     Output:
     Name,Gender,DOB,Maths,Physics,Chemistry,English,Biology,Economics,History,Civics
     '''

     keys = keys.split(",") # remove "," comma between values in keys
     #print(keys)
     '''
     Output:
     ['Name', 'Gender', 'DOB', 'Maths', 'Physics', 'Chemistry', 'English', 'Biology', 'Economics', 'History', 'Civics\n']
     '''
     keys[-1] = keys[-1][:-1] # remove "\n" from list
     #print(keys)
     '''
     Output:
     ['Name', 'Gender', 'DOB', 'Maths', 'Physics', 'Chemistry', 'English', 'Biology', 'Economics', 'History', 'Civics']
     '''
     for key in keys: # Initialize dictionary with the keys
          d[key] = []

     #print(d)

     for line in f.readlines():
          data = line.split(",") # remove "," from line
          data[-1] = data[-1][:-1] # remove "\n" from last field

          #print(data)
          j = 0
          for key in d:
               #print(f'{key} ==>{data[j]}')
               d[key].append(data[j])
               j+=1

     #print(d)

import pprint

pprint.pprint(d)

print("Keys: ")
print(d.keys())  # Print all Keys

print("Values: ")
print(d.values()) # Print all Values

# 3- Add a new field to the dictionary `total_marks` and store the total marks of the students.
# Here, we have 5 students:
# Here, we have 8 subjects:
d['total_marks'] = [0]*5  # returns [0,0,0,0,0]

all_subjects = ['Maths', 'Physics', 'Chemistry', 'English', 'Biology', 'Economics', 'History', 'Civics']
for i in range(5):
          sum_marks = 0
          for subject in all_subjects:
               try:
                    sum_marks += int(d[subject][i])
               except:
                    pass

          d['total_marks'][i] = sum_marks

print(d['total_marks'])

# 4- Add a new field to the dictionary `Average` and store the average marks of the students.

d['average'] = [0]*5

total_subject = len(all_subjects)

for i in range(5):
          d['average'][i] = float (d['total_marks'][i]/total_subject)


print(f"Average : {d['average']}")

# 5- Create a new file and write this information to the new file

pprint.pprint(d)

with open("student_marksheet.csv","w") as f_out:
     header = ','.join([key for key in d.keys()])
     #print(header)
     f_out.write(header+'\n')

     for i in range(5):
          #print(f'{key} ==> {d[key][i]}')
          try:
               row = ','.join([str(d[key][i]) for key in d.keys()])
          except:
               pass
          #print(row)
          f_out.write(row + '\n')



with open("student_marks.csv","r") as f:
     f.readlines()
     print(f)

