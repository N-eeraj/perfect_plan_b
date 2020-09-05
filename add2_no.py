from termcolor import colored

while True:
	try:
		num1 = float(input('Enter 1st Number: '))
		num2 = float(input('Enter 2nd Number: '))
		break
	except ValueError:
		print(colored('\nEnter a valid number\n', 'red'))
	except KeyboardInterrupt:
		print('\n\nExiting')
		exit()

result = num1 + num2

print(result)
