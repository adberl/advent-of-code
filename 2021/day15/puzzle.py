lines = [i.rstrip() for i in open('input', 'r').readlines()]

maxx = len(lines[0])
maxy = len(lines)

min_path = 100000000

def move_to(currentx, currenty, path):
	movx = [0, 1]
	movy = [1, 0]
	global min_path
	for k in range(len(movx)):
		newx = currentx + movx[k]
		newy = currenty + movy[k]
		
		if newx >= maxx or newy >= maxy:
			continue
		elif newx == maxx-1 and newy == maxy-1:
			potential_min = path + int(lines[newy][newx])
			if potential_min < min_path:
				min_path = potential_min
		else:
#			print(newx, newy, lines[newy][newx], maxx, maxy)
			potential_min = path + int(lines[newy][newx])
			if potential_min > min_path:
				continue
			else:
				move_to(newx, newy, potential_min)
			
move_to(0,0, 0)
print(min_path)
