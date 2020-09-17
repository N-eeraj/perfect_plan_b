import read
import os

def tower(twr):
	for i in twr:
		print(i)
	print()

def show():
	os.system('clear')
	for i in twrs:
		tower(i)

global limit
limit  = read.Read(int, 'Limit')

twrs = [[], [], []]

for i in range(1, limit + 1):
	twrs[0].append(i)

win = twrs[0]

show()

while win not in twrs[1:]:
	twr_s = read.Read(int, 'Tower number to select') - 1
	twr_d = read.Read(int, 'Destination tower number') - 1
	if (twr_s not in [0, 1, 2] and twr_d not in [0, 1, 2]):
		read.error('Enter number in (1,2,3)')
		continue
	if twrs[twr_d] == []:
		pass
	elif twrs[twr_d][0] < twrs[twr_s][0]:
		read.error("Can't place larger number on smaller number")
		continue
	twrs[twr_d].insert(0, twrs[twr_s].pop(0))
	show()
