import sys
sys.setrecursionlimit(8000)

extraction = [[i for i in l.rstrip()] for l in open("input").readlines()]
start = (1, 0) # (x, y)
end = (len(extraction[0])-2, len(extraction)-1)

blizzards = []
bliz_movements = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1),
}
boards = [[l.copy() for l in extraction]] # love you python :*

# get initial blizzards and reset board
for j in range(len(extraction)):
    for i in range(len(extraction[0])):
        if extraction[j][i] in bliz_movements:
            blizzards.append(((i, j), extraction[j][i]))
            extraction[j][i] = '.'

def new_board():
    # or maybe just return the board
    tmp_bliz = {k:v for k,v in blizzards}
    new_board = []
    for j in range(len(extraction)):
        tmp_board = []
        for i in range(len(extraction[0])):    
            if (i, j) in tmp_bliz:
                tmp_board.append(tmp_bliz[(i, j)])
            else:
                tmp_board.append(extraction[j][i])
        new_board.append(tmp_board)
    return new_board

# 1 <-> len(extraction) - 2
# (x - a) % (b - a + 1) + a
def tick_blizzards():
    new_blizzards = []
    a, bx, by = 1, len(extraction[0]) - 2, len(extraction) - 2
    for pos, dir_char in blizzards:
        dx, dy = bliz_movements[dir_char]
        x, y = pos
        nx, ny = x+dx, y+dy
        nx, ny = (nx - a) % (bx - a + 1) + a, (ny - a) % (by - a + 1) + a
        new_blizzards.append(((nx, ny), dir_char))
    return new_blizzards

while True:
    blizzards = tick_blizzards()
    board = new_board()
    if board in boards:
        break
    boards.append(board)

def get_neighbours(pos, next_time):
    x,y = pos

    neighbours = []
    deltas = [(0, 0)] + list(bliz_movements.values())

    next_board = boards[next_time]
    for dx, dy in deltas:
        nx, ny = x+dx, y+dy
        if nx >= len(next_board[0]) or ny >= len(next_board) \
            or nx < 0 or ny < 0:
            continue
        if next_board[ny][nx] != '.':
            continue
        neighbours.append((nx, ny))
    return neighbours

def bfs(to_visit, step, my_end):
    if my_end in to_visit:
        return step

    new_to_visit = set()
    next_time = (step+1) % len(boards)
    for pos in to_visit:
        for neighbour in get_neighbours(pos, next_time):
            new_to_visit.add(neighbour)
    
    return bfs(new_to_visit, step+1, my_end)

t1 = bfs(set([start]), 0, end) # part 1
t2 = bfs(set([end]), t1, start)
t3 = bfs(set([start]), t2-1, end)
print(t1, t2, t3)
