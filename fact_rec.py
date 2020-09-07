from termcolor import colored

def fact(x):
	x_fact = 1
	if x != 1:
		x_fact = x * fact(x - 1)
		return x_fact
	return 1

while True:
	try:
		num = int(input('Enter the number: '))
		break
	except ValueError:
		print(colored('Enter a valid integer', 'red'))
	except KeyboardInterrupt:
		print(colored('\nExiting', 'white'))
		exit()

print(fact(num))
