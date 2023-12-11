my_input = [list(line.rstrip()) for line in open("input").readlines()]

expand_rows = []
expand_colums = []
expansion_rate = 1000000

for idx, line in enumerate(my_input):
    if not '#' in line:
        expand_rows.append(idx)
 
# rotate to figure out which columns need expansion
rot = [[my_input[i][j] for i in range(len(my_input[0]))] for j in range(len(my_input))]
for idx, col in enumerate(rot):
    if not '#' in col:
        expand_colums.append(idx)

# expand!
# (if needed, but we can be smarter!)
#for row in my_input:
#    for i in reversed(expand_colums):
#        row.insert(i, '.')

#for i in reversed(expand_rows):
#    my_input.insert(i, ['.' for _ in my_input[0]])
    
# debug
#print(expand_rows, expand_colums)
#for line in my_input:
#    [print(i, end='') for i in line]
#    print()
    
galaxies = []
for j, line in enumerate(my_input):
    for i, char in enumerate(line):
        if char == '#':
            galaxies.append((i,j))
      
def min_manhattan(x1,y1,x2,y2):
    return abs(y2-y1) + abs(x2-x1)

distances = []
for g1 in reversed(galaxies):
    for g2 in galaxies:
        if g1 == g2:
            continue
            
        x1,y1 = g1
        x2,y2 = g2    
        
        leftx, rightx = (x1, x2) if x1 < x2 else (x2, x1)
        lefty, righty = (y1, y2) if y1 < y2 else (y2, y1)
        
        total_expansion = [1 if leftx <= p <= rightx else 0 for p in expand_colums]
        total_expansion += [1 if lefty <= p <= righty else 0 for p in expand_rows]
        gravity_gaps_crossed = sum(total_expansion)
        distances.append(min_manhattan(*g1, *g2)+gravity_gaps_crossed*expansion_rate-gravity_gaps_crossed)
    galaxies.remove(g1)
    
print(sum(distances))
