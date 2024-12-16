garden = [[x for x in line.rstrip('\n')] for line in open("input").readlines()]

maxx = len(garden[0])
maxy = len(garden)

movx = [1, 0, -1, 0]
movy = [0, 1, 0, -1]
directions = ['right', 'down', 'left', 'up']

plot_details = {}
plot_raycasts = {}

def is_valid(x, y):
	return 0 <= x < maxx and \
		0 <= y < maxy

def get_hash(x, y):
	return y * maxy + x

def unhash(somehash):
	return (somehash % maxx, somehash // maxx)

def is_aligned(x1, y1, x2, y2):
	return x1 == x2 or y1 == y2

def get_distance(pos1, pos2):
	x1, y1 = pos1
	x2, y2 = pos2
	return abs(x2 - x1) + abs(y2 - y1)

def traverse(x, y, region):
	plot_hash = get_hash(x, y)
	if plot_hash in plot_details:
		return
		
	friends, enemies = set(), set()
	current_plot = garden[y][x]
	region.add(plot_hash)

	direction = 0
	for dx, dy in zip(movx, movy):
		next_pos = (x + dx, y + dy)
		next_hash = next_pos[1] * maxy + next_pos[0]

		if is_valid(*next_pos):
			if current_plot == garden[y + dy][x + dx]:
				friends.add(next_hash)
			else:
				enemies.add(next_hash)

				# RAYCAST
				raycast = (next_pos, directions[direction])
				if plot_hash in plot_raycasts:
					plot_raycasts[plot_hash].append(raycast)
				else:
					plot_raycasts[plot_hash] = [raycast]
				# RAYCAST
					
		else:
			# border region
			enemies.add(next_hash)
			
			# RAYCAST
			raycast = (next_pos, directions[direction])
			if plot_hash in plot_raycasts:
				plot_raycasts[plot_hash].append(raycast)
			else:
				plot_raycasts[plot_hash] = [raycast]
			# RAYCAST
		
		direction+= 1	

	plot_entry = ((x, y), friends, enemies)
	plot_details[plot_hash] = plot_entry
		
	for friend in friends:
		traverse(*unhash(friend), region)


regions = []
for y in range(maxy):
    for x in range(maxx):
    	region = set()
    	traverse(x, y, region)
    	if region:
	    	regions.append(region)

#print('region')
#for region in regions:
#	for a in region:
#		x, y = unhash(a)
#		code = garden[y][x]
#		break
#	print(code, region)
 
cost = 0  	
bulk_discount = 0
for region in regions:
	area = 0
	perimeter = 0
	sides = 0
	raycasts = []
	plot_char = None
	
	for plot_hash in region:
			pos, friends, enemies = plot_details[plot_hash]
			area += 1
			perimeter += len(enemies)
			if plot_hash in plot_raycasts:
				raycasts += plot_raycasts[plot_hash]
			
			if not plot_char:
				plot_char = garden[pos[1]][pos[0]]
	
	potential_sides = {}
	for pos, direction in raycasts:
		if direction in potential_sides:
			potential_sides[direction].append(pos)
		else:
			potential_sides[direction] = [pos]
		
	for direction, side in potential_sides.items():
		lines = []
		for x in side:
			aligned = False
			for line in lines:
				for y in line:
					x1, y1 = x
					x2, y2 = y
					
					cool_aligned = False
					if direction in ['left', 'right']:
						cool_aligned = x1 == x2
					else:
						cool_aligned = y1 == y2
			
					if cool_aligned:
						aligned = True
					
					else:
						aligned = False
						break
				
				if aligned:
					line.append(x)
					break
			if not aligned:
				lines.append([x])
		
		for line in lines:
			sortline = sorted(line, key=lambda k: [k[0], k[1]])
			sides += 1
	
			for i in range(len(sortline)-1):
				if get_distance(sortline[i], sortline[i+1]) > 1:
					sides += 1		

	bulk_discount += area * sides
	cost += area * perimeter		


print(cost)
print(bulk_discount)
    
    
    

