reports = [line.rstrip('\n') for line in open("input").readlines()]
 
# they're square
max_len = len(reports)
 
target = 'XMAS'
 
def is_valid(coordinate):
    return 0 <= coordinate < max_len
 
movx = [0, 1, 1, 1, 0, -1, -1, -1]
movy = [-1, -1, 0, 1, 1, 1, 0, -1]
 
target = 'XMAS'
paths = set()
def check_tile(x, y, depth, direction, path):
    good_letter = reports[y][x] == target[depth]
    if depth == len(target) - 1 and good_letter:
        print(f'We found one!', path)
        paths.update(path)
        return True
        
    if good_letter:
        # go deeper
        print(f'Going deeper on: ({x},{y}) | {reports[y][x]}')
        dx, dy = movx[direction], movy[direction]
        nextx = dx + x
        nexty = dy + y
 
        if is_valid(nextx) and is_valid(nexty):
            if check_tile(nextx, nexty, depth+1, direction, path + [(x,y)]):
                return True

    return False

total = 0
# convention: reports[y][x]
for y in range(max_len):
    for x in range(max_len):
        if reports[y][x] == target[0]:
            # found an X, let's start checking every neighbour
            print(f'Found an X at: {x}, {y} - going deeper!')
            for direction in range(len(movx)):
                dx, dy = movx[direction], movy[direction]
                nextx = dx + x
                nexty = dy + y
 
                if is_valid(nextx) and is_valid(nexty):
                    # start walking in that direction
                    if check_tile(nextx, nexty, 1, direction, [(x,y)]):
                        total += 1
                        #break
 
print(total)

def debug():
    for sy in range(max_len):
        for sx in range(max_len):
            print(reports[sy][sx] if (sx, sy) in paths else '.', end='')
        print()

# part 2  
dir1 = [(-1, -1),(1, 1)]
dir2 = [(1, -1), (-1, 1)]
# M A S or S A M in an X pattern

def get_direction(x, y, which_dir):
    x1 = x + which_dir[0][0]
    y1 = y + which_dir[0][1]

    x2 = x + which_dir[1][0]
    y2 = y + which_dir[1][1]
    return x1, x2, y1, y2

def is_direction_good(x1, x2, y1, y2):
    if is_valid(x1) and is_valid(x2) and \
        is_valid(y1) and is_valid(y2):
        if (reports[y1][x1] == 'M' and \
            reports[y2][x2] == 'S') or \
            (reports[y1][x1] == 'S' and \
            reports[y2][x2] == 'M'):
            return True
    return False
                    
total2 = 0
for y in range(max_len):
    for x in range(max_len):
        if reports[y][x] == 'A':
            dir1_good = is_direction_good(*get_direction(x, y, dir1))
            dir2_good = is_direction_good(*get_direction(x, y, dir2))
            if dir1_good and dir2_good:
                total2 += 1

print(total2)
