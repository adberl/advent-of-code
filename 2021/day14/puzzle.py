lines = [i.rstrip() for i in open('input', 'r').readlines()]

polymer = ''
all_pairs = {}
MAX_STEPS = 40
polymer_pairs = {}
el_count = {}
for i in range(len(lines)):
	if polymer == '' and lines[i+1] == '':
		polymer = lines[i]
	elif lines[i] == '':
		continue
	else:
		pair, insert = lines[i].split(' -> ')
		all_pairs[pair] = insert

def p1(): # gets too big :(
	for step in range(10):
		new_polymer = polymer
		for i in range(len(polymer), 1, -1):
			key = polymer[i-2:i]
			new_polymer = new_polymer[:i-1] + all_pairs[key] + new_polymer[i-1:]		
		polymer = new_polymer
	#	print(f'Polymer after step {step}: {polymer}')	

	#count all elements
	element_count = {}
	for el in polymer:
		if not el in element_count:
			element_count[el] = 1
		else:
			element_count[el] += 1

	min_el = 1000000000
	max_el = -1
			
	for el in element_count:
		ct = element_count[el]
		if ct > max_el:
			max_el = ct
		if ct < min_el:
			min_el = ct
				
	print(max_el - min_el)

def add_el(el, amount):
		if not el in el_count:
			el_count[el] = amount
		else:
			el_count[el] += amount

def add_new_pair(key, new_dict, amount):
	if not key in new_dict:
		new_dict[key] = amount
	else:
		new_dict[key] += amount

def p2(polymer_pairs):
	for i in range(len(polymer)): # count the initial elements
		el = polymer[i]
		add_el(el, 1)

	for i in range(len(polymer), 1, -1): # init the polymer pairs
		key = polymer[i-2:i]
		add_new_pair(key, polymer_pairs, 1)

	for step in range(MAX_STEPS):
		new_dict = polymer_pairs.copy()
		for pair in polymer_pairs:
			new_el = all_pairs[pair]
			add_el(new_el, polymer_pairs[pair])
			newpair1 = pair[0] + new_el
			newpair2 = new_el + pair[1]
			add_new_pair(newpair1, new_dict, polymer_pairs[pair])
			add_new_pair(newpair2, new_dict, polymer_pairs[pair])
			new_dict[pair] -= polymer_pairs[pair]
			if new_dict[pair] == 0:
				new_dict.pop(pair)
		polymer_pairs = new_dict
		print(f'Step {step}: {polymer_pairs}, ELEMENTS: {el_count}')

def det_max_el():
	min_el = 1000000000000
	max_el = -1
	for el in el_count:
		ct = el_count[el]
		if ct > max_el:
			max_el = ct
		if ct < min_el:
			min_el = ct
				
	print(max_el - min_el)

p2(polymer_pairs)
det_max_el()
