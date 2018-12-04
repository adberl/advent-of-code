import re
import numpy as np

lines = open('input.txt', 'r').readlines()
lines.sort()

guard = np.zeros((9999, 60), dtype=int)
start = 0

for line in lines:
	split_line = line.split(' ')	
	if(len(split_line) < 3): continue
	minute=int(split_line[1][3:5])
		
	if split_line[2][0] == 'G': # guard number
		current = int(split_line[3][1:])
	elif split_line[2][0] == 'f':
		start = minute
	else:
		for i in range(start, minute):
			guard[current][i] += 1
	
max_min_value = 0
max_min_id = 0
max_guard_id = 0

for ids in [89, 151, 541, 857, 1009, 1283, 1381, 1571, 1697, 1723, 2251, 2411, 2473, 2963, 3137, 3209, 3259, 3469, 3511, 3533]:
	if(max(guard[ids]) > max_min_value):
		max_min_value = max(guard[ids])
		max_min_id = np.argmax(guard[ids])
		max_guard_id = ids
		
print(max_guard_id, max_min_id)
