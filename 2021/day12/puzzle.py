cave_system = [i.rstrip() for i in open('input', 'r').readlines()]

path = {}
all_paths = []

for line in cave_system:
	cave_first, cave_next = line.split('-')
	if cave_first in path:
		path[cave_first].append(cave_next)
	else:
		path[cave_first] = [cave_next]
	if cave_next in path: # gotta add them both ways A<->b; A can go to b and b to A
		path[cave_next].append(cave_first)
	else:
		path[cave_next] = [cave_first]

def traverse(current_cave, traversed, small_cave_twice):
	if(current_cave == 'end'):
		all_paths.append(traversed)
		return
	#if not current_cave in path: # it's a dead end cave, we cant get back from it
	#	return
	for a in path[current_cave]: # where can we go from current cave
		if(a == 'start'): # cannot travel back to start
			continue
		if (not is_large_cave(a)) and (a in traversed) and small_cave_twice: # we cant go into a small cave that's already been traversed
			continue
		if (not is_large_cave(a)) and (a in traversed) and not small_cave_twice: 
			small_cave_twice = True
#		print(f'Going to {a}')
			been_to = traversed[::1]
			been_to.append(a)
			traverse(a, been_to, small_cave_twice)
			small_cave_twice = False
		else:
			been_to = traversed[::1]
			been_to.append(a)
			traverse(a, been_to, small_cave_twice)

def is_large_cave(cave):
	for char in cave:
		if not (char >= 'A' and char <= 'Z'):
			return False
	return True

#print(path)
traverse('start', ['start'], False)
#for a in all_paths:
#	print(a)
print(len(all_paths))