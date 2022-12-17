import networkx as nx
import matplotlib.pyplot as plt

cave = [l.rstrip() for l in open("input").readlines()]

valves = []

valve_network = {}
valve_rate = {}
valve_distances = {}

def _get_distance(valve, to_where, cost, visited, solution):
	#print(f'Visiting: {valve} on our journey to {to_where} info: {cost}|{visited}|{solution}')# {visited} {solution}')
	if valve == to_where:
		solution.append((valve, cost))
		#print(f'We got it.')
		return solution
	
	for nvalve in valve_network[valve]:
		if nvalve in visited:
			continue
		solution = _get_distance(nvalve, to_where, cost+1, visited+[nvalve], solution)

	return solution

def get_distances(valve):
	dists = {}
	for to_where in valves:
		if to_where == valve: # can't go to ourselves :D
			dists[valve] = 0
		if to_where in valve_network[valve]:
			dists[to_where] = 1
		else:
			my_distances = _get_distance(valve, to_where, 0, [valve], [])
			min_distance = min(my_distances, key=lambda x: x[1])

			dists[to_where] = min_distance[1]

	#print(dists)
	return dists

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

for valve in valves:
	valve_distances[valve] = get_distances(valve)

#print(valve_network)
#print(valve_rate)
#print(valves)
#print(valve_distances)

def get_total_eventual_pressures(current_valve, current_time, max_time):
	total_pressures_released = []
	time_remaining = max_time - current_time
	for valve in valves:
		time_to_move = valve_distances[current_valve][valve] + 1
		#total_pressures_released[valve] = (time_remaining-time_to_move) * valve_rate[valve]
		total_pressures_released.append((valve, (time_remaining-time_to_move) * valve_rate[valve], time_to_move))

	return total_pressures_released

def cool_heuristics():
	while current_time < max_time:
		print(f'I am currently in {current_valve} at time {current_time}')
		for local_valve, local_score, local_time in sorted(get_total_eventual_pressures(current_valve, current_time, max_time), key=lambda x: x[1], reverse=True):
			if local_valve in opened:
				continue
			else:
				print(f'I have decided to move to {local_valve} and open it which will take {local_time}, increasing total valve pressure released by {local_score}')
				#print(local_valve, local_score, local_time, current_time)
				current_valve = local_valve
				opened.append(current_valve)
				total_score += local_score
				current_time += local_time	
				break
		#print(opened)

def visualize_it():
	edges = []
	for valve in valves:
		for neighbour in valve_network[valve]:
			edges.append([valve, neighbour])
			

	G = nx.Graph()
	G.add_edges_from(edges)
	nx.draw_networkx(G)
	plt.show()


#max_time = 30 # minutes
solution = 0
remaining_to_open = []
def bfs_it(score, current_valve, to_visit, current_time, level, max_time=30):
	global solution
	global remaining_to_open
	#print(f'{" "* level}{level} {current_valve} | {to_visit} | {score} | {current_time}')
	if current_time > max_time or not to_visit:
		if score > solution:
			remaining_to_open = to_visit + [current_valve]
			solution = score
		#solution = max(solution, score)
		return

	time_remaining = max_time - current_time
	score += (time_remaining) * valve_rate[current_valve]		

	for new_valve_to_visit in to_visit:
		time_to_move = valve_distances[current_valve][new_valve_to_visit] + 1

		new_to_visit = [x for x in to_visit if x != new_valve_to_visit]
		bfs_it(score, new_valve_to_visit, new_to_visit, current_time + time_to_move, level+1, max_time)

_to_visit = []
for valve in valves:
	if valve_rate[valve] != 0:
		_to_visit.append(valve)
#bfs_it(0, 'AA', _to_visit, 0, 0) # part 1 here

bfs_it(0, 'AA', _to_visit, 0, 0, 26)
a = solution
solution = 0
bfs_it(0, 'AA', remaining_to_open, 0, 0, 26)
print(a+solution)

# rip output_historical.txt (1.7 million lines ~ 124 MiB)
# forever in our hearts