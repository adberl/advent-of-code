my_input = [[int(x) for x in line.rstrip().split(' ')] for line in open("input").readlines()]

def is_safe(some_report):
    inc = some_report[0] < some_report[1]
    dec = some_report[0] > some_report[1]
    
    cond1 = lambda x,y,z: x > y and z
    cond2 = lambda x,y,z: x < y and z
    cond3 = lambda x,y: 1 <= abs(x-y) <= 3
    
    for i in range(0, len(some_report)-1):
        n0 = some_report[i]
        n1 = some_report[i+1]
        if cond1(n0, n1, inc) or \
            cond2(n0, n1, dec) or \
            not cond3(n0, n1):
            return False
    return True

safe1 = 0
safe2 = 0
for report in my_input:
    if is_safe(report):
        safe1 += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                safe2 += 1
                break
                
print('part 1: ', safe1)
print('part 2: ', safe1+safe2)

