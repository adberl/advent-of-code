orbits = open('input.txt', 'r')

orb_data = {}
last_planets = []

for orbit in orbits:
	obj = orbit.rstrip().split(')')
	orb_data[obj[1]] = obj[0] # obj1 is orbiting around obj0
	
# key = object that is orbiting
# value = what is being orbited	
	
for obj, around in orb_data.items():
	if(not obj in orb_data):
		last_planets.append(obj)

print(last_planets)

def get_orbited(item):
	orbited = []
	for obj, around in orb_data.items():
		if(obj == item):
			orbited.append(around)
	print(item, orbited)
	return orbited

jumps = []
def mintrans(item, depth):
	if(not (item in orb_data) or item in last_planets):
		return
	if(item == 'SAN'):
		jumps.append(depth)
	else:
		mintrans(orb_data[item], depth+1)
		for a in get_orbited(item):
			mintrans(orb_data[a], depth+1)

mintrans('YOU', 0)

print(jumps)


#for obj, around in orb_data.items():
#	a += ret_orbits(obj)

