input = [line.rstrip() for line in open("input").readlines()]


elves = []
tsum = 0
for line in input:
    if line == '':
       elves.append(tsum)
       tsum = 0
       continue
    tsum += int(line)
    
    
print(max(elves))
print(sum(sorted(elves)[-3:]))
