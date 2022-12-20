import re
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

blueprints_max = [0 for _ in range(len(blueprints))]
max_time = 24
def traverse(bid, blueprint, robots, resources, time):
    #print(f'Currently on turn {time}/{max_time}')
    if time >= max_time:
        #print(bid, resources, robots)
        blueprints_max[bid] = max(blueprints_max[bid], resources['geode'])
        #print(f'We managed to get {resources["geode"]} geodes.')    
        return

    new_blueprint = blueprint.copy()
    max_resources = max_resources_needed(blueprint)
    for robot_name, amount in robots.items():
        if robot_name in max_resources and robot_name in blueprint:
            if amount >= max_resources[robot_name]:
                new_blueprint.pop(robot_name)

    # it is not optimal to skip a turn if we built a robot
    reversed_blueprint = dict(reversed(list(blueprint.items())))
    for robot_name, robot_cost in reversed_blueprint.items():
        if can_afford_robot(robot_cost, resources):
            
            # we branch off and create the robot here
            # meaning we substract robot cost, mine new resources and start a new turn
        
            new_resources = resources.copy()
            for res, amount in robot_cost.items():
                new_resources[res] -= amount

            new_robots = robots.copy()
            if robot_name in new_robots:
                new_robots[robot_name] += 1
            else:
                new_robots[robot_name] = 1

            for robot, amount in robots.items():
                new_resources[robot] += amount

            traverse(bid, new_blueprint, new_robots, new_resources, time+1)

    # if we can can't build a geode or a obsidian robot, its ok to wait
    if not can_afford_robot(blueprint['obsidian'], resources) or\
        not can_afford_robot(blueprint['geode'], resources):
        for robot, amount in robots.items():
            resources[robot] += amount

        traverse(bid, new_blueprint, robots, resources, time+1)

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

print(max_resources_needed(blueprints[0]))
print(blueprints_max)
#print(max_resources_needed(blueprints[0]))
#print(blueprints)