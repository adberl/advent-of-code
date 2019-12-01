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
			
max_g_id = 0			
guard_id = 0
max_mins = 0

for minute_list in guard:
	total_mins = 0
	for minute in minute_list:
		total_mins += minute
		
	if(total_mins > max_mins):
		max_mins = total_mins
		max_g_id = guard_id
	guard_id += 1
	
print(max_g_id, np.argmax(guard[max_g_id]))
