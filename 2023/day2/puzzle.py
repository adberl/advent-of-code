import pprint
pp = pprint.PrettyPrinter(indent=4)

my_input = [line.rstrip() for line in open("input").readlines()]

max_draws = {
	"red": 12,
	"green": 13,
	"blue": 14,
}


# parsing
all_games = []
for game in my_input:
	my_game = {}
	game_id, sets = game.split(": ")
	game_id = int(game_id.split(' ')[1])
	my_game["id"] = game_id
	sets = [x.split(", ") for x in sets.split("; ")]
	my_sets = []
	for one_set in sets:
		draws = []
		for draw in one_set:
			amount, color = draw.split(' ')
			draws.append((color, int(amount)))
		my_sets.append(draws)
	my_game["sets"] = my_sets
	all_games.append(my_game)	

#part 1
id_sum = 0
for game in all_games:
	valid_game = True
	for a_set in game["sets"]:
		for color, amount in a_set:
			if not (color in max_draws and max_draws[color] >= amount):
				valid_game = False
						
	if valid_game:
		print(f"Possible game: {game['id']}")
		id_sum += int(game["id"])

print(id_sum)

#part 2
game_powers = 0
for game in all_games:
	mins = {}
	for a_set in game["sets"]:
		for color, amount in a_set:
			if not color in mins:
				mins[color] = amount
			else:
				mins[color] = amount if mins[color] < amount else mins[color]

	game_powers += eval(str(list(mins.values())).replace(', ', '*')[1:-1])

print(game_powers)
#pp.pprint(all_games)
