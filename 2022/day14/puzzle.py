rocks = [l.rstrip() for l in open("input").readlines()]

MAXX = 0
MINX = 1000
MAXY = 0
MINY = 1000

my_map = [['.' for _ in range(300)] for _ in range(1200)]

# set this to 0 for part 1
# or a reasonable number (like 300) for part 2
XSHIFT = 0#300 # part2

sand_start = (500+XSHIFT, 0)

def path_to_touple(path):
	return tuple([int(x) for x in path.split(',')])

def set_map_boundaries(p1, p2):
	global MAXX, MINX, MAXY, MINY
	MAXX = max(p1[0], p2[0], MAXX)
	MINX = min(p1[0], p2[0], MINX)

	MAXY = max(p1[1], p2[1], MAXY)
	MINY = min(p1[1], p2[1], MINY)

for rock_path in rocks:
	paths = rock_path.split(' -> ')

	current_path = path_to_touple(paths[0])

	for i in range(1, len(paths)):
		next_path = path_to_touple(paths[i])
		set_map_boundaries(current_path, next_path)		

		if next_path[0] == current_path[0]: # the x are the same, move along y
			y1 = min(next_path[1], current_path[1])
			y2 = max(next_path[1], current_path[1])
			for y in range(y1, y2+1):
				my_map[current_path[0]+XSHIFT][y] = '#'
		else:
			x1 = min(next_path[0], current_path[0]) + XSHIFT
			x2 = max(next_path[0], current_path[0]) + XSHIFT
			for x in range(x1, x2+1):
				my_map[x][current_path[1]] = '#'

		current_path = next_path


MAXX = max(1200, MAXX)
MINY = min(0, MINY)

# part 2
if XSHIFT > 0:
	for i in range(0, 1200):
		my_map[i][MAXY + 2] = '#'
	MAXY += 2
# part 2 end

can_any_sand_move = True
sand_grains_moved = 0
my_map[500+XSHIFT][0] = '+'

def print_map():
	for i in range(MINX,MAXX):
		for j in range(MINY,MAXY+1):
			print(my_map[i][j], end='')
		print()

#for i in range(25): # this will move X amount of sand grains
while can_any_sand_move:
	movements = [(0, 1), (-1, 1), (1, 1)] # empirically tested :D
	sandx, sandy = sand_start
	can_move = True

	while can_move: # while current grain can move
		has_moved = False
		for move in movements: # go through each movement and see if we can move with it
			new_sandx = sandx + move[0]
			new_sandy = sandy + move[1]

			#print(f'For {i} checking out {new_sandx}-{new_sandy}')
			if my_map[new_sandx][new_sandy] == '.': # if the next tile is air
				sandx = new_sandx
				sandy = new_sandy
				has_moved = True
				#print(f'Moved {i} to {sandx}-{sandy}')
				break # inner loop, dont go through movements anymore
		if sandy+1 > MAXY:
			can_any_sand_move = False
			break
		if not has_moved:
			my_map[sandx][sandy] = 'o'
			sand_grains_moved += 1
			#print_map()
			if (sandx, sandy) == sand_start:
				can_any_sand_move = False
			break

#print(MINX, MAXX, MINY, MAXY)
print_map()

print(sand_grains_moved)