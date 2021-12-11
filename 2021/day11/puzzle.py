height_map = [[int(j) for j in list(i.strip())] for i in open('input', 'r').readlines()]

#print(height_map)

movements = [
(-1, 0),
(-1, -1),
(0, -1),
(1, -1),
(1, 0),
(1, 1),
(0, 1),
(-1, 1)
]

max_x, max_y = (10, 10)

class Octopus:
	octopuses = [ [ None for y in range(max_y) ] for x in range(max_x) ]
	flashes = 0
	def __init__(self, x, y, energy):
		self.x = x
		self.y = y
		self.energy = energy
		self.flashed = False
		
	def step(self):
		if(self.flashed):
			return
		self.energy += 1
		if(self.energy > 9):
			self.flash()
			self.energy = 0

	def end_turn(self):
		self.flashed = False

	def flash(self):
		self.flashed = True
		Octopus.flashes += 1
		for movx, movy in movements:
			newx = movx+self.x
			newy = movy+self.y
			if newx < 0 or newx >= max_x or newy < 0 or newy >= max_y:
				continue
			else:
				Octopus.octopuses[newy][newx].step()

	def __str__(self):
		return str(self.energy)
		
	def __repr__(self):
		return self.__str__()
		
def p1():

	for xoct in range(max_x):
		for yoct in range(max_y):
#			print(f'Adding octopus ({xoct, yoct}) with energy {height_map[yoct][xoct]}')
			Octopus.octopuses[yoct][xoct] = Octopus(xoct, yoct, height_map[yoct][xoct])
	
#	print(f'before any steps:\n', Octopus.octopuses)
	for k in range(1000):
		for i in range(max_x):
			for j in range(max_y):
				Octopus.octopuses[j][i].step()
		all_flashed = True	
		for i in range(max_x):
			for j in range(max_y):
				if(not Octopus.octopuses[j][i].flashed):
					all_flashed = False
				Octopus.octopuses[j][i].end_turn()

		if False:
			print(f'Turn {k+1} map: ')
			for m in Octopus.octopuses:	
				print(m)		

		if(all_flashed):
			print(k+1)
			return
			

	print(f'Total flashes: {Octopus.flashes}')
p1()
