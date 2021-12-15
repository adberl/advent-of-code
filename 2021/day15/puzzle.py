lines = [i.rstrip() for i in open('input', 'r').readlines()]

maxx = len(lines[0])
maxy = len(lines)

movex = [-1, 0, 1, 0]
movey = [0, -1, 0, 1]

current_node = (0, 0)
visited = []
distances = {current_node: 0}
end_node = (maxx-1, maxy-1)
to_test = []

def add_neighbours(whose, where):
	for m in range(len(movex)):
		newx = whose[0] + movex[m]
		newy = whose[1] + movey[m]
		
		if newx < 0 or newx >= maxx or newy < 0 or newy >= maxy:
			continue
		new_node = (newx, newy) # thanks python
		if not new_node in visited:
			where.append(new_node)

def ret_smallest():
	smallest_dist = 1000000000
	node = None
	for i in distances:
		if (not (i in visited)) and (distances[i] < smallest_dist):
			smallest_dist = distances[i]
			node = i
	return node

working = True

while working:
	neighbours = []
	add_neighbours(current_node, neighbours)
	for n in neighbours:
		new_dist = distances[current_node] + int(lines[n[1]][n[0]])
		if not n in distances:
			distances[n] = new_dist
		if new_dist < distances[n]:
			distances[n] = new_dist
	visited.append(current_node)
	current_node = ret_smallest()
#	print(current_node)
	if current_node == None or current_node == end_node:
		break
#	break

#for a in distances:
#	print(a, distances[a])
print(distances[end_node])
#	new_node = current_node + (newx, newy)
#	print(new_node)
