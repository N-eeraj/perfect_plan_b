import read

string = read.Read(str, 'String')

rev = string[::-1] #reversing string

if string.lower() == rev.lower(): #checking if input string is same as it's reverse
	print(string, 'is Palindrome')
else:
	print(string, 'is not Palindrome')
