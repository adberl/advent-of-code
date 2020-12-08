with open('input', 'r') as f:
	lines = [i.strip() for i in f.readlines()]
	
accumulator = 0
program_counter = 0
visited = []
working = True
cp_ins = ""
cp_pc = 0
cp_visited = 0
cp_acc = 0
flag_changed = False
	
def checkpoint(instr, newpc):
#	print(f'Checkpoint at PC: {program_counter} ({newpc}) with instr {instr}')
	global cp_ins, cp_pc, cp_visited, cp_acc, flag_changed
	cp_ins = instr
	cp_pc = newpc
	cp_visited = len(visited) - 1
	cp_acc = accumulator
	flag_changed = True
	
def restore_checkpoint():
#	print('Restoring checkpoint')
	global program_counter, accumulator, visited, flag_changed
	program_counter = cp_pc
	accumulator = cp_acc
	visited = visited[:cp_visited]
	flag_changed = False

while working:
	if(program_counter == len(lines)):
		working = False
		print(f'Accumulator is {accumulator}')
		continue		

	if program_counter in visited:
		restore_checkpoint()
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
		ival = 0
		if(sign == '+'):
			ival += int(val)
		else:
			ival -= int(val)

		if(not flag_changed): 
			checkpoint('jmp', program_counter + ival)
			program_counter += 1
		else:
			program_counter += ival

	if(instruction == 'nop'):
		if(not flag_changed):
			checkpoint('nop', program_counter + 1)
			if(sign == '+'):
				program_counter += int(val)
			else:
				program_counter -= int(val)
		else:
			program_counter += 1
