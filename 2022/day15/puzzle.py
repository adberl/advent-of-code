cave = [l.rstrip() for l in open("input").readlines()]

y_check = 2000000
cavemap = {}
minx = maxx = 0
sensor_ranges = {}

def get_distance(sensor, beacon):
	sum = 0
	for i in range(2):
		sum += abs(sensor[i] - beacon[i])

	return sum

for s in cave:
	sens, beac = s.split(': closest beacon is at ')
	sens = sens.replace('Sensor at ', '')
	sens = tuple([int(x.split('=')[1]) for x in sens.split(', ')])
	beac = tuple([int(x.split('=')[1]) for x in beac.split(', ')])

	cavemap[sens] = beac

	dist = get_distance(sens, beac)
	minx = min(sens[0]-dist, minx)
	maxx = max(sens[0]+dist, maxx)

for s,b in cavemap.items():
	sensor_ranges[s] = get_distance(s, b)

def part1():
	res = 0
	for i in range(minx, maxx):
		#print(f'Checking point: {(i, y_check)}')
		for sensor, beacon in cavemap.items():
			sensor_range = get_distance(sensor, beacon)
			distance_to_sensor = get_distance((i, y_check), sensor)
			#print(f'Distance to sensor {sensor} is {distance_to_sensor} and it has range {sensor_range}')
			if distance_to_sensor <= sensor_range and \
				(i, y_check) not in cavemap and \
				(i, y_check) not in cavemap.values():
				res += 1
				break
	print(res)

def part2_bruteforce(): # this takes 11 years, dont do this 
	for i in range(4000000):
		for j in range(4000000):
			potential_distress_beacon = (i, j)
			occupied = False
			for sensor, beacon in cavemap.items():
				sensor_range = get_distance(sensor, beacon)
				distance_to_sensor = get_distance(potential_distress_beacon, sensor)
				#print(f'Distance to sensor {sensor} is {distance_to_sensor} and it has range {sensor_range}')
				if distance_to_sensor <= sensor_range or \
					potential_distress_beacon in cavemap or \
					potential_distress_beacon in cavemap.values():
					occupied = True
					break
			if not occupied:
				print(f'We found him at {potential_distress_beacon}!')
				print(f'Tuning frequency: {potential_distress_beacon[0]*4000000+potential_distress_beacon[1]}')
		print(f'{i}/4000000')
		break

def get_skip(x, y): 
	for sensor, s_range in sensor_ranges.items():
		if get_distance((x,y), sensor) > s_range:
			continue

		#print(f'Distance to sensor{sensor} is {get_distance((x,y), sensor)} and its reach is: {s_range}')

		y_dist = abs(sensor[1]-y)
		points_covered = (s_range - y_dist) #* 2 + 1

		# new pos we should check on the first is (14, 0)
		x_dist = abs(sensor[0]-x)
		if x <= sensor[0]: # we are on the left side
			#print(f'We are on the left side! of sensor {sensor}')
			skip_ahead = x_dist + points_covered + 1 + (0 if y_dist else 1) # if we are in the same row as the sensor, we skip the sensor aswell
			#print(skip_ahead)
		else: # we are on the right side
			#print(f'We are on the right side! of sensor {sensor}')
			skip_ahead = points_covered - (x_dist-2)
			#print(skip_ahead, points_covered, x_dist)
		
		#print(f'my new pos: {(x+skip_ahead, y)}')
		return skip_ahead

MAX_COORD = 4000000
def part2(): # this takes about a minute and a bit more
	for y in range(MAX_COORD):
		x = 0
		found = False
		while x < MAX_COORD: # loop through X and check columns
			skip = get_skip(x, y)
			if skip == None:
				print(f'We found him at {x, y}!')
				print(f'Tuning frequency: {x*4000000+y}')
				found = True
				break
			x += skip
		#print(f'{y+1}/{MAX_COORD}')
		if found:
			break


# (8,7): range:9:
# on line 0: 6->10 (including both)
# on line 1: 5->11
# on line 2: 4->12
# formula: RANGE-OURY (distance on Y axis basically) * 2 + 1

#part1()
part2()
# even with trying my best to brute-force this solution, part2 ended in ~1 minute
# if you're brave enough to see how this works, uncomment some of the prints