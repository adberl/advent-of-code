import re, math
blueprints_input = [l.rstrip() for l in open("input").readlines()]

blueprints = []
for line in blueprints_input:
    costs = [int(i) for i in re.findall(r'\d+', line)]

    tmp_blueprint = {}
    tmp_blueprint['ore'] = {'ore': costs[1]}
    tmp_blueprint['clay'] = {'ore': costs[2]}
    tmp_blueprint['obsidian'] = {'ore':costs[3], 'clay': costs[4]}
    tmp_blueprint['geode'] = {'ore':costs[5], 'obsidian': costs[6]}

    blueprints.append(tmp_blueprint)

def can_afford_robot(robot, resources):
    #print(f'Testing robot: {robot} and I have {resources}: ', end='')
    for k,v in resources.items():
        if k in robot and robot[k] > v:
            #print(f'Cannot afford robot!!!')
            return False
    #print(f'If it got here, robot is affordable')
    return True

def max_resources_needed(blueprint):
    resources = {
        'ore': 0,
        'clay': 0,
        'obsidian': 0,
    }

    for _, all_costs in blueprint.items():
        for res_name, amount in all_costs.items():
            if res_name not in resources:
                continue
            if amount > resources[res_name]:
                resources[res_name] = amount

    return resources

def time_to_build(robot_cost, robots):
#    print(f'Testing {robot_cost}, {robots}')
    max_turns = 0
    for res, val in robot_cost.items():
        if res not in robots:
            # cannot build this robot ever
            return -1
        
        max_turns = max(max_turns, math.floor(val/robots[res]))
    #print(max_turns)
    return max_turns

blueprints_max = [0 for _ in range(len(blueprints))]
max_potentials = [0 for _ in range(len(blueprints))]
max_time = 24
visited_nodes = 0
caching = {}
def traverse(bid, blueprint, robots, resources, time):
    #print(f'Currently on turn {time}/{max_time}')
    global visited_nodes
    visited_nodes += 1
    if time >= max_time:
        #print(bid, resources, robots)
        blueprints_max[bid] = max(blueprints_max[bid], resources['geode'])
        #print(f'We managed to get {resources["geode"]} geodes.')    
        #print(f'Using these robots: {robots}')
        return

    # if we already somehow saw this robot combination before but at an earlier time (somehow)
    # then no point pursuing this
    robots_tuple = tuple(list(robots.values())) #[:-1]) # :-1 is too aggressive 
    if robots_tuple in caching and caching[robots_tuple] < time:
            return
    caching[robots_tuple] = time

    # remove a robot blueprint if we have no need for it anymore
    new_blueprint = blueprint.copy()
    max_resources = max_resources_needed(blueprint)
    for robot_name, amount in robots.items():
        if robot_name in max_resources and robot_name in blueprint:
            if amount >= max_resources[robot_name]:
                new_blueprint.pop(robot_name)
    blueprint = new_blueprint

    remaining_time = max_time - time

    max_geodes_with_current_robots = 0
    if 'geode' in robots:
        max_geodes_with_current_robots = robots['geode'] + remaining_time * robots['geode']
    max_geodes_potential = max_geodes_with_current_robots + remaining_time * (remaining_time-1)//2

    if max_geodes_potential < max_potentials[bid]:
        # we have a max potential somewhere else, should likely try that branch
        return
    max_potentials[bid] = max_geodes_with_current_robots
    # skip from current turn to when we can build that robot
    blueprint_reversed = dict(reversed(list(blueprint.items())))
    for robot_name, robot_cost in blueprint_reversed.items():
        # figure out how many turns we gotta wait to build it
        duration_to_build = time_to_build(robot_cost, robots)
        if duration_to_build == -1 or duration_to_build + time > max_time:
            # cant build it with the current resource extraction we have
            continue
        
        # can build the robot, let's build it!
        #print(f'Building a {robot_name} which will take {duration_to_build}')
        new_resources = {}
        for res, amount in resources.items():
            if res in robots:
                new_resources[res] = amount + robots[res]*duration_to_build
            else:
                new_resources[res] = amount

        new_robots = robots.copy()
        if robot_name in robots:
            new_robots[robot_name] += 1
        else:
            new_robots[robot_name] = 1

        for res, val in robot_cost.items():
            new_resources[res] -= val

        traverse(bid, blueprint, new_robots, new_resources, time+duration_to_build)


for bid, blueprint in enumerate(blueprints):
    resources = {
        'ore': 0,
        'clay': 0,
        'obsidian': 0,
        'geode': 0,
    }
    #print(bid, blueprint)
    traverse(bid, blueprint, {'ore': 1}, resources, 0)

    #can_afford_robot(blueprint['ore'], resources)

print(blueprints_max)
print(visited_nodes)
#print(max_resources_needed(blueprints[0]))
#print(blueprints)