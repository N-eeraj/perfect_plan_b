
import read

str = read.Read(str)
unique = ''

for i in str:
	if i not in unique:
		unique += i

print(unique)
