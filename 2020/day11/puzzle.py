from copy import copy

with open('input', 'r') as f:
	room = [i.strip() for i in f.readlines()]	

mx = [0, 1, 1, 1, 0, -1, -1, -1]
my = [-1, -1, 0, 1, 1, 1, 0, -1]

while True:
	newroom = copy(room)
	for i in range(len(room)):
		for j in range(len(room[0])):
			nempty = 0
			noccupied = 0
#			print(f'Neighbours for {room[i][j]}[{i},{j}]:')
			for m in range(len(mx)):
				nothit = True
				posx = j
				posy = i
				while nothit:
					posx = posx + mx[m]
					posy = posy + my[m]
#					print(posx, posy)
					if(0 <= posx < len(room[0]) and 0 <= posy < len(room)):
						if(room[posy][posx] == '.'):
							continue
						else:
							nothit = False
					else:
						nothit = False
				if(0 <= posx < len(room[0]) and 0 <= posy < len(room)): #position is valid
					if(room[posy][posx] == '#'):
						noccupied += 1
					elif(room[posy][posx] == 'L'):
						nempty += 1
#					print(f'{room[posy][posx]}[{posy},{posx}]')
			if(room[i][j] == 'L' and noccupied == 0):
				l = list(newroom[i])
				l[j] = '#'
				newroom[i] = ''.join(l)
			elif(room[i][j] == '#' and noccupied >= 5):
				l = list(newroom[i])
				l[j] = 'L'
				newroom[i] = ''.join(l)
	if room == newroom:
#		print('Rooms are the same')
		break
	else:
#		print('Rooms are different')
		room = newroom

occupied = 0
for row in room:
	for i in row:
		if(i == '#'):
			occupied += 1
			
print(f'Final occupied seats: {occupied}')
