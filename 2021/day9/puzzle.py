height_map = [[int(j) for j in list(i.strip())] for i in open('input', 'r').readlines()]

max_x = len(height_map[0])
max_y = len(height_map)

low_points = []

def is_smallest(i, j):
	our_number = height_map[j][i] 
	for movx, movy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
		newx = movx+i
		newy = movy+j
#		print(f"i:{i},j:{j} | movx:{movx}, movy:{movy} | newx:{newx}, newy:{newy}")
		if newx < 0 or newx >= max_x or newy < 0 or newy >= max_y:
			continue
#		print(f"i:{i},j:{j} | movx:{movx}, movy:{movy} | newx:{newx}, newy:{newy}")
#		print(our_number, height_map[newy][newx])
		if our_number >= height_map[newy][newx]:
			return False
	return True

def p1():
	total_risk_level = 0
	#print(max_x, max_y)
	for i in range(max_x):
		for j in range(max_y):
			if is_smallest(i, j):
	#			print("is smallest: ", height_map[j][i])
				total_risk_level += height_map[j][i] + 1
				low_points.append((j,i))
	print(f"total risk level: {total_risk_level}")

def determine_basin(already_visited, coord):
#	print(low_points)
	i = coord[1]
	j = coord[0]
	basins = 1
	our_number = height_map[j][i] 
#	print(already_visited, coord, our_number)
	for movx, movy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
		newx = movx+i
		newy = movy+j
		if newx < 0 or newx >= max_x or newy < 0 or newy >= max_y:
			continue
		if height_map[newy][newx] == 9:
			continue
		if (newy, newx) in already_visited:
			continue
		if our_number < height_map[newy][newx]: #it can trickle down from the new number, we check its basin too!
			#tmp_arr = already_visited.append()
			already_visited.append((newy, newx))
			basins += determine_basin(already_visited, (newy, newx))
	return basins

def p2():
	all_basins = []
	for low_point in low_points:
#		print(f"TESTING NEW LOW POINT: {low_point}")
		all_basins.append(determine_basin([low_point], low_point))
	all_basins.sort()
	mul = 1
	for k in all_basins[-3:]:
		mul *= k
	
	print(f"{mul}")

p1()
p2()
