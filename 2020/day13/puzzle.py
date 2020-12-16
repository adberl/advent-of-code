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
		
		
def parttwo():
	ids = lines[1].split(',')
	working = True
	timestamp = 150000000000000 # if you start it at 0, it will run for an hour with no result
	relative_timestamp = 0
	busids = []
	for idx, busid in enumerate(ids):
		if(busid != 'x'):
			busids.append((int(busid), idx))
	while working:
		timestamp += 1
		for busid in busids:
			if ((timestamp + busid[1]) % busid[0]) == 0:
				if busid == busids[-1]:
					print(timestamp)
					working = False
			else:
				break

parttwo()
