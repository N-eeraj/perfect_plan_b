from termcolor import colored
import math #import to get pi value

while True: #infinite loop till a valid input is received
	try: #trying to read valid input
		r = float(input('Enter the number: ')) #valid input read
		break #exiting the loop
	except ValueError: #handling non integer input
		print(colored('Enter a valid integer', 'red'))
	except KeyboardInterrupt: #handling keyboard inerrupt to exit
		print(colored('\nExiting', 'white'))
		exit()

area = round(math.pi * r ** 2, 2) #calculating the area & rounding off to 2 decimal values
per = round(2 * math.pi * r, 2) #calculating the circumference

print('Area of the circle is', area)
print('Perimeter of the circle is', per)
