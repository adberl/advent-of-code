with open('input', 'r') as f:
	lines = [int(i.strip()) for i in f.readlines()]
	
def partone():
	number = 25	
	while(number <= len(lines ) - 1):
		preamble = lines[number-25:number]
		current = lines[number]
		print(current, preamble)
		flag_hit = False
		for i in preamble:
			for j in preamble:
				if i + j == current and i != j:
					flag_hit = True
		
		if flag_hit == False:
			print(f'Bad number: {current}')
			break
		number += 1

def parttwo():
	weak_number = 3199139634
	startid = 0
	currentid = 0	
	the_set = []
	while True:
		the_set.append(currentid)
		if(sum(the_set) == weak_number and len(the_set) >= 2):
			print(f'Final answer: {the_set[0] + the_set[-1]}')
			break
		elif(sum(the_set) > weak_number):
#			print(f'Too big {the_set}')
			startid += 1
			currentid = startid
			the_set.clear()
		else:
#			print(f'Too small {the_set}')
			currentid += 1
			
parttwo()
