import math

file = open('input.txt', 'r')

total_fuel = 0
for line in file.readlines():
	initial = int(line)
	before = initial
	div1 = math.floor(initial / 3) - 2
	
	while(True):
#		print(div1)
		if(div1 <= 0):
#			total_fuel += before
#			print('b4: ', before)
			break
		else:
			total_fuel += div1
			before = div1
			div1 = math.floor(div1 / 3) - 2
#		print('tf: ', total_fuel)
			
print(total_fuel)
