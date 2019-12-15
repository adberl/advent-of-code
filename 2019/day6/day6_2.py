orbits = open('input.txt', 'r')

orb_data = {}
last_planets = []

for orbit in orbits:
	obj = orbit.rstrip().split(')')
	orb_data[obj[1]] = obj[0] # obj1 is orbiting around obj0
	
# key = object that is orbiting
# value = what is being orbited	
	
for in_orbit, around in orb_data.items():
	if(not in_orbit in orb_data.values()):
		last_planets.append(in_orbit)

last_planets.remove('SAN')
last_planets.remove('YOU')
last_planets.append('COM')

def get_orbited(item):
	orbited = []
	for in_orbit, around in orb_data.items():
		if(around == item):
			orbited.append(in_orbit)
	return orbited

jumps = []
def mintrans(previous, item, depth):
#	print(previous, item, depth)
	if(not (item in orb_data) or item in last_planets):
		return -1
	if(item == 'COM'):
		return -1
	if(item == 'SAN'):
		jumps.append(depth)
	else:
		if(not orb_data[item] == previous):
			mintrans(item, orb_data[item], depth+1)
		for a in get_orbited(item):
			if(previous == a):
				continue
			mintrans(item, a, depth+1)

mintrans('1', 'YOU', 0)

print(jumps[0] - 2)


#for obj, around in orb_data.items():
#	a += ret_orbits(obj)

