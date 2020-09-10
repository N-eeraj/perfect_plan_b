import read

lim = read.Read(int, 'Limit')

for i in read.fib(lim):
	print(i, end = ' ')
print('')
