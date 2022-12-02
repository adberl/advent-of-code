input = [line.rstrip() for line in open("input").readlines()]

transform = lambda x: chr(ord(x) - 23) # shift XYZ -> ABC
transform_proper = lambda x,y: (ord(x) - 65 + ((ord(y) - 89) % 3)) % 3

def calculate_outcome(enemy, me):
    #new_me = transform(me) # part 1
    new_me = chr(transform_proper(me, enemy) + 65) # part 2   
    winnings = abs((1 + ord(new_me) - ord(enemy)) % 3) * 3
    choice = ord(new_me)-64
    print(enemy, me, new_me)
    return winnings + choice 
    
def part2(enemy, me):
    pass
    
total_score = 0
for l in input:
    battle = l.split(' ')
    total_score += calculate_outcome(battle[0], battle[1])
    
print(total_score)
