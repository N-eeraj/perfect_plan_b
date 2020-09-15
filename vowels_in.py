import read

str = read.Read(str).lower()

vowels = ['a', 'e','i', 'o', 'u']
vowels_not = [] #to store vowels not in the string

for i in vowels:
	if not read.inList(i, str): #checking if each vowel is in the input
		vowels_not.append(i) #if not in the input, then appending to vowels_not

if vowels_not == []: #if vowels_not is empty then input has all vowels
	print('All vowels are present')
else:
	print(','.join(vowels_not), 'are not present') #joining the list with commas
