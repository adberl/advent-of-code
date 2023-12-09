my_input = [[int(y) for y in line.rstrip().split(' ')] for line in open("input").readlines()]

part2 = True

def all_zeros(array):
    for num in array:
        if num != 0:
            return False
    return True

total = 0
for line in my_input:
    values = [line]
    if part2:
        values = [list(reversed(line))]
        
    while not all_zeros(values[-1]):
        new_values = []
        current_values = values[-1]
        for i in range(len(current_values)-1):
            new_values.append(current_values[i+1] - current_values[i])
        values.append(new_values)
#    print(values)
        
    previous = 0
    for l in reversed(values):
        previous += l[-1]
    total += previous
    #print(previous)

print(total)
