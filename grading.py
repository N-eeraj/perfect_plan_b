import read
import numpy as np

#reading & calculating averages of all marks
asmnt = np.array(read.ReadList(int, 'Assignment Marks')).mean()
test = np.array(read.ReadList(float, 'Test Marks')).mean()
lab = np.array(read.ReadList(float, 'Lab Marks')).mean()

total = asmnt * 0.1 + test * 0.7 + lab * 0.2 #10% Assignments, 70% Test, 20% Lab marks

#grading
if total >= 90:
	grade = 'A'
elif total >= 80:
	grade = 'B'
elif total >= 70:
	grade = 'C'
elif total >= 60:
	grade = 'D'
else:
	grade = 'E'

print('Grade:', grade)
