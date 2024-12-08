from itertools import product

equations = [line.rstrip('\n') for line in open("input").readlines()]

def mul(arr):
	ret = 1
	for x in arr:
		ret *= x
	return ret

total = 0
for equation in equations:
	test_val, nums = equation.split(': ')
	
	test_val = int(test_val)
	nums = [int(x) for x in nums.split(' ')]

	print(f'Testing numbers: {test_val} | {nums}')

    #part1
    #operands = '*+'
	#part2
	operands = '*+|'	
	for test_case in product(operands, repeat=len(nums)-1):

		to_eval = []
		for items in zip(nums, test_case + (' ',)):
			to_eval.extend(items)
		
		while len(to_eval) > 2:
			if to_eval[1] == '|':
				to_eval[0] = eval(str(to_eval[0]) + str(to_eval[2]))
			else:
				to_eval[0] = eval(str(to_eval[0]) + to_eval[1] + str(to_eval[2]))
			
			if to_eval[0] > test_val:
				# we went over, early out
				break
			to_eval[1:] = to_eval[3:]		
		
		if to_eval[0] == test_val:
			total += test_val
			print(f'we got one: {to_eval[0]} | total: {total}')
			break	

print(total)
	
