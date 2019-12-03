noun = 0
verb = 0

while(True):

	if(noun == 99 and verb == 99):
		break
	
	if(verb == 99):
		noun = noun + 1
		verb = 0
	else:
		verb = verb + 1

	print(noun, verb)
	file1 = open('input.txt', 'r')	
	memory = file1.read().rstrip().split(',')
	memory = [int(item) for item in memory]
	
	memory[1] = noun
	memory[2] = verb

	ptr = 0
	try:
		while(True):
			if(memory[ptr] == 1): # addition
				a = memory[memory[ptr+1]]
				b = memory[memory[ptr+2]]
				memory[memory[ptr+3]] = a + b
			elif(memory[ptr] == 2): # mul
				a = memory[memory[ptr+1]]
				b = memory[memory[ptr+2]]
				memory[memory[ptr+3]] = a * b
			else:
				break
			ptr = ptr+4
	except:
		print('exception occured')
		continue
	if(memory[0] == 19690720):		
		print(100 * noun + verb)
		break
