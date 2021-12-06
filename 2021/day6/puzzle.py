f = [int(i.rstrip()) for i in open('input', 'r').readline().split(',')]

all_lanternfish = []

class Lanternfish:
	
	def __init__(self, timer):
		self.timer = timer
	
	def tick(self):
		if(self.timer == 0): 
			self.timer = 6
			return True
		else:
			self.timer -= 1
			return False

for a in f:
	all_lanternfish.append(Lanternfish(a))
"""	
for i in range(80): # 80 days part 1, 256 days part 2 :D
	for i in range(len(all_lanternfish)):
		if(all_lanternfish[i].tick()):
			all_lanternfish.append(Lanternfish(8))
			
print(len(all_lanternfish))
"""

lanternfish = [0] * 9 # 0 to 8 days
#setup list

for lf in f:
	current = int(lf)
	lanternfish[current] += 1
	
def tick():
	new_spawns = lanternfish.pop(0)
	lanternfish[6] += new_spawns
	lanternfish.append(new_spawns)
	
for i in range(256):
	tick()
	
print(sum(lanternfish))
#print(lanternfish)
