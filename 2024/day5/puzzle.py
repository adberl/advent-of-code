pages = [line.rstrip('\n') for line in open("input").readlines()]

# extra processing
rules = {}
updates = []
is_rules = True
for line in pages:
    if not line:
        is_rules = False
        continue

    if is_rules:
        a, b = (int(x) for x in line.split('|'))
        if a in rules:
            rules[a].append(b)
        else:
            rules[a] = [b]
    else:
        update = [int(x) for x in line.split(',')]
        updates.append(update)

def is_good_update(my_update):
    good_update = True 
    for a, b in rules.items():
        if a in my_update:
            for idb in b:
                if not idb in my_update:
                    continue
                #print(f'Testing rule: {a}|{b} for {my_update}')
                if my_update.index(a) > my_update.index(idb):
                    #print(f'Rule broken: {a}|{b} for {my_update}')
                    good_update = False
                    break
    return good_update                

# find bad and good rules
good_updates = []
fix_updates = []
for update in updates:
    good_update = is_good_update(update)

    if good_update:
        good_updates.append(update)
    else:
        fix_updates.append(update)

# part 1      
total = 0
for updt in good_updates:
    total += updt[len(updt)//2]
print(total)

# part 2
def fun_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        
        a = arr[n]

        # needs to be swapped
        if a in rules:
            # find the left-most we should swap with
            smallest = n # a index
            for b in rules[a]:
                if b not in arr:
                    # not all rules might be applicable
                    continue 
                smallest = min(arr.index(b), smallest)
                
            arr[n], arr[smallest] = arr[smallest], arr[n]
            swapped = True    
            
        if not swapped:
            break
                
for bad_update in fix_updates:
    while not is_good_update(bad_update):
        fun_sort(bad_update)

total2 = 0
for updt in fix_updates:
    total2 += updt[len(updt)//2]
print(total2)
