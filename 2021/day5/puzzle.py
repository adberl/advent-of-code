f = [i.rstrip() for i in open('input', 'r').readlines()]

all_line_segments = []
diagonal_line_segments = []

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __str__(self):
		return f"({str(self.x)},{str(self.y)})"
	
class Segment():
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def __str__(self):
		return "" + str(self.p1) + "->" + str(self.p2)

	def ret_common(self):
		if self.p1.x == self.p2.x:
			return 'x'
		elif self.p1.y == self.p2.y:
			return 'y'

	def fix_coords(self):		
		if self.ret_common() == 'x': # x is the same
			if self.p1.y > self.p2.y:
				self.p1.y, self.p2.y = self.p2.y, self.p1.y
		elif self.ret_common() == 'y':
			if self.p1.x > self.p2.x:
				self.p1.x, self.p2.x = self.p2.x, self.p1.x



def process_data():
	tmax_x = -1
	tmax_y = -1
	for line in f:
		point1, point2 = [i.split(',') for i in line.split(' -> ')]
		obj_p1 = Point(int(point1[0]), int(point1[1]))
		obj_p2 = Point(int(point2[0]), int(point2[1]))
		
		tmax_x = max(obj_p1.x, obj_p2.x, tmax_x)
		tmax_y = max(obj_p1.y, obj_p2.y, tmax_y)
		
		if(obj_p1.x == obj_p2.x or obj_p1.y == obj_p2.y):
			tmax_x = max(obj_p1.x, obj_p2.x, tmax_x)
			tmax_y = max(obj_p1.y, obj_p2.y, tmax_y)

			all_line_segments.append(Segment(obj_p1, obj_p2))
		else:
			diagonal_line_segments.append(Segment(obj_p1, obj_p2))
	return tmax_x+1, tmax_y+1


def setup_vent_area(max_x, max_y):
	return [[0] * max_x for _ in range(max_y)]

def process_vent_area(vent_area):
	for seg in all_line_segments:
		seg.fix_coords()
		if seg.ret_common() == 'x':
			the_x = seg.p1.x
			for i in range(seg.p1.y, seg.p2.y+1):
				vent_area[i][the_x] += 1
		elif seg.ret_common() == 'y':
			the_y = seg.p1.y
			for i in range(seg.p1.x, seg.p2.x+1):
				vent_area[the_y][i] += 1
	return vent_area

def draw_diagonals(vent_area):
	for seg in diagonal_line_segments:
		dist = abs(seg.p1.x - seg.p2.x)
		x_inc = 0
		y_inc = 0

		if seg.p1.x > seg.p2.x:
			x_inc = -1
		else:
			x_inc = 1

		if seg.p1.y > seg.p2.y:
			y_inc = -1
		else:
			y_inc = 1

		startx = seg.p1.x
		starty = seg.p1.y
#		print(seg, end=' | ')
		for i in range(dist+1):
#			print(startx, starty, end=' | ')
			vent_area[starty][startx] += 1
			startx += x_inc
			starty += y_inc
#		print()
	return vent_area

def solve(vent_area):
	tmp_sum = 0
	for x in vent_area:
		for y in x:
			if y >= 2:
				tmp_sum += 1
	return tmp_sum

def print_all_line_segments():
	for seg in all_line_segments:
		print(seg)

def print_vent_area(vent_area):
	for i in vent_area:
		for j in i:
			print(j, end = ' ')
		print()

if __name__ == "__main__":
	max_x, max_y = process_data()
	vent_area = setup_vent_area(max_x, max_y)
#	print_all_line_segments()
	vent_area = process_vent_area(vent_area)
	vent_area = draw_diagonals(vent_area)
#	print_vent_area(vent_area)
	print(solve(vent_area))
