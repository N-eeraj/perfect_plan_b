import read

num = read.Read(int, 'number')

fact = num #initalizing factorial variable
for i in range(2, num): #iterating over the input variable
	fact *= i

print(str(num) + '! = ',fact) #print output along input
