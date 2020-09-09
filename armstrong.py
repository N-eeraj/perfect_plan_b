from termcolor import colored

while True: #infinite loop till a valid input is received
	try: #trying to read valid input
		num = int(input('Enter the number: ')) #valid input read
		num = str(num)
		break #exiting the loop
	except ValueError: #handling non integer input
		print(colored('Enter a valid integer', 'red'))
	except KeyboardInterrupt: #handling keyboard inerrupt to exit
		print(colored('\nExiting', 'white'))
		exit()

sum = 0

for i in num:
	sum += int(i) ** len(num)

if sum == int(num):
	print('{} is an amstrong number'.format(num))
else :
	print('{} is not an amstrong number'.format(num))
