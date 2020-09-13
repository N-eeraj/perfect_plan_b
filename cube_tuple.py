import read

lst = read.ReadList(int)

cb = []
for i in lst:
	cb.append((i, i ** 3))

print(cb)
