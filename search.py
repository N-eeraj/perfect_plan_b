import read

string = read.Read(str, 'String')
key = read.Read(str, 'Substring')

if read.inList(key, string):
	print(key, 'found in', string)
else:
	print(key, 'not found in', string)
