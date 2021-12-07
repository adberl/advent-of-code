h_pos = [int(i.rstrip()) for i in open('input', 'r').readline().split(',')]

pos_values = {}

def p2():
	for p in range(max(h_pos)):
		tmp_pos = h_pos
		if not p in pos_values:
			total_fuel = 0
			for a in tmp_pos:
				tmp_sum = 0
				# (n*(n+1))/2
				#for g in range(0, abs(p-a)+1): # this is not smart
				#	tmp_sum += g
				n = abs(p-a)
				total_fuel += (n*(n+1))/2 # this is :D
				#total_fuel += abs(p - a)
			pos_values[p] = total_fuel

def p1():
	for p in h_pos:
		tmp_pos = h_pos
		if not p in pos_values:
			total_fuel = 0
			for a in tmp_pos:
				total_fuel += abs(p - a)
			pos_values[p] = total_fuel


p2()
print(pos_values[min(pos_values, key=pos_values.get)])