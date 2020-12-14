with open('input', 'r') as f:
	lines = [i.strip() for i in f.readlines()]	

def apply_mask(mask, num):
	bitnum = '{:036b}'.format(num)
	newnum = []
	for i, bit in enumerate(mask):
		if bit == 'X':
			newnum.append(bitnum[i])
		if bit == '1':
			newnum.append('1')
		if bit == '0':
			newnum.append('0')	
	newnum = ''.join(newnum)
#	print(bitnum, mask, newnum)
	return int(newnum, 2)

def partone():
	mem = {}
	mask = ''
	
	for line in lines:
		if('mask' in line):
			_, mask = line.split(' = ')
		else:
			loc, num = line.split(' = ')
			loc = loc[4:-1]
			mem[loc] = apply_mask(mask, int(num))
			
	total_mem = 0
	for n in mem:
		total_mem += mem[n]
	
	print(f'Part 1 solution: {total_mem}')
	
def fix_floaters(lst):
	allcombs = []
	lst = list(set(lst))
	morex = False
	for numstr in lst:
		for i, char in enumerate(numstr):
			if char == 'X':
							
				num0 = list(numstr)
				num0[i] = '0'
				num0 = ''.join(num0)
				
				num1 = list(numstr)
				num1[i] = '1'
				num1 = ''.join(num1)
						
				allcombs += [num0, num1]
				morex = True
	
	if morex:
		return fix_floaters(list(set(allcombs)))
	else:
		return lst
		#return list(set(lst))

def apply_mask2(mask, num):
	bitnum = '{:036b}'.format(num)
	newnum = []
	for i, bit in enumerate(mask):
		if bit == 'X':
			newnum.append('X')
		if bit == '1':
			newnum.append('1')
		if bit == '0':
			newnum.append(bitnum[i])	

	newnum = ''.join(newnum)
	goodfloaters = fix_floaters([newnum])
#	[print(i, int(i, 2)) for i in goodfloaters] # testing
	return [int(i, 2) for i in goodfloaters]
		
def parttwo():
	mem = {}
	mask = ''
	
	for line in lines:
		if('mask' in line):
			_, mask = line.split(' = ')
		else:
			loc, num = line.split(' = ')
			loc = loc[4:-1]
			memaddr = apply_mask2(mask, int(loc))
			
			for m in memaddr:
				mem[m] = int(num)

	total_mem = 0
	for n in mem:
		total_mem += mem[n]
	print(f'Part 2 solution: {total_mem}')

#partone()
parttwo() #it takes a while, just be patient =) nothing like a exponential time algorithm!
