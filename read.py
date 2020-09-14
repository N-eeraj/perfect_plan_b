from termcolor import colored

def Read(data_type, msg = 'Input'): #function to read an input with specified datatype & input message
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

def error(msg = 'Invalid Input'): #funtion to print red error message
	print(colored(msg, 'red'))

def prime(num): #function to check if a number is prime or not
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

def fib(limit): #funtion to create a fibonacci list
	fib_list = []
	if limit < 1: #invalid input
		error('Invalid Position')
		exit()
	else:
		fib_list.append(0) #1st position
		fib_list.append(1) #2nd position
		for i in range(2, limit):
			fib_list.append(fib_list[-2] + fib_list[-1]) #updating the fibonacci list
	return fib_list

def Pow(limit, pow):
	sum = 1
	for i in range(2, limit + 1):
		sum += i ** pow
	return sum

def ReadList(d_type = str, msg = 'Input'):
	lst = []
	while True:
		ip = Read(str, msg).lower()
		if ip == 'done':
			return lst
		try:
			lst.append(d_type(ip))
		except:
			error()
			continue

def inList(key, list):
	if key in list:
		return True
	return False
