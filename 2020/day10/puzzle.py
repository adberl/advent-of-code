with open('input', 'r') as f:
	jolts = [int(i.strip()) for i in f.readlines()]
jolts += [0, max(jolts) + 3]	

def partone():
	jolts.sort()
	ones = 0
	threes = 0
	for current in range(len(jolts)-1):
		if(jolts[current+1] - jolts[current] == 1):
			ones += 1
		elif(jolts[current+1] - jolts[current] == 3):
			threes +=1
	print('Part 1 solution:', ones, '*', threes, '=', ones * threes)
	
def parttwo():
	jolts.sort()
	cjolts = {}
	for i in range(len(jolts)-1):
		cjolts[jolts[i]] = 0
	cjolts[jolts[-1]] = 1
	for i in range(len(jolts)-2, -1, -1): # start at -2 because we dont care about 22
		for child in get_children(i):
			cjolts[jolts[i]] += cjolts[child]

	print(f'Part 2 solution: {cjolts[0]}')
		
def get_children(i):
	viable_children = []
	for j in range(i+1, len(jolts)):
		if(jolts[j] - jolts[i] <= 3):
			viable_children.append(jolts[j])
	return viable_children

partone()
parttwo()
