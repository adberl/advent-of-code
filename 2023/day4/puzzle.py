my_input = [line.rstrip() for line in open("input").readlines()]

total_points = 0
total_cards = [1 for _ in range(len(my_input))]
for idx, game in enumerate(my_input):
    _, numbers = game.split(": ")
    winning, haves = [set([int(y) for y in x.split(' ') if y != ''])\
                        for x in numbers.split(" | ")]
    
    actual_winnings = len(haves.intersection(winning))
    if(actual_winnings > 0):
        total_points += 2**(len(haves.intersection(winning))-1)

    for i in range(actual_winnings):
        total_cards[idx+i+1] += total_cards[idx]

print("part one: ", total_points)
print("part two: ", sum(total_cards))
