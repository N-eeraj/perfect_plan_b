import read

lst = read.ReadList()

key = read.Read(str, 'Key to Search')

if read.inList(key, lst):
	print(key, 'is in the list')
else:
	print(key, 'is not in the list')
