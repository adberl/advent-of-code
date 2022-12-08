forest = [l.rstrip() for l in open("input").readlines()]

forest_size = len(forest)

def is_visible(row, col):
	if row == 0 or row == forest_size-1:
		return True
	if col == 0 or col == forest_size-1:
		return True

	my_tree_size = int(forest[row][col])
	#print(f'currently checking: {my_tree_size}({row},{col}):')
	# check row
	hit_bigger_top = False
	hit_bigger_bottom = False
	hit_bigger_left = False
	hit_bigger_right = False
	for i in range(forest_size):
		some_tree_size = int(forest[row][i])
		other_tree_size = int(forest[i][col])
		#print(f'row: {row}, {i}: {some_tree_size}\t col: {i}, {col}: {other_tree_size}')
		if some_tree_size >= my_tree_size:
			if i == col:
				pass
			elif i < col:
				hit_bigger_left = True
			else:
				hit_bigger_right = True
			#print(f'set {hit_bigger_left} {hit_bigger_right} on {row} {i} ({some_tree_size})')
		if other_tree_size >= my_tree_size:
			if i == row:
				pass
			elif i < row:
				hit_bigger_top = True
			else:
				hit_bigger_bottom = True

	#print(hit_bigger_top, hit_bigger_bottom, hit_bigger_left, hit_bigger_right)
	visible = not ((hit_bigger_top and hit_bigger_bottom) and\
		(hit_bigger_left and hit_bigger_right))
	#print(visible)
	return visible

def first_larger(where, my_val):
	for i in range(len(where)):
		if where[i] >= my_val:
			return i+1
	return len(where)

def get_scenic_score(row, col):
	left = right = top = down = 0
	my_tree_size = forest[row][col]
	to_the_right = forest[row][col+1:]
	to_the_left = list(reversed(forest[row][:col]))
	above = ''
	below = ''
	for i in range(forest_size):
		if i < row:
			above += forest[row-i-1][col]
		if i > row:
			below += forest[i][col]

	r = first_larger(to_the_right, my_tree_size)
	l = first_larger(to_the_left, my_tree_size)
	a = first_larger(above, my_tree_size)
	b = first_larger(below, my_tree_size)
	#print(r, l, a, b)
	scenic_score = r*l*a*b
	#print(f'{my_tree_size} ({row}, {col}): {to_the_right} | {to_the_left} | {above} | {below} - {scenic_score}')	
	return scenic_score

def part1():
	total_visible = 0
	for row in range(len(forest)):
		for col in range(len(forest[0])):
			#print(row, col, '-', forest[row][col])
			total_visible += is_visible(row, col)
	return total_visible

def part2():
	scenic_score = []
	for row in range(len(forest)):
		for col in range(len(forest[0])):
			#print(row, col, '-', forest[row][col])
			scenic_score.append(get_scenic_score(row, col))

	return max(scenic_score)

print(part1())
print(part2())