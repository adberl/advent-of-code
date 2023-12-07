from functools import cmp_to_key

my_input = [line.rstrip() for line in open("input").readlines()]

#card_str = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"] # part 1
card_str = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"] # part 2
part2 = True

handranks = {}
handbids = {}
hands = []

def handrank(hand):
	if hand in handranks:
		return handranks[hand]
	
	hand_set = {}
	for char in hand:
		if char in hand_set:
			hand_set[char] += 1
		else:
			hand_set[char] = 1	

	someret = 0
	jokers = hand_set['J'] if 'J' in hand_set else 0
	if part2 and jokers > 0:
		del hand_set['J']
		hand_type = sorted(list(hand_set.values()))
		if len(hand_type) == 1:
			someret = 6
		
		if len(hand_type) == 2: 
			if jokers == 1:
				if 3 in hand_type:
					someret = 5
				else:
					someret = 4
			elif jokers >= 2:
					someret = 5

		if len(hand_type) == 3:
			someret = 3

		if len(hand_type) == 4:
			someret = 1
		
		if jokers == 5:
			someret = 6

	else:
		hand_type = sorted(list(hand_set.values()))

		# all cards are the same
		if len(hand_type) == 1:
			handranks[hand] = 6
			return 6
		
		# 4 cards same or full house
		if len(hand_type) == 2:
			if 4 in hand_type:
				someret = 5 # four of a kind
			else:
				someret = 4 # full house 2-3 
		
		# either 1 1 3 or 1 2 2 (three of a kind or two pairs)
		if len(hand_type) == 3:
			if 3 in hand_type:
				# three of a kind
				someret = 3
			else:
				# two pairs
				someret = 2
		
		# one pair
		if len(hand_type) == 4:
				someret = 1

		# high card
		if len(hand_type) == 5:
			someret = 0

	handranks[hand] = someret
	return someret

def handsorter(left, right):
	lr, rr = handrank(left), handrank(right)
	if lr == rr:
		for i in range(len(left)):
			if left[i] != right[i]:
				return -1 if card_str.index(left[i]) < card_str.index(right[i]) else 1
		return 0
	else:
		return -1 if lr < rr else 1

for line in my_input:
	cards, bid = line.split(" ")
	handbids[cards] = int(bid)
	hands.append(cards)

hands = sorted(hands, key=cmp_to_key(handsorter))

total_winnings = 0
for idx, hand in enumerate(hands):
	total_winnings += (idx+1) * handbids[hand]

print(total_winnings)
