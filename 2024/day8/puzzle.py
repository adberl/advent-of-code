from itertools import combinations

antennas = [line.rstrip('\n') for line in open("input").readlines()]

lenx = len(antennas[0])
leny = len(antennas)

# some more processing
freq = {}
for y in range(leny):
	for x in range(lenx):
		char = antennas[y][x]
		if char == '.':
			continue
			
		if char in freq:
			freq[char].append((x,y))
		else:
			freq[char] = [(x,y)]

def addt(t1, t2):
	return (t1[0] + t2[0], t1[1] + t2[1])
	
def subt(t1, t2):
	return (t1[0] - t2[0], t1[1] - t2[1])

def is_valid(x, y):
	return 0 <= x < lenx and 0 <= y < leny

def ripple(p, t):
	ripples = []
	while True:
		p = addt(p, t)
		if is_valid(*p):
			ripples.append(p)
		else:
			break	
	return ripples

def raycast(p1, p2):
	ripples = []

	rt1 = subt(p1, p2)
	ripples += ripple(p1, rt1)

	rt2 = subt(p2, p1)
	ripples += ripple(p2, rt2)

#	r1 = addt(p1, subt(p1, p2))
#	r2 = addt(p2, subt(p2, p1))
	return ripples

antinodes = set()
for freq, positions in freq.items():
	if len(positions) > 1:
		antinodes.update(positions)
	for a, b in combinations(positions, 2):
		print(f'doing: {a}, {b}')
		antinodes.update(raycast(a, b))
#		m, n = raycast(a, b)
#		if is_valid(*m):
#			antinodes.add(m)
#		if is_valid(*n):
#			antinodes.add(n)
		

print(len(antinodes))
for y in range(leny):
	for x in range(lenx):
		if (x, y) in antinodes:
			print('#', end='')
		else:
			print(antennas[y][x], end='')
	print()

