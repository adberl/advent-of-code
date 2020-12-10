with open('input', 'r') as f:
	lines = [i.strip() for i in f.readlines()]
	
passes = []

for boardingpass in lines:
	lower = 0
	upper = 127
	row = 0
	column = 0
	
	for i in range(7):
		if(i == 6):
			if(boardingpass[i] == 'B'):
				row = upper
			else:
				row = lower
		else:
			if(boardingpass[i] == 'B'):
				lower = int((upper + lower)/2) + 1
			else:	
				upper = int((upper + lower)/2)

	lower = 0
	upper = 7
	
	for i in range(3):
		if(i == 2):
			if(boardingpass[i+7] == 'R'):
				column = upper
			else:
				column = lower
		
		else:
			if(boardingpass[i+7] == 'R'):
				lower = int((upper + lower)/2) + 1
			else:
				upper = int((upper + lower)/2)

	passes.append({'row': row, 'column': column})
	
#highestid = max(passes, key=lambda p: p['row'] * 8 + p['column'])
#print(highestid['row'] * 8 + highestid['column'])

passes.sort(key=lambda x: x['row'] * 8 + x['column'])

def retpid(bpass):
	return bpass['row'] * 8 + bpass['column']

for pid in range(1, len(passes) - 1):
	previous = retpid(passes[pid-1])
	current = retpid(passes[pid])
	next = retpid(passes[pid+1])
	
	# its gonna print twice but who cares
	if(current - 1 != previous):
		print(current - 1)
	if(current + 1 != next):
		print(current + 1)
