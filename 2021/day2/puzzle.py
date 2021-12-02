lines = open('input', 'r').readlines()

def part1():
	depth, h_pos = 0, 0
	for line in lines:
		direction, amount = line.split(' ')
		amount = int(amount)
		
		if(direction == "forward"):
			h_pos += amount
		elif(direction == "down"):
			depth += amount
		elif(direction == "up"):
			depth -= amount
	return depth * h_pos

def part2():
	depth, h_pos, aim = 0, 0, 0
	for line in lines:
		direction, amount = line.split(' ')
		amount = int(amount)
		
		if(direction == "forward"):
			h_pos += amount
			depth += aim * amount
		elif(direction == "down"):
			aim += amount
		elif(direction == "up"):
			aim -= amount
	return depth * h_pos

	
print("part 1: ", part1())
print("part 2: ", part2())
