report = [int(i.strip()) for i in open('input', 'r').readlines()]

for i in report: # maybe dont read from start each time :\
	for j in report:
		for k in report:
			if i + j + k == 2020:
				print(i * j * k)
		
