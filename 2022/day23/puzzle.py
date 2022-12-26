grove_input = [l.rstrip() for l in open("input").readlines()]
# grove is a square
# nvm not always :(
            
PADDING = 100

grove = [['.' for i in range(len(grove_input) + PADDING*2)] for _ in range(len(grove_input) + PADDING*2)]

for j in range(len(grove_input)):
    for i in range(len(grove_input[0])):
        if grove_input[j][i] == '#':
            grove[j+PADDING][i+PADDING] = '#'

def print_grove():
    for l in grove:
        print(''.join(l))

MOVEMENTS = [
    [(-1, 0), (-1, 1), (-1, -1)], # N, NE, NW
    [(1, 0), (1, 1), (1, -1)], # S, SE, SW
    [(0, -1), (-1, -1), (1, -1)], #W, NW, SW
    [(0, 1), (-1, 1), (1, 1)], #E, NE, SE
]

current_movement = 0 # we start with north movement

def get_movements(x, y):
    potential_movements = []
    for m in range(4):
        move = (current_movement + m) % 4
        has_elves = False
        for my, mx in MOVEMENTS[move]: # put Y first in MOVEMENTS by accident x
            newx, newy = x+mx, y+my
            if grove[newy][newx] == '#': # elf here
                has_elves = True
                break
        if not has_elves:
            potential_movements.append(MOVEMENTS[move][0])
    return potential_movements

def find_borders():
    minx, maxx = 10000, 0
    miny, maxy = 10000, 0

    for j in range(len(grove)):
        for i in range(len(grove[0])):
            if grove[j][i] == '#':
                minx = min(minx, i)
                maxx = max(maxx, i)

                miny = min(miny, j)
                maxy = max(maxy, j)
    return minx, maxx+1, miny, maxy+1

turns = 5000 # for part 1 just make this 10
for t in range(turns):
    # round 1, elves propose movements
    proposals = {}
    i_know_a_spot = {}
    for j in range(len(grove)):
        for i in range(len(grove)):
            if grove[j][i] == '#': # elf
                moves = get_movements(i, j)
                if len(moves) == 4 or len(moves) == 0:
                    # elf cannot move
                    continue
                first_move = moves[0]
                new_spot = (i+first_move[1], j+first_move[0]) 
                proposals[(i,j)] = new_spot# again mixed up x and y
                if new_spot in i_know_a_spot:
                    i_know_a_spot[new_spot] += 1
                else:
                    i_know_a_spot[new_spot] = 1
                # print(f'Elf {i} {j} wants to move to: {moves}')
    
    # round 2, check proposals
    if not proposals:
        # part 2 solution here
        print(f'We are done on turn {t+1} as there are no more moves')
        break
    
    for elf, proposal in proposals.items():
        if i_know_a_spot[proposal] > 1:
            # cant move there, multiple elves know of this cool spot
            continue
        ox, oy = elf
        nx, ny = proposal
        grove[oy][ox] = '.'
        grove[ny][nx] = '#'
    current_movement += 1#(current_movement + 1) % len(current_movement)
    #print_grove()
    #print()

# find borders
minx, maxx, miny, maxy = find_borders()
fsum = 0
for j in range(miny, maxy):
    for i in range(minx, maxx):
        if grove[j][i] == '.':
            fsum += 1
print(fsum)