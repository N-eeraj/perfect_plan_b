from read import Read

lst = []
dict = {}

while True:
	key = Read(str, 'Key')
	if key.lower() == 'done':
		break
	value = Read(str, 'Value(s)').split()
	lst.append((key, value))

print(lst)

for i, j in lst:
	dict[i] = j

print(dict)
