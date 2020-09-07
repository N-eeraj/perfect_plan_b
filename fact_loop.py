from termcolor import colored

while True: #infinite loop till a valid input is received
	try: #trying to read valid input
		num = int(input('Enter the number: ')) #valid input read
		break #exiting the loop
	except ValueError: #handling non integer input
		print(colored('Enter a valid integer', 'red'))
	except KeyboardInterrupt: #handling keyboard inerrupt to exit
		print(colored('\nExiting', 'white'))
		exit()

fact = num #initalizing factorial variable
for i in range(2, num): #iterating over the input variable
	fact *= i

print(str(num) + '! = ',fact) #print output along input
