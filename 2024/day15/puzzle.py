lines = [line.rstrip('\n') for line in open("input").readlines()]

grid = []
grid2 = []
movements = []

delta = ((1,0), (0,1), (-1, 0), (0, -1))
directions = ['>', 'v', '<', '^']

# process everything
process_movements = False
for line in lines:
	if not line:
		process_movements = True
		continue
		
	if process_movements:
		movements += line
	else:
		grid.append([x for x in line])
		
# find our guy
current_position = (-1, -1)
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == '@':
			current_position = (x, y)

def print_grid(a_grid):
	for y in range(len(a_grid)):
		for x in range(len(a_grid[0])):
			print(a_grid[y][x], end='')
		print()

# process gird 2
current_pos2 = (-1, -1)
for y in range(len(grid)):
	row = []
	for x in range(len(grid[0])):
		tile = grid[y][x]
		if tile == '#':
			row += ['#', '#']
		elif tile == 'O':
			row += ['[', ']']
		elif tile == '.':
			row += ['.', '.']
		elif tile == '@':
			current_pos2 = (x*2, len(grid2))
			row += ['@', '.']
	grid2.append(row)

def try_move(cx, cy, dx, dy):
	nx, ny = cx+dx, cy+dy
	next_tile = grid[ny][nx]
	
	if next_tile == '#':
		return False
	if next_tile == 'O':
		# maybe we can push some boxes?
		if try_move(nx, ny, dx, dy):
			# swap them
			grid[cy][cx], grid[ny][nx] = grid[ny][nx], grid[cy][cx]
			return True
	if next_tile == '.':
		# safe to move, swap
		grid[cy][cx], grid[ny][nx] = grid[ny][nx], grid[cy][cx]
		return True
	
for mov in movements:
	i =	directions.index(mov)
	dx, dy = delta[i]
	cx, cy = current_position
#	print(f'Moving in direction: {mov}')
	if try_move(cx, cy, dx, dy):
		current_position = (cx+dx, cy+dy)
#	print_grid()
	
def get_coordinates():
	GPS_total = 0
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == 'O':
				GPS_total += y * 100 + x
	return GPS_total

# part 1
print(get_coordinates())

def try_move2(move_array, dx, dy, direction):

	# when moving left/right we only have 1 position to move along
	if direction in ['>', '<']:
		cx, cy = move_array.pop()
		nx, ny = cx+dx, cy+dy
		next_tile = grid2[ny][nx]

		if next_tile == '#':
			return False

		if next_tile in ['[', ']']:
			if try_move2([(nx, ny)], dx, dy, direction):
				# swap them
				grid2[cy][cx], grid2[ny][nx] = grid2[ny][nx], grid2[cy][cx]
				return True		

		if next_tile == '.':
			# safe to move, swap
			grid2[cy][cx], grid2[ny][nx] = grid2[ny][nx], grid2[cy][cx]
			return True

	else:
		for cx, cy in move_array:
			nx, ny = cx+dx, cy+dy
			next_tile = grid2[ny][nx]
			
			if next_tile == '#':
				return False

		next_dots = 0
		next_level = set()
		for cx, cy in move_array:
			nx, ny = cx+dx, cy+dy
			next_tile = grid2[ny][nx]
			
			if next_tile in ['[', ']']:			
					# we're going up or down
					box_delta = 1 if next_tile == '[' else -1
					
					next_level.add((nx, ny))
					next_level.add((nx+box_delta, ny))
			
			if next_tile == '.':
				next_dots += 1

		if next_dots == len(move_array) or \
				try_move2(next_level, dx, dy, direction):
			# all tiles in the next line are empty or
			# we can move all the next line of boxes
			for cx, cy in move_array:
				nx, ny = cx+dx, cy+dy
				grid2[cy][cx], grid2[ny][nx] = grid2[ny][nx], grid2[cy][cx]
			return True

		if try_move2(next_level, dx, dy, direction):
			for cx, cy in next_level:
				nx, ny = cx+dx, cy+dy
				grid2[cy][cx], grid2[ny][nx] = grid2[ny][nx], grid2[cy][cx]
			return True
			
# code for part 2
#print_grid(grid2)
for mov in movements:
	i = directions.index(mov)
	dx, dy = delta[i]
	cx, cy = current_pos2
#	print(f'Moving in direction: {mov}')
	if try_move2(set([(cx, cy)]), dx, dy, mov):
		current_pos2 = (cx+dx, cy+dy)
#	print_grid(grid2)

def get_coordinates2():
	GPS_total = 0
	for y in range(len(grid2)):
		for x in range(len(grid2[0])):
			if grid2[y][x] == '[':
				GPS_total += y * 100 + x
	return GPS_total
	
# 1528018 too high
# 1524252 too high
print(get_coordinates2())
