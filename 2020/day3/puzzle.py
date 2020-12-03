slopemap = [i.strip() for i in open('input', 'r').readlines()]
slopemap = slopemap[1:]

def partone():
	whereami = 0
	trees = 0

	for oneslope in slopemap:
		
		whereami += 3

		if(whereami >= len(oneslope)):
			whereami = whereami % len(oneslope)

		if(oneslope[whereami] == '#'):
			trees += 1
			print(f'tree hit!!!\t {oneslope} [{whereami}]')
		else:
			print(f'tree not hit!!!\t {oneslope} [{whereami}]')


	print(trees)
		

def parttwo(right, down):
	whereami = 0
	trees = 0
	count = 1

	for oneslope in slopemap:
		if count % down != 0:
			count += 1
			continue

		whereami += right

		if(whereami >= len(oneslope)):
			whereami = whereami % len(oneslope)

		if(oneslope[whereami] == '#'):
			trees += 1
			print(f'tree hit!!!\t {oneslope} [{whereami}]')
		else:
			print(f'tree not hit!!!\t {oneslope} [{whereami}]')

		count += 1
	print('------------ [ end slope ] -------------------')
	return trees


slopes = [(1, 1), (3, 1), (5, 1), (7,1), (1, 2)]
alltrees = 1

for sl in slopes:
	print(sl)
	treesonslope = parttwo(sl[0], sl[1])
	alltrees *= 1 if not treesonslope else treesonslope

print(alltrees)

