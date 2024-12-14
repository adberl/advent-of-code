my_input = [line.rstrip() for line in open("input").readlines()]

reflections = []
tmp_arr = []

for line in my_input:
	if line == '' and len(tmp_arr) > 0:
		reflections.append(tmp_arr)
		tmp_arr= []
	else:
		tmp_arr.append(line)

def test_line(someline, i):
	return someline[0:i+1] == someline[i+1:(i+1)*2][::-1]

def test_reflection(someref, part2=False):
	bad_indices = set(range(len(someref[0])))
	print(bad_indices)
	for i in range(len(someref[0])//2):
		
		mirrored = True
		for line in someref:
			if not test_line(line, i):
				mirrored = False
				if not part2: 
					break
				bad_indices &= i

		if mirrored:
			#print(f"For map: {someref} we got index {i+1}")	
			return i+1
			break

		mirrored = True
		for line in someref:
			if not test_line(line[::-1], i):
				mirrored = False
				break

		if mirrored:
			#print(f"For map: {someref} we got index {len(someref[0])-i-1}")
			return len(someref[0])-i-1

# part 1
#total_score = 0
#for ref in reflections:
#	ret = test_reflection(ref) 
#	if not ret: # we couldn't find a vertical one
#		rot = [[ref[i][j] for i in range(len(ref))] for j in range(len(ref[0])-1, -1, -1)]
#		for line in rot:
#			print(''.join(line))
#		ret = test_reflection(rot) * 100
#	total_score += ret
#print(total_score)

for ref in reflections:
	ret = test_reflection(ref, True)
