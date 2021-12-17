import re
line = open('input', 'r').readline().rstrip()

all_coords = [int(i) for i in re.findall(r'-?\d+', line)]
x1, x2 = all_coords[0:2]
y1, y2 = all_coords[2:4]

def check_returns(xvel, yvel):
	x, y = 0, 0
	highest = 0
	gotcha = False
	while True: # a step
		x += xvel
		y += yvel
		if y > highest:
			highest = y
		if xvel > 0:
			xvel -= 1
		elif xvel < 0:
			xvel += 1
		yvel -= 1
		if (x1 <= x <= x2) and (y1 <= y <= y2):
			gotcha = True
			break
		if x > x2 or y < y1:
			break
	return gotcha, highest

maxy = -1
alls = []

for i in range(-10, x2+5):
	for j in range(-200, 200):
		good_landing, highest = check_returns(i, j)
		if good_landing:
			alls.append(1)
		if good_landing and (highest > maxy):
			maxy = highest

print(maxy, len(alls))