import read

num = str(read.Read(int, 'a number'))

sum = 0 #variable to add sum of numbers

for digit in num:
	sum += int(digit) ** len(num) #calculating sum of number raised to length of number

if sum == int(num):
	print(num, 'is an amstrong number') #printing true case
else :
	print(num, 'is not an amstrong number') #printing false case
