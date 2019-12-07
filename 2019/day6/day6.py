orbits = open('input.txt', 'r')

orb_data = {}
orb_dist = {}

for orbit in orbits:
	obj = orbit.rstrip().split(')')
	orb_data[obj[1]] = obj[0] # obj1 is orbiting around obj0
	
def ret_orbits(item):
	if(not (item in orb_data)):
		return 0;
	if(orb_data[item] == 'COM'):
		return 1;
	return ret_orbits(orb_data[item]) + 1;

a = 0
for obj, around in orb_data.items():
	a += ret_orbits(obj)
print(a)
