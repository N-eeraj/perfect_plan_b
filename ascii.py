import read

try:
	print(ord(read.Read(str, 'character'))) #finding ascii value
except TypeError: #handling input length not equal to 1
	read.error('Input should be 1 character long')
