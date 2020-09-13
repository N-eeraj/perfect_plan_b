import read

lst = read.ReadList(int)

cb = []
for i in lst:
	cb.append((i, i ** 3)) #adding tuples to list

print(cb)
