from copy import deepcopy

og_lab = [[x for x in line.rstrip('\n')] for line in open("input").readlines()]

max_y = len(og_lab)
max_x = len(og_lab[0])

def is_valid(num, max_num):
	return 0 <= num < max_num

movx = [1, 0, -1, 0]
movy = [0, 1, 0, -1]
direction = ['>', 'v', '<', '^']

def get_dir_coords(x, y, some_dir):
	dir_id = direction.index(some_dir)
	dx = movx[dir_id]
	dy = movy[dir_id]

	next_x = x + dx
	next_y = y + dy
	return next_x, next_y

def guard_escaped(lastx, lasty, escape_dir):
#	print(f'Guard has escaped! last seen at: ({lastx}, {lasty}), with direction {escape_dir}')
	#og_lab[lasty][lastx] = 'X'	
	visited.add((lastx, lasty, escape_dir))
	p1_visited.add((lastx, lasty))

def print_grid(lab):
	for y in range(max_y):
		for x in range(max_x):
			print(lab[y][x], end='')
		print()
	print()

p1_visited = set()
visited = set()
def find_guard(lab):
	local_visited = set()
	steps_taken = 0
	for y in range(max_y):
		for x in range(max_x):
			guard_dir = lab[y][x]	 
			if guard_dir in direction:
#				print(f'Found the guard at: ({x}, {y})')
				escaped = False
					
				while not escaped:
#					print(f'Guard is at: ({x}, {y})')
					next_x, next_y = get_dir_coords(x, y, guard_dir)
					if is_valid(next_x, max_x) and is_valid(next_y, max_y):
						steps_taken += 1
						if steps_taken >= 100000:
							print(f'We walked too much ({steps_taken}), time to take a rest')
							return True
						if (next_x, next_y, guard_dir) in local_visited:
#							print(f'Already been here, must be a loop! ({x}, {y})')
							#loops += 1
							return True
					
						#print(f'Moving to: ({next_x}, {next_y})')
						if lab[next_y][next_x] == '#': # ups we hit a chemical spill
							dir_id = direction.index(guard_dir)
							#print(direction, dir_id, guard_dir)
							new_id = (dir_id + 1) % len(direction)
							guard_dir = direction[new_id]
							# rotate				
							next_x, next_y = get_dir_coords(x, y, guard_dir)
							while is_valid(next_x, max_x) and is_valid(next_y, max_y) \
								and lab[next_y][next_x] == '#':
								
								dir_id = direction.index(guard_dir)
								#print(direction, dir_id, guard_dir)
								new_id = (dir_id + 1) % len(direction)
								guard_dir = direction[new_id]
								# rotate				
								next_x, next_y = get_dir_coords(x, y, guard_dir)
								
							
							#if is_valid(next_x, max_x) and is_valid(next_y, max_y):
							visited.add((x, y, guard_dir))	
							p1_visited.add((x, y))	
							local_visited.add((x, y, guard_dir))					
							#lab[y][x] = 'X'
							lab[next_y][next_x] = guard_dir
							x, y = next_x, next_y
							
						else: # we can move normally
							#lab[y][x] = 'X'
							visited.add((x, y, guard_dir))
							p1_visited.add((x, y))
							local_visited.add((x, y, guard_dir))
							lab[next_y][next_x] = guard_dir
							x, y = next_x, next_y
					else:
						escaped = True
						guard_escaped(x, y, guard_dir)
						local_visited.add((x, y, guard_dir))
						return False
	print('ups we replaced the starting position')
	return False
								
find_guard(deepcopy(og_lab))
#print_grid(og_lab)		
print(len(p1_visited))

# part 2
def hash_in_row(y):
	for x in range(max_x):
		if og_lab[y][x] == '#':
			return True
	return False

def hash_in_col(x):
	for y in range(max_y):
		if og_lab[y][x] == '#':
			return True
	return False	


found = set()
tested = set()
for y in range(max_y):
	for x in range(max_x):
		if (x, y) in p1_visited: # we've been here
			if hash_in_row(y) or hash_in_col(x):
				for adir in direction:
					if (x, y, adir) in visited: # we now also have the direction
						next_x, next_y = get_dir_coords(x, y, adir)
						if is_valid(next_x, max_x) and is_valid(next_y, max_y):
							if og_lab[next_y][next_x] == '#' or (next_x, next_y) in found:
								continue
								
							if (next_x, next_y) in tested:
								continue
								
							#print(f'Potential placement at: {next_x}, {next_y}')
							tested.add((next_x, next_y))
							new_lab = deepcopy(og_lab)
							#new_lab[next_y][next_x] = 'O'
							#print_grid(new_lab)
							new_lab[next_y][next_x] = '#'
							if find_guard(new_lab):
								found.add((next_x, next_y))

def manual_debug():
	new_lab = deepcopy(og_lab)
	next_x, next_y = 5, 1
	new_lab[next_y][next_x] = 'O'
	print_grid(new_lab)
	new_lab[next_y][next_x] = '#'
	print_grid(new_lab)
	find_guard(new_lab)
	print_grid(new_lab)
	
#manual_debug()					
print(len(found))
