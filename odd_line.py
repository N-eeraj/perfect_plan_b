with open('file1.txt', 'r') as file: #opening file in read mode
	lines = file.readlines() #reading file into lines

for line_no, line in enumerate(lines): #iterating over each line in lines & it's index
	if line_no % 2 == 0: #checking for all odd line numbers
		print(line, end = '')
