original_diskmap = [[int(x) for x in line.rstrip('\n')] for line in open("input").readlines()][0] # sure we don't need index 0

diskmap = {}
current_position = 0

def add_to_diskmap(fid, start, stop):
	if fid in diskmap:
		diskmap[fid].append((start, stop))
	else:
		diskmap[fid] = [(start, stop)]	

file_id = 0
for i, file_size in enumerate(original_diskmap, 1):

	start = current_position
	stop = current_position+file_size
	current_position = stop

	if start == stop:
		# zero size
		continue

	if i % 2 == 0:
		# empty space
		add_to_diskmap(-1, start, stop)
	else:
		# actual file
		add_to_diskmap(file_id, start, stop)
		file_id += 1

def get_rightmost_id():
	max_right = 0
	max_id = -1
	for file_id, pos in diskmap.items():
		if file_id == -1:
			continue # pass over empty files
		for start, stop in pos:
			if stop > max_right:
				max_right = stop
				max_id = file_id
			
	return max_id, max_right

def is_valid_disk():
	fid, rstop = get_rightmost_id()
	
	for start, stop in diskmap[-1]:
		if start < rstop:
			return False
	return True

def get_leftmost_empty():
	min_left = 100000000000
	min_id = -1
	for i, pos in enumerate(diskmap[-1]):
		start, stop = pos
		if start < min_left:
			min_left = start
			min_id = i
			
	return min_id#, min_left

def add_new_file_block(fileid, position):
#	print(f'Adding new position for fileid: {fileid} at position {position}')
#	print(f'Here are the possible positions: {diskmap[fileid]}')
	for i, a in enumerate(diskmap[fileid]):
		start, stop = a
		if start <= position <= stop:
			# technically can only occur at the ends
#			print('how how how')
#			print(f'Found where to add: {start}, {stop} -> {start}, {stop+1}')
			diskmap[fileid][i] = [start, stop+1]#.append((start, stop+1))
			return
#	print(f'Couldnt find where to add, so adding at: {fileid}: {position}, {position+1}')
	diskmap[fileid].append((position, position+1))
		
def get_diskmap_arr():
	max_right = 0
	for fid, pos in diskmap.items():
		for start, end in pos:
			max_right = max(max_right, end)
	empty_array = [None] * max_right
	
	for fid, pos in diskmap.items():
		for start, end in pos:
			for i in range(start, end):

				char = str(fid)
				if fid == -1:
					char = '.'
				elif fid == None:
					char = '#'
					
				empty_array[i] = char
	return empty_array

def part1():		
	p_iter = 0
	while not is_valid_disk():

	#	print('START DISKMAP')
	#	print(diskmap)
	#	print(diskmap_str)
	#	print(f'Iteration: {p_iter} | {''.join(get_diskmap_arr())}')
		p_iter += 1
		
		fid, max_right = get_rightmost_id()
		file_empty = -1
		empty_empty = -1
		for i, m in enumerate(diskmap[fid]):
			start, stop = m
			if stop == max_right:
	#			print(f'We need to process: {fid} with coordinates: {start}, {stop}')
				# we found the position we need to process
				newstop = stop-1
	#			print(diskmap[fid])
				
				# just pop it
				diskmap[fid].pop(i)
				if newstop > start:
					# theres still some data left in this range
					diskmap[fid].append((start, newstop))
	#			print(diskmap[fid])
					
				eid = get_leftmost_empty()
				empty_start, empty_stop = diskmap[-1][eid]
				new_empty_start = empty_start + 1
				
				diskmap[-1].pop(eid)
				if new_empty_start < empty_stop:
					diskmap[-1].append((new_empty_start, empty_stop))
				
	#			print(f'Swapping positions:')
				add_new_file_block(-1, stop-1)
				add_new_file_block(fid, empty_start)
	#			print(f'END DISKMAP:', diskmap)
				break

def find_leftmost_good_span(size):
	min_left = 100000000000
	min_id = -1
	for i, pos in enumerate(diskmap[-1]):
		start, stop = pos
		if start < min_left and stop-start >= size:
			min_left = start
			min_id = i
			
	return min_id#, min_left	

def part2():
	p_iter = 0
	print(f'Iteration: {p_iter} | {''.join(get_diskmap_arr())}')
	for key in reversed(sorted(diskmap.keys())):
		if key == -1:
			continue
			
		start, stop = diskmap[key][0]
		
		span_id = find_leftmost_good_span(stop-start)
		if span_id == -1:
			# couldn't find a span
			continue
	
		span_start, span_stop = diskmap[-1][span_id]
	
		if span_start > start:
			continue
	
		diskmap[-1].pop(span_id)
		diskmap[key].pop(0)
	
		span_size = span_stop - span_start
		file_size = stop - start
		
		if span_size > file_size:
			diskmap[-1].append((span_start+file_size, span_stop))
	
	
		for i in range(0, stop-start):
			add_new_file_block(-1, i+start)
			add_new_file_block(key, i+span_start)

		p_iter += 1
#		print(f'Iteration: {p_iter} | {''.join(get_diskmap_arr())}')

		


#part1()
part2()
total = 0
for i, char in enumerate(get_diskmap_arr()):
	if char == '.':
		continue
		
	total += i * int(char)


print(f'Final look: {''.join(get_diskmap_arr())}')
#print(diskmap)
print(total)
