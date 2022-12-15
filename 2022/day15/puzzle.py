cave = [l.rstrip() for l in open("input").readlines()]

y_check = 2000000
cavemap = {}
minx = maxx = 0


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

def part2():
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

#part1()
part2()