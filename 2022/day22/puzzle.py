import re

board = [l.rstrip() for l in open("input").readlines()]
path = re.findall(r'\d+[LR]*', board[-1])
path[-1] = path[-1] + 'E' # UGLYYYYYY
max_line_len = len(max(board[:-2], key=len))
board = board[:-2]

RIGHT, DOWN, LEFT, UP = 0,1,2,3

for i, line in enumerate(board):
    newline = line.replace(' ', '~') + '~' * (max_line_len-len(line))
    board[i] = newline
    #print(newline)


# 133 % 50 => 33

def get_region(x, y):
    if 100 <= x < 150 and 0 <= y < 50:
        return 1
    elif 50 <= x < 100 and 0 <= y < 50:
        return 2
    elif 50 <= x < 100 and 50 <= y < 100:
        return 3
    elif 50 <= x < 100 and 100 <= y < 150:
        return 4
    elif 0 <= x < 50 and 100 <= y < 150:
        return 5
    elif 0 <= x < 50 and 150 <= y < 200:
        return 6
    else:
        print('ERROR ERROR WTF HOW DID WE END UP HERE')
        exit()

def get_region_starts(region):
    match region:
        case 1:
            return 100, 0
        case 2:
            return 50, 0
        case 3:
            return 50, 50
        case 4: 
            return 50, 100
        case 5:
            return 0, 100
        case 6:
            return 0, 150

region_movements = dict({
    # (new region, new direction im facing, inverse)
    1: [
        (4, LEFT, True),
        (3, LEFT, False),
        (2, LEFT, False),
        (6, UP, False),
    ],
    2: [
        (1, RIGHT, False),
        (3, DOWN, False),
        (5, RIGHT, True),
        (6, RIGHT, False),
    ],
    3: [
        (1, UP, False),
        (4, DOWN, False),
        (5, DOWN, False),
        (2, UP, False),
    ],
    4: [
        (1, LEFT, True),
        (6, LEFT, False),
        (5, LEFT, False),
        (3, UP, False),
    ],
    5: [
        (4, RIGHT, False),
        (6, DOWN, False),
        (2, RIGHT, True),
        (3, RIGHT, False),
    ],
    6: [
        (4, UP, False),
        (1, DOWN, False),
        (2, DOWN, False),
        (5, UP, False),
    ],
})


my_dir = 0 # 
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # +2 to skip to the opposite

current_pos = (board[0].find('.'),0)

def add_tuples(t1, t2):
    return tuple([sum(tup) for tup in zip(t1, t2)])

for move in path:
    amount, *rotate = int(move[:-1]), move[-1]
    #print(f'We\'re currently doing: {amount} {rotate}')

    #print(f'Current region: {get_region(current_pos[0], current_pos[1])}')
    for m in range(amount):
        xmove, ymove = directions[my_dir]
        
        newx = (current_pos[0] + xmove) % len(board[0])
        newy = (current_pos[1] + ymove) % len(board)

        #print(f'Trying to move to: {board[newy][newx]}')
        if board[newy][newx] == '~':
            old_region = get_region(current_pos[0], current_pos[1])
            new_region, new_dir, inverse = region_movements[old_region][my_dir]
            swap_coordinates = my_dir != new_dir and my_dir != (new_dir + 2) % len(directions)
            startx, starty = get_region_starts(new_region)
            
            #print(f'From region {old_region} trying to move to {new_region} by going {my_dir} and i will be moving {new_dir}')
            #print(current_pos, xmove, ymove, len(board[0]), newx, newy, swap_coordinates)
            
            if swap_coordinates:
                newx, newy = newy, newx

            if inverse:
                #print('inverse')
                oldstartx, oldstarty = get_region_starts(old_region)
                newx = oldstartx + 50 - (newx % 50) - 1
                newy = oldstarty + 50 - (newy % 50) - 1

            #print(newx, newy)
            match (new_dir + 2) % len(directions):
                # the side i'm popping in from is
                # always opposite of my moving direction
                # eg im moving left, means i popped up on right
                case 0: # right
                    newy = newy % 50 + starty
                    newx = startx + 50 - 1
                case 2: # left
                    newy = newy % 50 + starty
                    newx = startx
                case 1: # down
                    newy = starty + 50 - 1
                    newx = newx % 50 + startx
                case 3: # up
                    newy = starty
                    newx = newx % 50 + startx
            if board[newy][newx] != '#':
                my_dir = new_dir
            #print(newx, newy, board[newy][newx], my_dir)
        if board[newy][newx] == '#':
            
            break
        current_pos = (newx, newy) 

    match rotate[0]:
        case 'R':
            my_dir = (my_dir + 1) % len(directions)
        case 'L':
            my_dir = (my_dir - 1) % len(directions)
        case 'E':
            # we are done
            pass
    #print(current_pos, directions[my_dir])
    #break
    #print(amount, rotate)

print(1000*(1+current_pos[1]) + 4*(1+current_pos[0]) + my_dir)

# 130195 too low
# 103031 NOT GOOD

#print(path)