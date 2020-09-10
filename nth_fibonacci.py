import read

pos = read.Read(int, 'Position')
if pos < 3: #1st or 2nd position
	i = pos - 1
else:
	i = -1

print(read.fib(pos)[i])
