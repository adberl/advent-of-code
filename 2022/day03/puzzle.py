pinput = [line.rstrip() for line in open("input").readlines()]

def get_priority(letter):
    if ord(letter) < ord('a'):
        return ord(letter) - ord('A') + 27
    return ord(letter) - ord('a') + 1
        
def part1():
    priorities = 0
    for rucksack in pinput:
        l = len(rucksack)
        comp1 = set(rucksack[0:l//2])
        comp2 = set(rucksack[l//2:l])
        item_in_both = comp1.intersection(comp2).pop()
        priorities += get_priority(item_in_both)       
    print(priorities)
    
def part2():
    priorities = 0   
    for r1,r2,r3 in zip(*[iter(pinput)]*3):
        new_r = set(r1).intersection(set(r2)).intersection(set(r3))
        priorities += get_priority(new_r.pop())
    print(priorities)

part1()
part2()
