f = [i.rstrip() for i in open('input', 'r').readlines()]

all_line_segments = []
max_x, max_y = -1, -1

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

def process_data():
	for line in f:
		point1, point2 = [i.split(',') for i in line.split(' -> ')]
		obj_p1 = Point(int(point1[0]), int(point1[1]))
		obj_p2 = Point(int(point2[0]), int(point2[1]))
		all_line_segments.append(Segment(obj_p1, obj_p2))


	

if __name__ == "__main__":
	process_data()
