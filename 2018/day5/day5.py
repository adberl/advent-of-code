import time

start = time.process_time()

gpolymer = open('input.txt', 'r').readline()
gpolymer = gpolymer[:-1] #get rid of '\n'

min_polymer = len(gpolymer)

def reactpolymer(polymer):
	did_react = 1

	while did_react:
		did_react = 0
		i = 0
		
		while (i < len(polymer) - 1):
			current_unit = ord(polymer[i])
			next_unit = ord(polymer[i+1])
			
			if(abs(current_unit - next_unit) == 32):
				polymer = polymer[:i] + polymer[i+2:]
				did_react=1
				
			i += 1
	return len(polymer)		

for i in range(0, 25):
	
	current = reactpolymer(gpolymer.replace(chr(65+i), '').replace(chr(97+i), ''))
	min_polymer = current if current < min_polymer else min_polymer
	
print(min_polymer)
print(time.process_time() - start)
