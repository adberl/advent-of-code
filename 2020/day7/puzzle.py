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
			containee_temp.append(c[3:-4].rstrip())
		else:
			containee_temp.append(c[3:-5].rstrip())
	containee = containee_temp
	
	if (container in bag_graph):
		bag_graph[container] += containee
	else:
		bag_graph[container] = containee
	print(container, '\t', containee)
	
def can_contain(current, path):
	ret = 0
	print(current, path)
	if current in path:
		return ret
	if not current in bag_graph:
		return ret
	else:
		for a in bag_graph[current]:
			if(a == 'shiny gold'):
				ret += 1
			else:
				path.append(a)
				ret += can_contain(a, path)
	return ret	

total = 0
for bag in bag_graph:
	total += can_contain(bag, [])
print(total)
