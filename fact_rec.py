from termcolor import colored #module for colored output

def fact(x): #recursive function to calculate factorial
	x_fact = 1 #initializing factorial variable
	if x != 1:
		x_fact = x * fact(x - 1) #calling the recursive function
		return x_fact #return value of the factorial
	return 1 #returning factorial value of 1

while True: #infinite loop till a valid input is received
	try: #trying to read valid input
		num = int(input('Enter the number: ')) #valid input read
		break #exiting the loop
	except ValueError: #handling non integer input
		print(colored('Enter a valid integer', 'red'))
	except KeyboardInterrupt: #handling keyboard inerrupt to exit
		print(colored('\nExiting', 'white'))
		exit()

print(str(num) + '! = ',fact(num)) #printing output along input

#output format :
#	input! = factorial
