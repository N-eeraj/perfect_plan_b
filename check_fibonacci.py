import read

num = read.Read(int, 'Number')

if num < 0: #show error in invalid number
	read.error('Invalid Number')
elif num < 2: #0 & 1 are fibonacci numbers
	print(num, 'is a Fibonacci number')
else:
	seed1, seed2 = 0, 1
	for i in range(num): #checking if number is fibonacci
		if seed1 + seed2 == num:
			print(num, 'is a Fibonacci number')
			exit()
		else:
			seed1, seed2 = seed2, seed1 + seed2
	print(num, 'is not a Fibonacci number')
