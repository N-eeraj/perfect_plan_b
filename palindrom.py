import read

string = read.Read(str, 'String')

rev = string[::-1]

if string.lower() == rev.lower():
	print(string, 'is Palindrome')
else:
	print(string, 'is not Palindrome')
