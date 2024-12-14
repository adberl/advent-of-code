rocks = [[int(x) for x in line.rstrip('\n').split(' ')] for line in open("input").readlines()][0]

cache = {}
mapping = {}

def add_to_cache(which, what):
	if what in which:
		which[what] += 1
	else:
		which[what] = 1

def rule_it_out(number):
	if number == 0:
		return [1]
	
	nrstr = str(number)
	if len(nrstr) % 2 == 0:
		half = len(nrstr)//2
		return [int(nrstr[:half]), int(nrstr[half:])]
	
	return [number*2024]


for rock in rocks:
	add_to_cache(cache, rock)

blinks = 75
for i in range(blinks):
	print(f'blink {i+1}/{blinks}')
	
	new_cache = {}
	
	for rock, amount in cache.items():
		if not rock in mapping:
			mapping[rock] = rule_it_out(rock)
			
		for new_rock in mapping[rock]:
			if new_rock in new_cache:
				new_cache[new_rock] += amount
			else:
				new_cache[new_rock] = amount
	cache = new_cache
				
#print(cache)
total = 0
for _, amount in cache.items():
	total += amount
	
print(total)
		