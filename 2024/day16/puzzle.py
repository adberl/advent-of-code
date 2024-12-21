import heapq as hq

maze = [[x for x in line.rstrip('\n')] for line in open("input").readlines()]

maxx = len(maze[0])
maxy = len(maze)

#for y in range(maxy):
#	for x in range(maxx):
#		print(maze[y][x], end = '')
#	print()

delta = ((0, -1),  (1,0), (0,1), (-1, 0))
rotation = ['^', '>', 'v', '<']
rotation = [0, 1, 2, 3]
start = (1, maxy-2)
end = (maxx-2, 1)



queue = [(0, start, 1)]
distances = [[10000000 for _ in range(maxx)] for _ in range(maxy)]
distances[start[1]][start[0]] = 0
visited = []

def get_rotation_distance(old_rot, new_rot):
	naive_dist = abs(old_rot - new_rot)
	if naive_dist > 2:
		# 3 -> 1 or 1 -> 3 whever we can loop around
		return 1
	else:
		return naive_dist

def get_neighbours(node, visited, is_part_two=False):
	neighbours = []

	for i, (dx, dy) in enumerate(delta):
		x, y = node
		newx = x + dx
		newy = y + dy
		
		if 0 <= newx < maxx and 0 <= newy < maxy:
			new_node = (newx, newy)
			if maze[newy][newx] == '#':
				# we hit a wall
				continue

			if is_part_two:
				if new_node in visited:
					continue
			else:
				if (new_node, i) in visited:
					continue
			
			neighbours.append((new_node, i))
			
	return neighbours
				
def dijkstra():
		while queue:
#			print(queue)
			dist, node, r = hq.heappop(queue)
			
			for neighbour, nr in get_neighbours(node, visited):
				new_dist = 1 + dist + 1000 * get_rotation_distance(r, nr)
				nx, ny = neighbour
				if new_dist < distances[ny][nx]:
					distances[ny][nx] = new_dist
					hq.heappush(queue, (new_dist, neighbour, nr))
				visited.append((neighbour, nr))
		
dijkstra()

# part 1:
end_dist = distances[end[1]][end[0]]
print(end_dist)

def print_distances():
	for y in range(maxy):
		for x in range(maxx):
			if distances[y][x] == 10000000:
				print('#####', end = '\t\t')
			else:
				print(distances[y][x], end = '\t\t')
		print()

#print_distances()

# part 2:
steps = end_dist % 1000
rotations = end_dist // 1000

good_nodes = set()
optimal_path = []

def find_optimal_path():
	cx, cy = end
	while distances[cy][cx] != 0:
		optimal_path.append((cx,cy))
		
		smallest_distance = 10000000
		npos = (0, 0)
		for pos, rot in get_neighbours((cx, cy), []):
			nx, ny = pos
			if smallest_distance > distances[ny][nx]:
				npos = pos
				smallest_distance = distances[ny][nx]
				
		cx, cy = npos
	optimal_path.append(start)	

def step(node, path):

	#steps = end_dist % 1000
	#rotations = end_dist // 1000
	cx, cy = node
	neighbours = get_neighbours(node, path, True)
	if len(path) == steps-1:
		yellow_node = any([True if x == end else False for x, y in neighbours])
		if yellow_node:
			
			ex, ey = end
			
			current_dist = distances[cy][cx]
			end_dist = distances[ey][ex]
			
			if current_dist <= end_dist-1:
				good_nodes.update(path)
				return
		
		return
	
	for neighbour, i in neighbours:
		nx, ny = neighbour
	
		if not node in optimal_path and neighbour in optimal_path:
			# we're rejoining the optimal path, let's make sure we
			# didn't do any extra turns
			current_steps = len(path)
			current_rotations = distances[cy][cx] // 1000
			npox, npoy = optimal_path[current_steps+2]
			n_plus_one_rotations = distances[npoy][npox] // 1000
			if not ((current_rotations == n_plus_one_rotations) or (current_rotations + 1 <= n_plus_one_rotations)):

				return

		if distances[ny][nx]%1000 == (distances[cy][cx]%1000+1):
			# current node rotation count should be the same as optimal path + 1 node
			step(neighbour, path+[neighbour])
	
# part 2 actual solution	
find_optimal_path()
optimal_path = list(reversed(optimal_path))
#print(optimal_path)

step(start, [])

def print_maze():
	for y in range(maxy):
		for x in range(maxx):
			if((x, y) in good_nodes):
				print('O', end='')
			else:
				print(maze[y][x], end = '')
		print()

print_maze()	
	
	
# 519 too high
# 517 too high
# 477 too low
print(len(good_nodes)+2)
