depths = [int(i.strip()) for i in open('input', 'r').readlines()]

def part1():
	goes_deeper = 0
	for i in range(len(depths) - 1):
		if depths[i] < depths[i+1]:
			goes_deeper += 1
	return goes_deeper
		
def part2():
	goes_deeper = 0
	for i in range(1, len(depths) - 2):
		first_three = sum(depths[i-1:i+2])
		second_three = sum(depths[i:i+3])
		if first_three < second_three:
			goes_deeper += 1
	return goes_deeper
	
#print(part1())
print(part2())
