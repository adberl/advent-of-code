from functools import cmp_to_key

packets = [l.rstrip() for l in open("input").readlines()]

pairs = []
p1 = p2 = None

current_pkt = 0
for packet in packets:
	if packet == '':
		pairs.append((p1, p2))
		current_pkt = 0
	elif current_pkt == 0:
		p1 = eval(packet)
		current_pkt += 1
	else:
		p2 = eval(packet)
		current_pkt += 1

def compare(left, right):
	#print(f'Comparing: {left}, {right}')
	if type(left) == int and type(right) == int:
		if left > right:
			return -1
		if right > left:
			return 1
		return 0
	
	if not isinstance(left, list):
		left = [left]

	if not isinstance(right, list):
		right = [right]

	for i in range(min(len(left), len(right))):
		ret = compare(left[i], right[i])

		if ret == 0:
			continue
		else:
			return ret

	if len(left) > len(right):
		return -1
	elif len(right) > len(left):
		return 1		

	return 0

results = []
sort_pairs_here = []
for lpair, rpair in pairs:
	results.append(compare(lpair, rpair))
	sort_pairs_here.append(lpair)
	sort_pairs_here.append(rpair)

fin = 0
for i, res in enumerate(results):
	if res > 0:
		fin += i+1

#print(results, fin) # part 1 => fin
key1 = [[2]]
key2 = [[6]]

sort_pairs_here.append(key1)
sort_pairs_here.append(key2)
sort_pairs_here.sort(key=cmp_to_key(compare), reverse=True)

key1_loc = sort_pairs_here.index(key1) + 1
key2_loc = sort_pairs_here.index(key2) + 1

print(key1_loc*key2_loc)