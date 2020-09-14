from read import Read

string = Read(str, 'String')
key = Read(str, 'Substring')

if string.find(key) == -1:
	print(key, 'not found in', string)
else:
	print(key, 'found in', string)
