from read import ReadList

lst = ReadList()
rev = []
ln = len(lst)

for i in range(ln):
	rev.append(lst[ln - i - 1])

print('Input:', lst)
print('Output:', rev)
