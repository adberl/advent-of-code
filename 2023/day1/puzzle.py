my_input = [line.rstrip() for line in open("input").readlines()]

numbers_alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def find_num_in_list(numbers_list, line):
	min_index = 100000 # arbitrarily large minimum
	min_index_value = 0	
	for num in numbers_list:
		try:
			num_index = line.index(num)
		except ValueError:
			continue
		if not num_index == -1 and num_index < min_index:
			min_index = num_index
			min_index_value = numbers_list.index(num)
	return min_index, min_index_value

global_calibration_value = 0
for line in my_input:

	min_index, min_index_value = find_num_in_list(numbers_alpha, line)
	min_index2, min_index_value2 = find_num_in_list(numbers_digit, line)
	calibration_value = (min_index_value if min_index < min_index2 else min_index_value2) * 10
	global_calibration_value += calibration_value
	
	min_index, min_index_value = find_num_in_list([x[::-1] for x in numbers_alpha], line[::-1])
	min_index2, min_index_value2 = find_num_in_list([x[::-1] for x in numbers_digit], line[::-1])
	calibration_value2 = (min_index_value if min_index < min_index2 else min_index_value2)
	global_calibration_value += calibration_value2
	
#	print(calibration_value + calibration_value2)

print(global_calibration_value)            
