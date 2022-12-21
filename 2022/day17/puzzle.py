jets = [l.rstrip() for l in open("input").readlines()][0]


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
    print(f'checking {rock} against {board}')
    for i, r in enumerate(rock):
        if r == '#':
            if board[i] == '|' or board [i] == '#' or board[i] == '-':
                return True
    return False

def print_board(b):
    for line in list(reversed(b)):
        print(line)

placed_rocks = 0
current_top = 1 # 0th element is the floor :)
jetid = 0
while placed_rocks <= 2022:
    for rock in tetrominos:
        print(f'Currently working on {rock}')
        stopped = False
        current_row = current_top+3
        # left edge is two units from the wall
        # means we start on id=3 
        current_column = 3
        while not stopped:
            sideways_ok = True
            jet = jets[jetid]
            print(jet, jetid)
            direction = 1 if jet == '>' else -1
            #try moving down
            for i in range(len(rock)):
                rock_row = list(reversed(rock))[i]
                local_row = current_row + i
                if local_row >= len(board):
                    # we are still in limbo so its ok
                    continue
                board_row = board[local_row][current_column+direction:]
                if collides(rock_row, board_row):
                    sideways_ok = False
            
            if sideways_ok:
                current_column += direction
                #for i in range(len(rock)):
                # shift it right or left
                #    local_row = current_row + i
                #    rock_row = list(reversed(rock))[i]
                #    board_row = board[local_row]             
                #    board[local_row] = board_row[:current_column+1] + rock_row + board_row[1 + current_column + len(rock_row):]

            #try moving down
            can_move_down = True

            for i in range(len(rock)):
                rock_row = list(reversed(rock))[i]
                local_row = current_row + i - 1
                if local_row >= len(board):
                    # we are still in limbo so its ok
                    continue
                board_row = board[local_row][current_column:]
                if collides(rock_row, board_row):
                    can_move_down = False
                        

            if not can_move_down: # add it to board here
                for i in range(len(rock)): 
                    local_row = current_row + i
                    rock_row = list(reversed(rock))[i]
                    board_row = board[local_row]             
                    board[local_row] = board_row[:current_column+1] + rock_row + board_row[1 + current_column + len(rock_row):]
                placed_rocks += 1
                stopped = True
            else:
                current_row -= 1
                #for i in range(len(rock)):
                # move down
                #    local_row = current_row + i - 1
                #    rock_row = list(reversed(rock))[i]
                #    board_row = board[local_row]             
                #    board[local_row] = board_row[:current_column+1] + rock_row + board_row[1 + current_column + len(rock_row):]

            # dummy board to print after each move
            dummy_board = board.copy()
            for i in range(len(rock)): 
                local_row = current_row + i
                rock_row = list(reversed(rock))[i]
                board_row = dummy_board[local_row]             
                dummy_board[local_row] = board_row[:current_column+1] + rock_row + board_row[1 + current_column + len(rock_row):]
            print("DUMMY BOARD:")
            print_board(dummy_board)
            jetid = (jetid + 1) % len(jets) 
            #break
    break