my_input = [line.rstrip() for line in open("input").readlines()]

# empirically verified :)
start_pipe = 'F'
start_dir = set(['L','D'])
current_direction = 'R'

# find start position
def find_start_position():
	for v, line in enumerate(my_input):
		for h, char in enumerate(line):
			if char == 'S':
				start = (h,v)
				my_input[v] = my_input[v].replace('S', start_pipe)
				return start

# find start pipe
# TO BE ADDED

start = find_start_position()

dir_move = {
	'L': (lambda x,y: ((x-1, y), 'L')),
	'U': (lambda x,y: ((x, y-1), 'U')),
	'R': (lambda x,y: ((x+1, y), 'R')),
	'D': (lambda x,y: ((x, y+1), 'D'))
}

move = {
	'-': (lambda x,y,d: dir_move['L'](x,y) if d == 'L' else dir_move['R'](x,y)),
	'|': (lambda x,y,d: dir_move['U'](x,y) if d == 'U' else dir_move['D'](x,y)),
	'L': (lambda x,y,d: dir_move['R'](x,y) if d == 'D' else dir_move['U'](x,y)),
	'J': (lambda x,y,d: dir_move['L'](x,y) if d == 'D' else dir_move['U'](x,y)),
	'7': (lambda x,y,d: dir_move['D'](x,y) if d == 'R' else dir_move['L'](x,y)),
	'F': (lambda x,y,d: dir_move['D'](x,y) if d == 'L' else dir_move['R'](x,y))
}

path = []
current_position = start
pipemap = [[set() for _ in my_input[0]] for _ in my_input]

while not current_position in path:
	path.append(current_position)
	x,y = current_position
	pipe = my_input[y][x]
	old_direction = current_direction
	current_position, current_direction = move[pipe](x,y,current_direction)
	pipemap[y][x] = set([current_direction, old_direction])
pipemap[start[1]][start[0]] = start_dir


print(len(path)//2) # part 1


# part 2
insides = 0
debug = False
for v, line in enumerate(my_input):
	for h, char in enumerate(line):
		vis = [[g for g in y] for y in my_input]
		pos = (h, v)
		if pos in path:
			continue

		riding_pipes = False
		hits = 0
		direction = set()
		vis[v][h] = 'X'
		riding_direction = set()
		for i in range(h+1, len(line)): # raycast to the right
			if (i, v) in path: # we hit a pipe
				vis[v][i] = hits+ (1 if not riding_pipes else 2)
				direction = pipemap[v][i]

				if len(direction) == 2: # we hit a corner
					if riding_pipes:
						riding_pipes = False
						same_new_dir = direction - riding_direction
						hits += 2 if 'U' in same_new_dir or 'D' in same_new_dir else 1
					else:
						riding_direction = direction					
						riding_pipes = True 
				else: # not a corner, maybe vertical pipe?
					if not 'L' in direction and not 'R' in direction:
						hits += 1


		if hits > 0 and hits % 2:
			insides += 1
			print(f"{pos} is inside! {hits}")

		if debug:
			for line in vis:
				for a in line:
					print(a, end=' ')
				print()
			print()

print(insides)
