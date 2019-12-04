w1 = set()
w2 = set()

intersections = {(-820, -300), (-837, -300), (-555, -43), (-354, -43), (-136, -155), (-389, -205), (-354, -155), (-247, -155)}

distd = {}
distz = {}

lastx = 1
lasty = 1

file1 = open('input.txt', 'r')

wire1, wire2 = file1.readlines()

wire1 = wire1.rstrip().split(',')
wire2 = wire2.rstrip().split(',')
steps = 0

for entry in wire1:
	direction = entry[0]
	amount = int(entry[1:])
	if(direction == 'R'):
		for i in range(1, amount + 1):
			point = ((lastx + i), lasty)
			w1.add(point)
			steps += 1
			if(point in intersections):
				if(not point in distd):
					distd[point] = steps
			
		lastx = lastx + amount
	if(direction == 'L'):
		for i in range(1, amount + 1):
			point = (((lastx - i), lasty))
			w1.add(point)
			steps += 1
			if(point in intersections):
				if(not point in distd):
					distd[point] = steps
		lastx = lastx - amount
	if(direction == 'U'):
		for i in range(1, amount + 1):
			point = ((lastx, lasty + i))
			w1.add(point)
			steps += 1
			if(point in intersections):
				if(not point in distd):
					distd[point] = steps
		lasty = lasty + amount
	if(direction == 'D'):
		for i in range(1, amount + 1):
			point = ((lastx, lasty - i))
			w1.add(point)
			steps += 1
			if(point in intersections):
				if(not point in distd):
					distd[point] = steps
		lasty = lasty - amount

lastx = 1
lasty = 1
steps = 0 #initially forgot to reset number of steps so i rewrote the thing epic style

for entry in wire2:
	direction = entry[0]
	amount = int(entry[1:])
	if(direction == 'R'):
		for i in range(1, amount + 1):
			point = ((lastx + i), lasty)
			w2.add(point)
			steps += 1
			if(point in intersections):
				if(not point in distz):
					distz[point] = steps
			
		lastx = lastx + amount
	if(direction == 'L'):
		for i in range(1, amount + 1):
			point = (((lastx - i), lasty))
			w2.add(point)
			steps += 1
			if(point in intersections):
				if(not point in distz):
					distz[point] = steps
		lastx = lastx - amount
	if(direction == 'U'):
		for i in range(1, amount + 1):
			point = ((lastx, lasty + i))
			w2.add(point)
			steps += 1
			if(point in intersections):
				if(not point in distz):
					distz[point] = steps
		lasty = lasty + amount
	if(direction == 'D'):
		for i in range(1, amount + 1):
			point = ((lastx, lasty - i))
			w2.add(point)
			steps += 1
			if(point in intersections):
				if(not point in distz):
					distz[point] = steps
		lasty = lasty - amount

point = (0,0)
max_steps = 999999999999		
for point, steps in distd.items():
	if steps+distz[point] < max_steps:
		max_steps = steps+distz[point]

print(distd)
print(distz)
print('-----------')
print(max_steps)
print(w1 & w2)


#dist = abs(point[0] - 1) + abs(point[1] - 1)
"""		
intersections = w1 & w2

min_distance = 99999999

for point in intersections:
	dist = abs(point[0] - 1) + abs(point[1] - 1)
	if dist < min_distance:
		min_distance = dist
		
print(min_distance)
"""
