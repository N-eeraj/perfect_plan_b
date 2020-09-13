import read

lst = read.ReadList()

print(lst)
lst[0],lst[-1] = lst[-1],lst[0] #swaping 1st & last elements
print(lst)
