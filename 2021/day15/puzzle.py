import heapq as hq

lines = [i.rstrip() for i in open('input', 'r').readlines()]

maxx = len(lines[0])
maxy = len(lines)


visited = []
queue = [(0, (0, 0))]

def fill_distances(maxonx, maxony):
	distances = {}
	for i in range(maxonx):
		for j in range(maxony):
			distances[(i, j)] = 10000000000000
	distances[(0,0)] = 0
	return distances

def make_bigger():
	risks = [[0 for i in range(maxx*5)] for j in range(maxy*5)]

	for i in range(maxx):
		for j in range(maxy):
			for biggerx in range(5):
				new_risk = (int(lines[j][i]) + biggerx)
				risks[j][i+maxx*biggerx] = new_risk
	for i in range(len(risks[0])):
		for j in range(maxy):
			for biggery in range(5):
				new_risk = (int(risks[j][i]) + biggery) 
				risks[j+maxy*biggery][i] = new_risk

	for i in range(len(risks[0])):
		for j in range(len(risks)): # cba to fix :(
			if risks[j][i] > 9: 
				risks[j][i] -= 9	

	return risks
		
def add_neighbours(whose, where, amaxx, amaxy):
	movement = [(-1, 0), (0, -1), (1, 0), (0, 1)]
	for movex, movey in movement:
		newx = whose[0] + movex
		newy = whose[1] + movey
		
		if newx < 0 or newx >= amaxx or newy < 0 or newy >= amaxy:
			continue
		new_node = (newx, newy) 
		if not new_node in visited:
			where.append(new_node)

def dijkstra():
	lines = make_bigger()
	newmax = len(lines)
	distances = fill_distances(newmax, newmax)
	end_node = (newmax-1, newmax-1)

	while queue:
		dist, current_node = hq.heappop(queue)
		neighbours = []
		add_neighbours(current_node, neighbours, newmax, newmax)
		for n in neighbours:
			new_dist = dist + int(lines[n[1]][n[0]])
			if new_dist < distances[n]:
				distances[n] = new_dist
				hq.heappush(queue, (new_dist, n))
		visited.append(current_node)

#		if current_node == None or current_node == end_node:
#			return distances[end_node]
	print(f'Distance from topleft to bottomright is {distances[end_node]}')

dijkstra()

"""
time python3 puzzle.py
Distance from topleft to bottomright is 2831 

real	204m14.091s
user	202m30.792s
sys	0m1.779s

it might take a while but it works :)
"""
