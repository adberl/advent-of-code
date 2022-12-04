ranges = [l.rstrip() for l in open("input").readlines()]

def check_contains(elf1, elf2):
	a1,b1 = elf1
	a2,b2 = elf2
#	print(f"{a1} <= {a2}:", a1 <= a2)
#	print(f"{b1} >= {b2}:", b1 >= b2)
	return (a1 <= a2) and (b1 >= b2)

def check_overlap(elf1, elf2):
	a1,b1 = elf1
	a2,b2 = elf2

	if a1 == a2 or b1 == b2 or b2 == a1 or b1 == a2:
		return True
	if b1 >= a2:
	    return True
	return False

total = 0
overlap_total = 0
for range in ranges:
	#elf1 = ['11', '12']
	elf1, elf2 = [x.split('-') for x in range.split(',')]
	elf1 = [int(i) for i in elf1]
	elf2 = [int(i) for i in elf2]
	
	contained = False
	if elf1[0] < elf2[0]:
		contained = check_contains(elf1, elf2)
		overlapping = check_overlap(elf1, elf2)
	elif elf1[0] == elf2[0] or elf1[1] == elf2[1]:
		contained = True
		overlapping = True
	else:
		contained = check_contains(elf2, elf1)
		overlapping = check_overlap(elf2, elf1)
	if contained:
#		print("contained!", elf1, elf2)
		total += 1
	print(f'overlapping: {overlapping}\t {elf1}, {elf2}')
	overlap_total += overlapping

#511 low
print(total)
print(overlap_total)
