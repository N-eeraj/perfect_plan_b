from termcolor import colored #importing colored module from termcolor library

while True:
	try: #trying to read required vslues & convert it to float
		principle = float(input('Enter principle amount: '))
		time  = float(input('Enter time: '))
		rate  = float(input('Enter rate of interest: '))
		break
	except ValueError: #error message for non float input
		print(colored('Error Invalid Entry\nEnter a valid number', 'red'))
	except KeyboardInterrupt: #exiting on keyboard interrupt
		print(colored('\nExiting', 'white'))
		exit()

si = (principle * time * rate) / 100 #equation to find simple interest

print('\nSimple interest for principle amount {}, for {} time, at an interest rate of {} is {}'.format(principle, time, rate, si))
