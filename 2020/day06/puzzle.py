with open('input', 'r') as f:
	lines = [i.strip() for i in f.readlines()]
allgroups = []
group_common = []
current_group = set()	
for line in lines:
	if line == '':
		allgroups.append(set.intersection(*group_common))
		current_group = set()
		group_common = []
	else:
		for question in line:
			current_group.add(question)
		group_common.append(current_group)
		current_group = set()
total_question = 0
for group in allgroups:
	total_question += len(group)
print(total_question)
