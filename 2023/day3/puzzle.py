my_input = [line.rstrip() for line in open("input").readlines()]

maxx = len(my_input[0])
maxy = len(my_input)

collected_points = set()
part_numbers = []
gear_ratios = []

def collect_number(my_y, my_x):
	left, right = my_x, my_x
	while not left-1 < 0 and my_input[my_y][left-1].isdigit():
		left -= 1
		#print("Moving left to new position: ", left)
		collected_points.add((my_y, left))

	while not right+1 >= maxx and my_input[my_y][right+1].isdigit():
		right += 1
		#print("Moving right to new position: ", right)
		collected_points.add((my_y, right))
	print("Collecting number: ", my_input[my_y][left:right+1])
	part_numbers.append(int(my_input[my_y][left:right+1]))


def check_neighbours(my_y, my_x):
	move_x = [-1, -1, 0, 1, 1, 1, 0, -1]
	move_y = [0, -1, -1, -1, 0, 1, 1, 1]
	collected_numbers = 0

	for i in range(len(move_x)):
		new_y, new_x = y+move_y[i], x+move_x[i]
		char = my_input[new_y][new_x]
		#print("Neighbour char: ", char)
		if char.isdigit() and not (new_y, new_x) in collected_points:
			collect_number(new_y, new_x)
			collected_numbers += 1

	if my_input[my_y][my_x] == '*' and collected_numbers == 2: # is a gear
		gear_ratios.append(part_numbers[-1] * part_numbers[-2])

for y in range(maxx): # length of a line
	for x in range(maxy): # how many lines there are
		char = my_input[y][x]
		if not char.isdigit() and not char == '.': # it's a symbol
			print(f"Checking for symbol: {char}")
			check_neighbours(y, x)

print("Part numbers: ", sum(part_numbers))
print("Gear ratios: ", sum(gear_ratios))
