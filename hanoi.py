import read
import os

def tower(twr):
	for i in twr:
		print(i)
def show():
	os.system('clear')
	for i,j in enumerate(twrs):
		tower(j)
		print('Tower', i + 1)
		print()

global limit
limit  = read.Read(int, 'Limit')

twrs = [[], [], []]

for i in range(1, limit + 1):
	twrs[0].append(i)

win = twrs[0]

show()

while win not in twrs[1:]:
	twr_s = read.Read(int, 'Tower number to select') - 1
	if not (-1 < twr_s < 3):
		read.error('Enter number in (1,2,3)')
		continue
	twr_d = read.Read(int, 'Destination tower number') - 1
	if not (-1 < twr_s < 3):
		read.error('Enter number in (1,2,3)')
		continue
	try:
		if twrs[twr_d] == []:
			pass
		elif twrs[twr_d][0] < twrs[twr_s][0]:
			read.error("Can't place larger number on smaller number")
			continue
		twrs[twr_d].insert(0, twrs[twr_s].pop(0))
		show()
	except IndexError:
		read.error("Can't select from empty tower")
		continue

print('You Won!!')
