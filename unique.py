import read

str = read.Read(str, 'String Input')

chars = []
for char in str:
	if char not in chars:
		chars.append(char)
	else:
		print(str, 'contains duplicates')
		exit()

print(str, "doesn't contain any duplicates")
