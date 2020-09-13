import read

lst = read.ReadList()

print(lst)
lst[0],lst[-1] = lst[-1],lst[0]
print(lst)
