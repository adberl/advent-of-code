drawing = [l.rstrip() for l in open("input").readlines()]

bunches = {}
whereami = 0
for l in drawing:
	#print(l, l[1])
	whereami += 1
	if(l == ''):
		break
	elif(l[1] == '1'):
		continue
	midx = 0
	current = 1
	for m in l.split(' '):
		if(m == ''):
			midx += 1
			if(midx % 4 == 0):
				current += 1
		else:
			crate = m.replace('[', '').replace(']', '')
			#print(crate)
			if current in bunches:
				bunches[current] += crate
			else:
				bunches[current] = [crate]
			current += 1

for k in bunches:
	bunches[k] = list(reversed(bunches[k]))

def part1():
	for l in drawing[whereami:]:
		newl = l.replace('move ', '').replace('from ', '').replace('to ', '')
		how_many, from_where, to_where = [int(i) for i in newl.split(' ')]
		for i in range(how_many):
			bunches[to_where] += bunches[from_where].pop()
	#print(bunches)

def part2():
	for l in drawing[whereami:]:
		newl = l.replace('move ', '').replace('from ', '').replace('to ', '')
		how_many, from_where, to_where = [int(i) for i in newl.split(' ')]

		bunches[to_where] += bunches[from_where][-how_many:]
		bunches[from_where] = bunches[from_where][:-how_many]
#part1()
part2()
final = ''
for i in range(len(bunches)):
	final += bunches[i+1].pop()
print(final)

		
	#print(l.split(' '))
	