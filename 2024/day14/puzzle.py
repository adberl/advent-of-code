import re

lines = [line.rstrip('\n') for line in open("input").readlines()]

maxx = 101
maxy = 103

robots = []
for line in lines:	
	x, y, dx, dy = [int(x) for x in re.findall(r'-?\d+', line)]
	robots.append(((x, y), (dx, dy)))

def print_grid():
	for gy in range(maxy):
		for gx in range(maxx):
			robots_in_square = 0
			for robot in robots:
				(x, y), (dx, dy) = robot
				if x == gx and y == gy:
					robots_in_square += 1
			
			if robots_in_square:
				print(robots_in_square, end='')
			else:
				print('.', end='')
		print()
	print()
		
def is_potential_tree():
	for gy in range(maxy):
		line_guards = 0
		for robot in robots:
			(x, y), (dx, dy) = robot
			if y == gy:
				line_guards += 1
		# if we have one solid line of guards
		if line_guards > 30:
			return True
	return False
		
# for part 1, loop to 100
for k in range(10000):
	for i, robot in enumerate(robots):
		(x, y), (dx, dy) = robot
		robots[i] = ( (((x+dx) % maxx), ((y+dy) % maxy)), (dx, dy) )
	if is_potential_tree():
		print(k)
		print_grid()

quadrants = [0, 0, 0, 0]
for robot in robots:
	# quadrant 1:
	(x, y), (dx, dy) = robot
	if 0 <= x < maxx//2 and 0 <= y < maxy//2:
		quadrants[0] += 1
	elif maxx//2 < x < maxx and 0 <= y < maxy//2:
		quadrants[1] += 1
	elif 0 <= x < maxx//2 and maxy//2 < y < maxy:
		quadrants[2] += 1
	elif maxx//2 < x < maxx and maxy//2 < y < maxy:
		quadrants[3] += 1

safety_factor = 1
for x in quadrants:
	safety_factor *= x
print(safety_factor)



