import heapq as hq

heightmap = [l.rstrip() for l in open("input").readlines()]

maxx = len(heightmap)
maxy = len(heightmap[0])

def get_connections(node, visited):
	moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
	ret = []

	x1, y1 = node
	prevheight = heightmap[x1][y1]
	for m in moves:
		x2, y2 = m
		newx, newy = x1 + x2, y1 + y2
		if newx >= 0 and newx < maxx and\
			newy >= 0 and newy < maxy: # good output
				if (newx, newy) in visited:
					continue
				newheight = heightmap[newx][newy]

				if newheight == 'S':
					newheight = 'a'
				elif newheight == 'E':
					newheight = 'z'

				if prevheight == 'S':
					prevheight = chr(ord('a')-1)
				
				dif = ord(newheight) - ord(prevheight)
				if dif == 1 or dif <= 0:
					ret.append((newx, newy))
	return ret

def get_distances():
	distances = {}
	end_node = (0,0)
	for i in range(maxx):
		for j in range(maxy):
			#if heightmap[i][j] == 'S':
			#	start_node = (i, j)
			if heightmap[i][j] == 'E':
				end_node = (i, j)
			distances[(i, j)] = 10000000000000
	return distances, end_node

def dijkstra(start_node):
	distances, end_node = get_distances()
	distances[start_node] = 0
	visited_nodes = []
	queue = [(0, start_node)]

	while queue: # while there is a node we haven't visited
		dist, current_node = hq.heappop(queue)
		neighbours = get_connections(current_node, visited_nodes)
		#print(f'doing node: {current_node}({heightmap[current_node[0]][current_node[1]]}) with neighbours: {neighbours}')
		for n in neighbours:
			if n in visited_nodes:
				continue
			new_dist = dist + 1
			if new_dist < distances[n]:
				distances[n] = new_dist
				hq.heappush(queue, (new_dist, n))

			visited_nodes.append(n)
	
	return distances[end_node]

all_distances = []
for i in range(maxx):
	print(f'node: {i+1}/{maxx}')
	all_distances.append(dijkstra((i, 0)))

print(all_distances, min(all_distances))

# part 2 took 1m13.360s to complete
# anxious of what this means for future days :D