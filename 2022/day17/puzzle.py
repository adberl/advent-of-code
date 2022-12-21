jets = open("input").readlines()[0] #l.rstrip() for l in open("input").readlines()

tetrominos = [
    ['####'], # line
    ['.#.', '###', '.#.'], # plus
    ['..#', '..#', '###'], # l
    ['#', '#', '#', '#'], # rare line
    ['##', '##'], # box
]

new_row = '|.......|'
board = ['+-------+', '|.......|', '|.......|', '|.......|', '|.......|']

def collides(rock, board):
    #print(f'Comparing {rock} to {board}')
    for i, r in enumerate(rock):
        if r == '#':
            if board[i] == '|' or board [i] == '#' or board[i] == '-':
                return True
    return False

def print_board(b):
    for line in list(reversed(b)):
        print(line)

def print_dummy_board(b, rock, current_row):
    dummy_board = b.copy()
    for i in range(len(rock)): 
        local_row = current_row + i
        rock_row = list(reversed(rock))[i]
        board_row = dummy_board[local_row]             
        dummy_board[local_row] = board_row[:current_column+1] + rock_row + board_row[1 + current_column + len(rock_row):]
    print_board(dummy_board)
    print()



placed_rocks = 0
current_top = 1 # 0th element is the floor :)
jetid = 0
ROCK_LIMIT = 2022
while placed_rocks < ROCK_LIMIT:
    for rock in tetrominos:
        #print(f'Currently working on {rock}')

        if placed_rocks >= ROCK_LIMIT:
            break

        stopped = False
        current_row = current_top+3

        # let's see if we need to add anything to the board!
        if current_row+len(rock) >= len(board):
            extra_size = current_row - len(board) + len(rock)
            board += [new_row for _ in range(extra_size)]

        # left edge is two units from the wall
        # means we start on id=3 
        current_column = 2

        #print_dummy_board(board, rock, current_row)

        while not stopped:

            jet = jets[jetid]
            direction = 1 if jet == '>' else -1

            # sideways movement
            can_move_sideways = True
            #print(f'Sideways verification: ')
            for i in range(len(rock)):
                rock_row = list(reversed(rock))[i]
                local_row = current_row + i

                board_row = board[local_row][1+current_column+direction:]
                if collides(rock_row, board_row):
                    can_move_sideways = False
            
            if can_move_sideways:
                current_column += direction

            # down movement
            can_move_down = True
            #print(f'Downwards verification: ')
            for i in range(len(rock)):
                rock_row = list(reversed(rock))[i]
                local_row = current_row + i - 1

                board_row = board[local_row][1+current_column:]
                if collides(rock_row, board_row):
                    can_move_down = False
                        

            if not can_move_down: # add it to board here
                for i in range(len(rock)): 
                    local_row = current_row + i
                    rock_row = list(reversed(rock))[i]
                    board_row = board[local_row]
                    # 1+current_column:
                    new_rock_row = ''
                    for i in range(len(rock_row)):
                        if rock_row[i] == '#':
                            new_rock_row += '#'
                        else:
                            new_rock_row += board_row[current_column+i+1]

                    board[local_row] = board_row[:current_column+1] + new_rock_row + board_row[1 + current_column + len(rock_row):]
                placed_rocks += 1
                stopped = True
            else:
                # move down
                current_row -= 1
                #print_dummy_board(board, rock, current_row)

            # dummy board after ever movement
            #print_dummy_board(board, rock, current_row)
            jetid = (jetid + 1) % len(jets)
        
        # after a tetromino stopped, increase all the relevant row values
        #print(f'current row is {current_row}')
        current_top = max(current_top, current_row + len(rock))
        
        #print_dummy_board(board, rock, current_row)


# 3178 is too low
# 3179 is too low
# 3204 is too low
# 3206
print_board(board)
for i in range(len(board)-1, 0, -1):
    if '#' in board[i]:
        print(i)
        break

#print(placed_rocks, current_top)