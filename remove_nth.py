import read

#reading list
lst = read.ReadList()
print(lst)

#reading item to find & check if it is int the list
key = read.Read(str,'item to remove')
if key not in lst:
	read.error(key + ' is not in the list')
	exit()

#reading occurrence number & checking if there are that many occurrences of key in the list
pos = read.Read(int, 'occurrence number')
if lst.count(key) < pos:
	read.error('{} does not have {} occurrences'.format(key, pos))
	exit()

count = 0

for index, item in enumerate(lst): #enumerate to get index
	if item == key:
		count += 1 #counting number of occurrences
		if count == pos:
			lst.pop(index)  #removing the key
			break

print(lst)
