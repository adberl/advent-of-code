import re

lines = [line.rstrip('\n') for line in open("input").readlines()]

total = 0
for i in range(0, len(lines) - 4, 4):
		
	x1, y1 = (int(x) for x in re.findall(r'\d+', lines[i]))
	x2, y2 = (int(x) for x in re.findall(r'\d+', lines[i+1]))
	s1, s2 = (int(x) for x in re.findall(r'\d+', lines[i+2]))

	# part 2
	s1 += 10000000000000
	s2 += 10000000000000

	y = ((y1 * s1) - (x1 * s2)) / ((y1 * x2) - (x1 * y2))
	x = (s1 - x2 * y) / x1

	if not x.is_integer() or not y.is_integer():
		continue
		
#	if x > 100 or y > 100:
#		continue
		
	total += 3*x + y

# 25531.0 too low
print(total)

