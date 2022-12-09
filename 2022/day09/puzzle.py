movements = [l.rstrip().split(' ') for l in open("input").readlines()]

def add_tuples(a, b):
	return tuple(map(lambda x, y: x + y, a, b))

def sub_tuples(a, b):
	return tuple(map(lambda x, y: x - y, a, b))

def dist_to(head, tail):
	x1, y1 = head
	x2, y2 = tail

	return ((y2-y1)**2 + (x2-x1)**2)**0.5
#starting_pos = (0,0)
def part1():
	head_pos = (0,0)
	tail_pos = (0,0)
	shadow_head_pos = (0, 0)
	visited = set()
	for direction, amount in movements:
		amount = int(amount)
		for i in range(amount):
			shadow_head_pos = head_pos
			match direction:
				case 'R':
					head_pos = add_tuples(head_pos, (0, +1))
				case 'L':
					head_pos = add_tuples(head_pos, (0, -1))
				case 'U':
					head_pos = add_tuples(head_pos, (1, 0))
				case 'D':
					head_pos = add_tuples(head_pos, (-1, 0))
			
			dist = dist_to(tail_pos, head_pos)
			if dist > 1.5:
				tail_pos = shadow_head_pos

			visited.add(tail_pos)

	print(len(visited))

def print_rope(head, tails):
	size = 6
	msize = 0
	for i in range(msize, size):
		for j in range(msize, size):
			if head == (i,j):
				print('H', end='')
			else:
				printed = False
				for kid, knot in enumerate(tails):
					if knot == (i, j) and not printed:
						print(kid+1, end='')
						printed = True
				if not printed:
					print('.', end='')
		print()
	print()

def print_final(head, tails, visited):
	size = 6
	msize = 0
	for i in range(msize, size):
		for j in range(msize, size):
			if (i, j) in visited:
				print('#', end='')
			else:
				print('.', end='')
		print()
	print()

def normalize_tuple(t):
	return tuple([i/abs(i) if i != 0 else 0 for i in t])

def part2():
	head = (0,0)
	tails = [(0,0) for x in range(9)]
	visited = set()
	for direction, amount in movements:
		amount = int(amount)
		for i in range(amount):
			delta = (0,0)
			match direction:
				case 'R':
					delta = (0, +1)
				case 'L':
					delta = (0, -1)
				case 'U':
					delta = (1, 0)
				case 'D':
					delta = (-1, 0)
			head = add_tuples(head, delta)
		
			for knot_id, knot in enumerate(tails):
				_head = head
				if knot_id > 0:
					_head = tails[knot_id-1] # we move according to the one ahead
				dist = dist_to(knot, _head)
				if dist >= 2:
					# its not in same column or row, warp behind it
					# by moving diagonally
					new_delta = sub_tuples(_head, knot)
					new_delta = normalize_tuple(new_delta)
					new_pos = add_tuples(knot, new_delta)
					tails[knot_id] = new_pos
			visited.add(tails[8])

		#print_rope(head, tails)
	print(len(visited))

part2()
