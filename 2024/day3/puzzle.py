import re

my_input = ''.join([line.rstrip() for line in open("input").readlines()])

restr = "mul\\(\\d+,\\d+\\)"

#part1
mps = re.findall(restr, my_input)
mults = []

def do_multiplication(some_mults):
#	print('summing: ', some_mults)
	ret_mults = []
	for mult in some_mults:
		a, b = mult[4:].split(',')
		b = b[:-1]
		ret_mults.append(int(a) * int(b))
	return sum(ret_mults)

print(do_multiplication(mps))

#part2
mul_id = [x.start() for x in re.finditer(restr, my_input)]
do_id = [x.start() for x in re.finditer("do\\(\\)", my_input)]
dont_id = [x.start() for x in re.finditer("don\'t\\(\\)", my_input)]
#print(mul_id, do_id, dont_id)

def find_closest(some_number, some_list):
	best = 0
	for i in some_list:
		if i < some_number:
			best = i
	return best

do_mul = []
for i in range(len(mps)):
	mult_start = mul_id[i]
	closest_do = find_closest(mult_start, do_id)
	closest_dont = find_closest(mult_start, dont_id)
#	print(closest_do, closest_dont)
	if not closest_do and not closest_dont:
		do_mul.append(mps[i])

	elif (closest_do or closest_dont) and \
		closest_do > closest_dont:
		do_mul.append(mps[i])

print(do_multiplication(do_mul))
	
