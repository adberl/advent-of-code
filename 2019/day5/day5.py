mem = open('input.txt', 'r').read().rstrip().split(',')

def mint(nr):
	if(type(nr) is str):
		return int(nr)
	else:
		return nr
		
# len of mem: 678
addr = 0
while(True):
	instruction = mem[addr]
	opcode = instruction[-2:] if len(instruction) >= 2 else '0' + instruction	
	modes = [0, 0, 0]
	i = 2
	for m in reversed(instruction[:-2]):
		modes[i] = mint(m)
		i -= 1
	
#	print(opcode)
	
	if(opcode == '99'):
		break
	elif(opcode == '08'): #equal
		a = mint(mem[addr+1]) if modes[2] == 1 else mint(mem[mint(mem[addr+1])])
		b = mint(mem[addr+2]) if modes[1] == 1 else mint(mem[mint(mem[addr+2])])
		put = 0
		if(a == b):
			put = 1

		mem[mint(mem[addr+3])] = put
		addr += 4
	elif(opcode == '07'): #less-than
		a = mint(mem[addr+1]) if modes[2] == 1 else mint(mem[mint(mem[addr+1])])
		b = mint(mem[addr+2]) if modes[1] == 1 else mint(mem[mint(mem[addr+2])])
		put = 0
		if(a < b):
			put = 1

		mem[mint(mem[addr+3])] = put
		addr += 4
	elif(opcode == '06'): #jump-if-false
		which = mint(mem[addr+1]) if modes[2] == 1 else mint(mem[mint(mem[addr+1])])
		if(which == 0):
			addr = mint(mem[addr+2]) if modes[1] == 1 else mint(mem[mint(mem[addr+2])])
		else:
			addr += 3
	elif(opcode == '05'): #jump-if-true
		which = mint(mem[addr+1]) if modes[2] == 1 else mint(mem[mint(mem[addr+1])])
		if(which != 0):
			addr = mint(mem[addr+2]) if modes[1] == 1 else mint(mem[mint(mem[addr+2])])
		else:
			addr += 3
	elif(opcode == '04'):
		where = mint(mem[addr + 1])
		mode = 1 if instruction[0] == '1' else 0
		print('dc:', mem[where] if mode == 0 else where)
		addr += 2
	elif(opcode == '03'):
		where = mint(mem[addr + 1])
		mem[where] = '5'
		addr += 2
	elif(opcode == '02'): #multiply
		a = mint(mem[addr+1]) if modes[2] == 1 else mint(mem[mint(mem[addr+1])])
		b = mint(mem[addr+2]) if modes[1] == 1 else mint(mem[mint(mem[addr+2])])
#		print(a, b)
		mem[mint(mem[addr+3])] = str(a * b)
		addr += 4
	elif(opcode == '01'): #add
		a = mint(mem[addr+1]) if modes[2] == 1 else mint(mem[mint(mem[addr+1])])
		b = mint(mem[addr+2]) if modes[1] == 1 else mint(mem[mint(mem[addr+2])])
#		print(a, b)
		mem[mint(mem[addr+3])] = str(a + b)
		addr += 4
	else:
		print('unkown opcode')
		break
	print(instruction, modes)
#	break
