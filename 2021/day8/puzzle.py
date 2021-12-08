f = [i.rstrip() for i in open('input', 'r').readlines()]

digit_out_count = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
total_good_digits = 0

def p1():
	for entry in f:
		signal_pattern, digit_output = [i.split(' ') for i in entry.split(' | ')]
		for i in digit_output:
			if len(i) in [2,4,3,7]:
				total_good_digits += 1

def p2():
	total_counter = 0
	for entry in f:
		signal_pattern, digit_output = [i.split(' ') for i in entry.split(' | ')]
		fds = {}
		found_lines = {}
		found_digits = {}
		#finding line a
		for a in signal_pattern:
			if len(a) == 2:
				fds[1] = set(a)
				found_digits[1] = a
			elif len(a) == 4:
				fds[4] = set(a)
				found_digits[4] = a
			elif len(a) == 3:
				fds[7] = set(a)
				found_digits[7] = a
			elif len(a) == 7:
				fds[8] = set(a)
				found_digits[8] = a
		found_lines['a'] = list(fds[7].difference(fds[1]))[0] # we set it to a character
		# found line a

		# finding line e or g
		found_lines['eg'] = fds[8].difference(fds[7].union(fds[4]))
		# found either one of them
		
		# determining exact e and g
		all_that_contain_six = [i for i in signal_pattern if len(i) == 6]
		for otcs in all_that_contain_six:
			potential_e = set(found_lines['eg']).difference(otcs)
			#print(potential_e)
			if len(potential_e) == 1:
				fds[9] = set(otcs)
				found_digits[9] = otcs
				found_lines['e'] = list(potential_e)[0]
				found_lines['g'] = list(found_lines['eg'].difference(potential_e))[0]
				found_lines.pop('eg')
				all_that_contain_six.remove(otcs)
				break
		# determined exact e and g
		
		# determine c	
		for otcs in all_that_contain_six:
			potential_c = fds[1].difference(otcs)
			if(len(potential_c)) == 1:
				found_lines['c'] = list(potential_c)[0]
				fds[6] = set(otcs)
				found_digits[6] = otcs
				all_that_contain_six.remove(otcs)
				break
		fds[0] = set(all_that_contain_six[0])
		found_digits[0] = all_that_contain_six[0]
		# determined c

		# determine number five
		all_that_contain_five = [i for i in signal_pattern if len(i) == 5]
		for atcf in all_that_contain_five:
			potential_e = fds[6].difference(set(atcf))
			if len(potential_e) == 1:
				found_digits[5] = atcf
				fds[5] = set(atcf)
				all_that_contain_five.remove(atcf)
				#print("potential d5: ", potential_d5)
		# found what digit 5 looks like :D

		# finding 2:
		for atcf in all_that_contain_five:
			if(found_lines['e'] in atcf):
				found_digits[2] = atcf
				fds[2] = set(atcf)
				all_that_contain_five.remove(atcf)
		found_digits[3] = all_that_contain_five[0]
		fds[3] = set(all_that_contain_five[0])

		digits_mapping = {}
		for a in found_digits:
			digits_mapping[found_digits[a]] = a
			#print(found_digits[a])

#		print(found_lines)
#		print(fds)
#		print(found_digits)
#		print(digits_mapping)
#		print(digit_output)

		tmp = ""
		for a in digit_output:
			for b in fds:
				if set(a) == fds[b]:
					tmp += str(b)
		print(tmp)
		total_counter += int(tmp)
	print(total_counter)
	
p2()
#print(total_counter)
#print(total_good_digits)