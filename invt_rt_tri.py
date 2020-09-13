from read import Read

lim = Read(int, 'Limit')

for i in range(lim, 0, -1): #loop for rows
	print(' ' * (lim - i), end = '') #space in front
	for j in range(i): #loop for columns
		print('*', end  = '')
	print() #new row
