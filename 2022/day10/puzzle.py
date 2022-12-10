program = [l.rstrip().split(' ') for l in open("input").readlines()]

x = 1
clock = 0
signal_strengths = []
screen = []

def check_clock():
	if clock == 20 or (clock-20) % 40 == 0:
		#print(clock, x)
		signal_strengths.append(clock*x)

	sprite = [x-1, x, x+1]
	position = clock%40
	if position-1 in sprite:
		screen.append('#')
	else:
		screen.append('.')
	#print(position, clock, x)
	#print(''.join(screen))


for opcode, *args in program:
	#print(opcode)
	if opcode == 'noop':
		clock += 1
		check_clock()
	elif opcode == 'addx':
		args = int(args[0])
		clock += 1
		check_clock()
		clock += 1
		check_clock()
		x += args

print(sum(signal_strengths))

for sid, char in enumerate(screen):
	if sid % 40 == 0:
		print()
	print(char,end='')