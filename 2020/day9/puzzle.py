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
	currentid = 1	
	thesum = lines[startid]
	while True:
		if(thesum == weak_number and currentid - startid >= 1):
			print(f'Final answer: {min(lines[startid:currentid]) + max(lines[startid:currentid])}')
			break
		elif(thesum > weak_number):
			startid += 1
			currentid = startid + 1
			thesum = lines[startid]
		else:
			thesum += lines[currentid]
			currentid += 1
			
parttwo()
