import read

num1 = read.Read(int, 'Lower Limit')
num2 = read.Read(int, 'Upper Limit')

for num in range(num1, num2 + 1):
	if read.prime(num): #true if num is prime
		print(num)
