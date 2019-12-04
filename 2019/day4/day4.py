

def pt1():
	total_pws = 0
	for i in range(284639, 748759 + 1):
		pw = str(i)
		previous = pw[0]
		based = 0
		redpilled = 1
		for current in pw[1:]:
			if(previous == current):
				based = 1
			if(previous > current):
				redpilled = 0
			previous = current
		if(based and redpilled):
			total_pws += 1
	return total_pws
	
def pt2():
	total_pws = 0
	for i in range(284639, 748759 + 1):
		pw = str(i)
		previous = pw[0]
		based = 0
		redpilled = 1
		mdict = {}
		mdict[previous] = 1
		for current in pw[1:]:
			if current in mdict:
				mdict[current] += 1
			else:
				mdict[current] = 1
			if(previous > current):
				redpilled = 0
			previous = current
		for key, value in mdict.items():
			if(value == 2):
				based = 1
				break
		if(based and redpilled):
			total_pws += 1
	return total_pws	

	
print(pt2())
