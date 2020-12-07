with open('input', 'r') as f:
	lines = [i.strip() for i in f.readlines()]
	
bag_graph = {}

for line in lines:
	container, containee = line.split('contain')
	container = container[:-6]
	if(containee == ' no other bags.'):
		continue
	containee = containee.split(',')
	containee_temp = []
	for c in containee:
		if(c[1] == '1'):
			containee_temp.append((1, c[3:-4].rstrip()))
		else:
			containee_temp.append((int(c[1]), c[3:-5].rstrip()))
	containee = containee_temp
	
	if (container in bag_graph):
		bag_graph[container] += containee
	else:
		bag_graph[container] = containee
#	print(container, '\t', containee)
	
def can_contain(bag):
	ret = 0
	if bag in bag_graph:
#		print(f'{bag} has children {bag_graph[bag]}')
		for child in bag_graph[bag]:
			if child[1] == 'shiny gold':
				return 1
			else:
				ret += can_contain(child[1])
	return 1 if ret >= 1 else 0

def partone():
	total = 0

	for bag in bag_graph:
	#	print(f'looking for {bag}')
		can = can_contain(bag)
		total += can
	return total
	
def count_children(bag):
	total = 0
#	print(f'counting children for {bag}')
	if bag in bag_graph:
		for child in bag_graph[bag]:
			total += child[0] + child[0] * count_children(child[1]) if (child[1] in bag_graph) else child[0]
#			print(total, child[0], child[1])
	return total
	
def parttwo():
	return count_children('shiny gold')
	
print('part one answer: ', partone())
print('part two answer: ', parttwo())
