from read import Read

string = Read(str)

for i in string.split():
	if len(i) % 2 == 0:
		print(i)
