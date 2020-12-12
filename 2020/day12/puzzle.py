from collections import deque

with open('input', 'r') as f:
	actions = [i.strip() for i in f.readlines()]	

class Coords:
	
	def __init__(self):
		self.v = 0
		self.h = 0
		self.rot = 90
		self.wv = 1
		self.wh = 10
	
	def __str__(self):
		return f'north/south: {self.v} east/west: {self.h} waypoint: ns/ew: {self.wv}/{self.wh}'
	
	def rotate(self, direction, value):
		if(direction == 'R'):
			self.rot += int(value)
		if(direction == 'L'):
			self.rot -= int(value)
		
		if self.rot > 360:
			self.rot = self.rot % 360
		elif self.rot < 0:
			self.rot = 360 - abs(self.rot)
			
	def forwards(self, value):
		if(self.rot == 90):
			self.h += int(value)
		elif(self.rot == 180):
			self.v -= int(value)
		elif(self.rot == 270):
			self.h -= int(value)
		elif(self.rot == 360 or self.rot == 0):
			self.v += int(value)
		else:
			print('something went horribly wrong', self.rot)
			
	#part2 methods
	def move_waypoint(self, direction, value):		
		if(direction == 'N'):
			self.wv += int(value)
		if(direction == 'S'):
			self.wv -= int(value)
		if(direction == 'E'):
			self.wh += int(value)
		if(direction == 'W'):
			self.wh -= int(value)
	def rotate_waypoint(self, direction, value):
		times = int(value) // 90
		#print(times)
		newlist = deque([0, 0, 0, 0]) #n, e, s, w
		if(self.wv >= 0):
			newlist[0] = self.wv
		else:
			newlist[2] = abs(self.wv)
		if(self.wh >= 0):
			newlist[1] = self.wh
		else:
			newlist[3] = abs(self.wh)
		if(direction == 'L'): # n -> w
			newlist.rotate(-times)
		else: # n -> e
			newlist.rotate(times)
		if(newlist[0]):
			self.wv = newlist[0]
		else:
			self.wv = -newlist[2]
		if(newlist[1]):
			self.wh = newlist[1]
		else:
			self.wh = -newlist[3]
		#print(newlist)
		
	def move_to_waypoint(self, value):
		self.v += int(value) * self.wv
		self.h += int(value) * self.wh
			
def partone():
	coord = Coords()
	for action in actions:
		direction = action[0]
		value = action[1:]	
		
		if(direction == 'N'):
			coord.v += int(value)
		if(direction == 'S'):
			coord.v -= int(value)
		if(direction == 'E'):
			coord.h += int(value)
		if(direction == 'W'):
			coord.h -= int(value)
		if(direction == 'L' or direction == 'R'):
			coord.rotate(direction, value)
		if(direction == 'F'):
			coord.forwards(value)
	print(coord)
	print('part one solution:', abs(coord.h) + abs(coord.v))
	
def parttwo(): 
	coord = Coords()
	for action in actions:
		direction = action[0]
		value = action[1:]
		
		if(direction in 'NSEW'):
			coord.move_waypoint(direction, value)
		if(direction in 'LR'):
			coord.rotate_waypoint(direction, value)
		if(direction == 'F'):
			coord.move_to_waypoint(value)
		print(action, coord)
	print('part two solution:', abs(coord.h) + abs(coord.v))
partone()
parttwo()
