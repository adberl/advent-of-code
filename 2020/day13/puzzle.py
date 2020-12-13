from math import ceil

with open('input', 'r') as f:
	lines = [i.strip() for i in f.readlines()]	


def partone():
	time = int(lines[0])
	ids = lines[1].split(',')

	for busid in ids:
		if busid == 'x':
			continue
		busid = int(busid)
		nearest = ceil(time / busid)
		
		print(busid, time - nearest*busid)	
