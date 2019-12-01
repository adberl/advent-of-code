import re
import numpy as np

lines = open('input.txt', 'r').readlines()

fabric = np.zeros((1000, 1000), dtype=int)
total = 0

ranges_list = []

for line in lines:
	splitl = line.split()
#	print(split)
	
	top2rect = int(splitl[2].split(',')[1][0:-1])
	left2rect = int(splitl[2].split(',')[0])

	sizes = [int(item) for item in splitl[3].split('x')] # 0 - x axis; 1 = y axis
		
	range_xaxis = range(left2rect, left2rect + sizes[0])
	range_yaxis = range(999 - top2rect - sizes[1], 999 - top2rect)
		
	ranges_list.append([int(splitl[0][1:]), range_xaxis, range_yaxis])
		
	for i in range_xaxis:
		for j in range_yaxis:
			fabric[i][j] += 1
			
for a in np.nditer(fabric):
	if(a > 1): 
		total += 1

print(total)

for id_range in ranges_list:
	found_overlapping = 0
	for i in id_range[1]:
		for j in id_range[2]:
			if(fabric[i][j] > 1):
				found_overlapping = 1
				break
	
	if(found_overlapping == 0):
		print(id_range[0])
		break
	
