diagnostic_report = [list(i.strip()) for i in open('input', 'r').readlines()]

def part1():
	bit_size = len(diagnostic_report[0])
	bit_zero = [0] * bit_size
	bit_one = [0] * bit_size
	both_bits = [bit_zero, bit_one]
	for bin_num in diagnostic_report:
		for i in range(bit_size):
			bit = int(bin_num[i])
			both_bits[bit][i] += 1
	gamma_rate = ""
	epsilon_rate = ""
	for i in range(bit_size):
		if(both_bits[0][i] > both_bits[1][i]):
			gamma_rate += "0"
			epsilon_rate += "1"
		else:
			gamma_rate += "1"
			epsilon_rate += "0"
	return int(gamma_rate, 2) * int(epsilon_rate, 2)
	
def calc_counts(array_where):
	bit_size = len(array_where[0])
	both_bits = [[0] * bit_size, [0] * bit_size]
	for bin_num in array_where:
			for i in range(bit_size):
				bit = int(bin_num[i])
				both_bits[bit][i] += 1
	return both_bits

def oxygen_criteria(start_array):
	#most common value, if equally common return ones with 1
	found = False
	i = 0
	while not found:
		counts = calc_counts(start_array)
		if(counts[0][i] > counts[1][i]): # 0 is more common
			start_array = list(filter(lambda x: (x[i] == '0'), start_array))
		elif(counts[0][i] <= counts[1][i]): # 1 is more common or they're equal
			start_array = list(filter(lambda x: (x[i] == '1'), start_array))
		if(len(start_array) == 1):
			found = True
			return int("".join(start_array[0]), 2) # return as int
		else:
			i += 1

def co2_criteria(start_array):
	#least common value, if equally common return ones with 0
	found = False
	i = 0
	while not found:
		counts = calc_counts(start_array)
		if(counts[0][i] <= counts[1][i]): # 1 is more common or they're equal
			start_array = list(filter(lambda x: (x[i] == '0'), start_array))
		elif(counts[0][i] > counts[1][i]): # 0 is more common
			start_array = list(filter(lambda x: (x[i] == '1'), start_array))
		if(len(start_array) == 1):
			found = True
			return int("".join(start_array[0]), 2) # return as int
		else:
			i += 1

def part2():
	return oxygen_criteria(diagnostic_report) * co2_criteria(diagnostic_report)
print(part2())
#print(part1())
