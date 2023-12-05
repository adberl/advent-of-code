my_input = [line.rstrip() for line in open("input").readlines()]

current_seeds = []
all_maps = []
current_map = []

for idx, line in enumerate(my_input):
    if idx == 0:
        current_seeds = [int(x) for x in line.split(": ")[1].split(' ')]     
        continue

    if "map" in line:
        current_map = []
        continue
    
    if line == '':
        if current_map != []:
            all_maps.append(current_map)
        continue

    current_map += [[int(x) for x in line.split(' ')]]

# ranges are inclusive on both sides
seed_ranges = []
for i in range(0, len(current_seeds), 2):
    seed_ranges.append((current_seeds[i], current_seeds[i] + current_seeds[i+1] - 1))

#part 1
for mappings in all_maps:
    for i in range(len(current_seeds)):
        for dest, src, arange in mappings:
            delta = dest-src
            if src <= current_seeds[i] <= src+arange:
#                print(f"Transforming {current_seeds[i]} into {current_seeds[i]+delta}")
                current_seeds[i] += delta
                break
   
print(min(current_seeds))

# test for part 2
big_seeds = []
for a, b in seed_ranges:
    big_seeds += range(a, b+1)
    
for mappings in all_maps:
    for i in range(len(big_seeds)):
        for dest, src, arange in mappings:
            delta = dest-src
            if src <= big_seeds[i] <= src+arange:
#                print(f"Transforming {current_seeds[i]} into {current_seeds[i]+delta}")
                big_seeds[i] += delta
                break
 #   print(sorted(big_seeds))
#print(big_seeds)
#part 2
print(f"BIG START: ", seed_ranges)
for mappings in all_maps:
    i = 0
    while i < len(seed_ranges):
        changed = False
        for dest, src, arange in mappings:
            delta = dest-src 
            if i >= len(seed_ranges):
                break
            print(f"Starting {i}", seed_ranges)
            start, end = seed_ranges[i]
        
            # simplest case, the entire range can be mapped
            if src <= start <= src+arange and src <= end <= src+arange:
                print("entire", delta, start, end, src, dest)
                seed_ranges[i] = (start+delta, end+delta)
                i += 1
                changed = True
                
            # if range is includes start
            elif src <= start <= src+arange and not (src <= end <= src+arange):
                # figure out how many seeds are contained in the range
                contained = (src+arange) - start
                print("start", contained, delta, start, end, src, dest)
                print("two new: ", (start+delta, start+delta+contained), (start+contained+1, end))
                seed_ranges[i] = (start+delta, start+delta+contained)
                seed_ranges.insert(i+1, (start+contained+1, end))
                print(seed_ranges)
                i += 1
                changed = True
            
            # if range includes end
            elif not (src <= start <= src+arange) and src <= end <= src+arange:
                contained = end - src
                print("end", contained, delta, start, end, src, dest, arange)
                print("two new: ", (src+delta, end+delta), (start, src-1))
                seed_ranges.insert(i+1, (start, src-1))
                seed_ranges[i] = (src+delta, end+delta)
                print(seed_ranges)
                i += 1
                changed = True
            
            # if mapping range entirely contained
            elif start <= src and src+arange <= end:
                print("mid", delta, start, end, src, dest)
                seed_ranges[i] = (start, src-1)
                seed_ranges.insert(i+2, (src, src+arange)) 
                seed_ranges.insert(i+1, (src+arange+1, end))
                i += 2
                changed = True
        
        if not changed:
            i += 1
        #print(seed_ranges)
        #i += 1
    print('Seed ranges after mapping: ', seed_ranges)
    print(mappings)
    print()

print(seed_ranges)
