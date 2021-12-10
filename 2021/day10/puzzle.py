navigation_subsystem = [i.rstrip() for i in open('input', 'r').readlines()]

pairs = {
	'(' : ')',
	'[' : ']',
	'{' : '}',
	'<' : '>'
}

score = {
	')' : 3,
	']' : 57,
	'}' : 1197,
	'>' : 25137
}

fix_score = {
	'(' : 1,
	'[' : 2,
	'{' : 3,
	'<' : 4
}

chunk_open = ['(', '[', '{', '<']
chunk_close = [')', ']', '}', '>']

total_score = 0
fixed_nav_subsystem = navigation_subsystem[:] # cool trick
for line in navigation_subsystem:
	opened_chunks = []
	for char in line:
		if char in chunk_open:
			opened_chunks.append(char)
		elif char in chunk_close:
			tmp_chunk_open = opened_chunks.pop()
			if not pairs[tmp_chunk_open] == char:
				total_score += score[char]
				print(f'in {line} expected {pairs[tmp_chunk_open]} but found {char}')
				fixed_nav_subsystem.remove(line)
				break

print(f'Part 1 score {total_score}')

incomplete_chunks = []
for line in fixed_nav_subsystem:
	opened_chunks = []
	for char in line:
		if char in chunk_open:
			opened_chunks.append(char)
		elif char in chunk_close:
			tmp_chunk_open = opened_chunks.pop()
	incomplete_chunks.append(opened_chunks)

line_scores = []
for chunk in incomplete_chunks:
	total_fix_score = 0
	for a in chunk[::-1]:
		total_fix_score *= 5
		total_fix_score += fix_score[a]
	line_scores.append(total_fix_score)

line_scores.sort()
print(f'Part 2 score {line_scores[len(line_scores)//2]}')
#print(fixed_nav_subsystem)