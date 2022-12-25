import re

board = [l.rstrip() for l in open("input").readlines()]
path = re.findall(r'\d+[LR]*', board[-1])
path[-1] = path[-1] + 'E' # UGLYYYYYY
max_line_len = len(max(board, key=len))
board = board[:-2]

for i, line in enumerate(board):
    newline = line.replace(' ', '~') + '~' * (max_line_len-len(line))
    board[i] = newline
    #print(newline)

my_dir = 0 # 
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

current_pos = (board[0].find('.'),0)

def add_tuples(t1, t2):
    return tuple([sum(tup) for tup in zip(t1, t2)])

for move in path:
    xmove, ymove = directions[my_dir]
    amount, *rotate = int(move[:-1]), move[-1]

    for m in range(amount):
        newx = (current_pos[0] + xmove) % len(board[0])
        newy = (current_pos[1] + ymove) % len(board)

        #print(f'Trying to move to: {board[newy][newx]}')
        if board[newy][newx] == '~':
            match my_dir:
                case 0:
                    newx = re.search(r'[^~]', board[newy]).start()
                case 1:
                    for i, l in enumerate(board):
                        if l[newx] != '~':
                            break
                    newy = i   
                case 2:
                    g = re.search(r'[^~]', ''.join(list(reversed(board[newy])))).start()
                    newx = max_line_len - g - 1
                case 3:
                    for i, l in enumerate(reversed(board)):
                        if l[newx] != '~':
                            break     
                    newy = len(board) - i - 1
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
    #print(current_pos, my_dir)
    #break
    #print(amount, rotate)

print(1000*(1+current_pos[1]) + 4*(1+current_pos[0]) + my_dir)
# 40480 too high

#print(path)