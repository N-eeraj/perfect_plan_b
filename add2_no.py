try:
	num1 = float(input('Enter 1st Number: '))
	num2 = float(input('Enter 2nd Number: '))
except:
	print('\nEnter a valid number\n')
	exit()

result = num1 + num2

print(result)
