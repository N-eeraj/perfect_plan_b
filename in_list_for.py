import read

lst = read.ReadList()
key = read.Read(str, 'Key to Search')

for i in lst:
	if i == key:
		print(key, 'is in the list')
		exit()
print(key, 'is not in the list')
