import read

def fact(x): #recursive function to calculate factorial
	x_fact = 1 #initializing factorial variable
	if x != 1:
		x_fact = x * fact(x - 1) #calling the recursive function
		return x_fact #return value of the factorial
	return 1 #returning factorial value of 1

num = read.Read(int, 'number')

print(str(num) + '! = ',fact(num)) #printing output along input

#output format :
#	input! = factorial
