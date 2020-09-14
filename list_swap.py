import read

lst  = read.ReadList()

pos1 = read.Read(int,'First Position') - 1
pos2 = read.Read(int,'Second Position') - 1

lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

print(lst)
