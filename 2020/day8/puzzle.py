with open('input', 'r') as f:
	lines = [i.strip() for i in f.readlines()]
	
accumulator = 0
program_counter = 0
visited = []
working = True

while working:
	if program_counter in visited:
		working = False
		print(f'Accumulator is {accumulator}')
		continue
	
	visited.append(program_counter)

	instruction, val = lines[program_counter].split(' ')
	sign = val[:1]
	val = val[1:]
	
	if(instruction == 'acc'):
		if(sign == '+'):
			accumulator += int(val)
		else:
			accumulator -= int(val)
		program_counter += 1
	if(instruction == 'jmp'):
		if(sign == '+'):
			program_counter += int(val)
		else:
			program_counter -= int(val)
	if(instruction == 'nop'):
		program_counter += 1
	
