from termcolor import colored

def Read(data_type, msg):
	while True: #infinite loop till a correct input is recieved
		try: #reading input
			ip = data_type(input('Enter ' + msg + ': '))
			break #exiting loop on getting valid input
		except ValueError: #handling undesired input data type
			print(colored('\nEnter a valid number\n', 'red')) #red error message
		except KeyboardInterrupt: #handling keyboard interrupt
			print(colored('\n\nExiting', 'white')) #white exit msg
			exit() #exit the program
	return ip

def prime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True
