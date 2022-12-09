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
			#for i in range(5):
			#	for j in range(5):
			#		if head_pos == (j,i):
			#			print('H', end='')
			#		elif tail_pos == (j, i):
			#			print('T', end='')
			#		else:
			#			print('.', end='')
			#	print()
			visited.add(tail_pos)
			#print(head_pos, tail_pos)
	print(len(visited))

def print_rope(head, tails):
	size = 30
	msize = -20
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
	size = 300
	msize = -50
	for i in range(msize, size):
		for j in range(msize, size):
			if (i, j) in visited:
				print('#', end='')
			else:
				print('.', end='')
		print()
	print()


def part2():
	head = (0,0)
	tails = [(0,0) for x in range(9)]
	visited = set()
	for direction, amount in movements:
		amount = int(amount)
		for i in range(amount):
			shadow_head = head
			shadow_tails = tails.copy()
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
			for kid, knot in enumerate(tails):
				if kid == 0: # first tail
					dist = dist_to(knot, head)
					if dist > 1.5:
						tails[0] = shadow_head
				#elif kid == 8: # first knot, regular tail
				#	pass
					#dist_forward = dist_to(knot, tails[kid-1])
					#if dist_forward > 1.5:
					#	tails[kid] = shadow_tails[kid-1]
				else: # 1-8, aka all other knots
					dist_forward = dist_to(knot, tails[kid-1]) # distance to previous knot, eg from 2 to 1
					prev_diag = dist_to(tails[kid-1], shadow_tails[kid-1]) > 1
					#print(f'[HEAD: {head}] doing {knot}({kid+1}): dist: {dist_forward} ({tails[kid-1]} {prev_diag}: {dist_to(tails[kid-1], shadow_tails[kid-1])}) ', end='')
					#print('tails:', tails)
					#print('shadows:', shadow_tails)
					if dist_forward > 1.5:
						if prev_diag:
							if dist_forward > 2:
								new_delta = sub_tuples(tails[kid-1], shadow_tails[kid-1])
							else:
								new_delta = tuple([i-1 if i >1 else i for i in sub_tuples(tails[kid-1], knot)])
							#print(tails[kid-1], shadow_tails[kid-1], new_delta)
							new_pos = add_tuples(knot, new_delta) 
							# if we try to move, we have to be close == 1 dist to our knot before
							# because, on diagonal turns, we have to straighten out
							#delta_between = (0,0)
							#if dist_to(new_pos, tails[kid-1]) > 1:
								#delta_between = sub_tuples(tails[kid-1], new_pos)
							#	new_pos = sub_tuples(shadow_tails[kid-1], knot)
							#new_pos = add_tuples(new_delta, delta_between)
							#print(new_pos)
							# different row and column
							x1,y1 = knot
							x2,y2 = tails[kid-1]
							if x1 != x2 and y1 != y2:
								#print('aaa')
								tails[kid] = shadow_tails[kid-1]
							#else:
							tails[kid] = new_pos#add_tuples(knot, new_delta)
						else:
							tails[kid] = shadow_tails[kid-1]
							#if not (shadow_tails[kid-1] == tails[kid-1]):
					#print(f'is now: {tails[kid]}')
					

			visited.add(tails[8])
			#print(tails)
		#print_rope(head, tails)
	print_final(head, tails, visited)
	print(len(visited))
# 2310 too low
# 2365 too low
# 2366 too low
# 2369 maybe
part2()

#def part2_new()
#	pass


#part2_new()