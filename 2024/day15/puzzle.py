lines = [line.rstrip('\n') for line in open("input").readlines()]

grid = []
grid_part2 = []
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

def try_move(cx, cy, dx, dy):
	nx, ny = cx+dx, cy+dy
	next_tile = grid[ny][nx]
#	print(f'Checking out next tile: {next_tile}')
	
	if next_tile == '#':
		return False
	if next_tile == 'O':
#		print(f'Pushing boxes! at: {next_tile}')
		# maybe we can push some boxes?
		if try_move(nx, ny, dx, dy):
			# swap them
			grid[cy][cx], grid[ny][nx] = grid[ny][nx], grid[cy][cx]
			return True
	if next_tile == '.':
		# safe to move, swap
		grid[cy][cx], grid[ny][nx] = grid[ny][nx], grid[cy][cx]
		return True

def print_grid():
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			print(grid[y][x], end='')
		print()
		
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
	
print(get_coordinates())
