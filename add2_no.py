from termcolor import colored #module to give color

while True: #infinite loop till a correct input is recieved
	try: #reading numbers
		num1 = float(input('Enter 1st Number: '))
		num2 = float(input('Enter 2nd Number: '))
		break #exiting loop on getting valid input
	except ValueError: #handling non number input
		print(colored('\nEnter a valid number\n', 'red')) #red error message
	except KeyboardInterrupt: #handling keyboard interrupt
		print(colored('\n\nExiting', 'white')) #white exit msg
		exit() #exit the program

result = num1 + num2

print('Sum of {} & {} is {}'.format(num1, num2, result)) #printing result along with inputs
