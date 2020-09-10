import read

def is_prime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

num1 = read.Read(int, 'Lower Limit')
num2 = read.Read(int, 'Upper Limit')

for num in range(num1, num2 + 1):
	if is_prime(num):
		print(num)
