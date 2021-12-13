lines = [i.rstrip() for i in open('input', 'r').readlines()]

maxx, maxy = 0,0
read_maxes = 0
for line in lines: # determine max in a very inefficient way
	if line == '':
		continue
	if line[0] == 'f':
		dontcare, mymax = line.split('=')
		mymax = int(mymax)
		read_maxes += 1
		if(read_maxes == 1):
			maxx = mymax*2 + 1
		else:
			maxy = mymax*2 + 1
			break
	else:
		continue
dots = [[0 for x in range(maxx)] for y in range(maxy)]

folds = []
for line in lines:
	if line == '': # we've arrived at folds
		continue
	elif line[0] == 'f': # folds here
		folds.append(line.split('along ')[1])
	else:
		x, y = [int(i) for i in line.split(',')]
		dots[y][x] = 1
		
for fold in folds:
	axis, pos = fold.split('=')
	pos = int(pos)
	if(axis == 'x'):
		for j in range(maxy):
			for i in range(pos):
				dots[j][i] += dots[j][maxx-1-i]
		maxx = pos
		for i in range(len(dots)):
			dots[i] = dots[i][:maxx]
	elif(axis == 'y'):
		for j in range(pos):
			for i in range(maxx):
				dots[j][i] += dots[maxy-1-j][i]
		maxy = pos
		dots = dots[:maxy]
#	break

total_dots = 0
viz = True
for a in dots:
	for b in a:
		if b >= 1:
			total_dots += 1
			if viz:
				print('#', end='')
		else:
			if viz:
				print('.', end='')
			pass
	if viz:
		print()

#print(maxx, maxy)
print(total_dots)
