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

max_res_blueprints = []
for blueprint in blueprints:
    max_res_blueprints.append(max_resources_needed(blueprint))

def time_to_build(robot_cost, robots, available_res):
#    print(f'Testing {robot_cost}, {robots}')

    max_turns = 0
    for res, val in robot_cost.items():
        if res not in robots:
            return -1

        resources_i_have = available_res[res]
        resource_robots_i_have = robots[res]

        if resources_i_have > val:
            continue
        else:
            max_turns = max(max_turns, math.ceil((val-resources_i_have)/resource_robots_i_have))
    return max_turns+1

blueprints_max_geodes = [0 for _ in range(len(blueprints))]
max_potentials = [0 for _ in range(len(blueprints))]
caching = [{} for _ in range(len(blueprints))]
max_time = 32
visited_nodes = 0
def traverse(bid, blueprint, robots, resources, time):
    #print(f'{time*"  "}Currently on turn {time}/{max_time}')
    #print(f'{time*"  "} {robots} {resources} {blueprint}')

    global visited_nodes
    visited_nodes += 1
    if time >= max_time:
        blueprints_max_geodes[bid] = max(blueprints_max_geodes[bid], resources['geode'])
        return

    # if we already somehow saw this robot combination before but at an earlier time (somehow)
    # then no point pursuing this
    robots_tuple = tuple(list(robots.values())) #[:-1]) # :-1 is too aggressive 
    if robots_tuple in caching[bid] and caching[bid][robots_tuple] < time:
            return
    caching[bid][robots_tuple] = time

    # remove a robot blueprint if we have no need for it anymore
    new_blueprint = blueprint.copy()
    max_resources = max_res_blueprints[bid] # max_resources_needed(blueprint)
    for robot_name, amount in robots.items():
        if robot_name in max_resources and robot_name in blueprint:
            if amount >= max_resources[robot_name]:
                new_blueprint.pop(robot_name)
    blueprint = new_blueprint

    remaining_time = max_time - time
    max_geodes_with_current_robots = 0
    if 'geode' in robots:
        max_geodes_with_current_robots = resources['geode'] + remaining_time * robots['geode']
    max_geodes_potential = max_geodes_with_current_robots + remaining_time * (remaining_time-1)//2

    if max_geodes_potential < max_potentials[bid]:
        # we have a max potential somewhere else, should likely try that branch
        return
    max_potentials[bid] = max(max_potentials[bid], max_geodes_with_current_robots)

    managed_to_build_robot = False

    # skip from current turn to when we can build that robot
    blueprint_reversed = dict(reversed(list(blueprint.items())))
    for robot_name, robot_cost in blueprint_reversed.items():
        # figure out how many turns we gotta wait to build it
        duration_to_build = time_to_build(robot_cost, robots, resources)
        #print(f'Duration to build {robot_name}: {duration_to_build}')
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

        managed_to_build_robot = True
        traverse(bid, blueprint, new_robots, new_resources, time+duration_to_build)

    if not managed_to_build_robot:
        new_resources = {}
        for res, amount in resources.items():
            if res in robots:
                new_resources[res] = amount + robots[res]*(max_time-time)
            else:
                new_resources[res] = amount
        traverse(bid, blueprint, robots, new_resources, max_time)

# part 1:
for bid, blueprint in enumerate(blueprints):
    resources = {
        'ore': 0,
        'clay': 0,
        'obsidian': 0,
        'geode': 0,
    }
    #print(bid, blueprint)
    traverse(bid, blueprint, {'ore': 1}, resources, 0)

t = 0
for i, b in enumerate(blueprints_max_geodes):
    t += (i+1)*b

print(t)

# part 2:
t = 1
for b in blueprints_max_geodes[:3]:
    t *= b

print(t)


# stats for nerds
print(blueprints_max_geodes)
print(visited_nodes)