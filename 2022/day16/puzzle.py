cave = [l.rstrip() for l in open("input").readlines()]

valves = []

valve_network = {}
valve_rate = {}
valve_distances = {}

def _get_distance(valve, to_where, cost, visited, solution):
	print(f'Visiting: {valve} on our journey to {to_where} info: {cost}|{visited}')# {visited} {solution}')
	if valve == to_where:
		solution.append(valve)
		print('We got it.')
		return solution
	
	if valve in visited:
		return []
	visited.append(valve)
	
	for nvalve in valve_network[valve]:
		if nvalve in visited:
			continue
		solution += _get_distance(nvalve, to_where, cost+1, visited, solution)

	return solution

def get_distances(valve):
	dists = []
	for to_where in valves:
		if to_where == valve: # can't go to ourselves :D
			continue
		if to_where in valve_network[valve]:
			dists.append((to_where, 1)) # trivial, it's 1 step away
		else:
			dists.append(_get_distance(valve, to_where, 0, [], []))
	valve_distances[valve] = dists

for line in cave:
	valve, rest = line.split(' has flow ')
	valve = valve.split('Valve ')[1]
	
	rate, network = rest.split(';')
	rate = int(rate.split('rate=')[1])

	network = network.split('valve')[1].replace('s ', '').replace(' ', '')
	network = network.split(',')

	valve_network[valve] = network
	valve_rate[valve] = rate
	valves.append(valve)

get_distances("AA")

#print(valve_network)
#print(valve_rate)
#print(valves)
#print(valve_distances)


# at each step, calculate what's the max output
# a valve could provide, considering our current
# position and the time it has already passed