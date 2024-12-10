topographic_map = [[int(x) for x in line.rstrip('\n')] for line in open("input").readlines()]

maxx = len(topographic_map[0])
maxy = len(topographic_map)

def is_valid(nextx, nexty, depth):
	if (0 <= nextx < maxx) and \
		(0 <= nexty < maxy) and \
		topographic_map[nexty][nextx] == depth+1:

		return True
	return False

def traverse(x, y, depth, path, pathset):
	if depth == 9:
		print(f'We did it! {x}, {y}', path)
		pathset.add((path[0], path[-1]))
		return 1
	
	movx = [1, 0, -1, 0]
	movy = [0, 1, 0, -1]
	
#	print(f'Currently on: {x}, {y}', path)
	
	total = 0
	for dx, dy in zip(movx, movy):
		nextx = x + dx
		nexty = y + dy
		
		if is_valid(nextx, nexty, depth):
			total += traverse(nextx, nexty, depth+1, path+[(nextx,nexty)], pathset)
	return total

total = 0
unique_paths = set()
for y in range(maxy):
	for x in range(maxx):
		if topographic_map[y][x] == 0:
			print(f'Start point at: {x}, {y}')
			total += traverse(x, y, 0, [(x,y)], unique_paths)

print(len(unique_paths))
print(total)
