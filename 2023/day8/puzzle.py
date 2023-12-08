import re
from math import lcm

my_input = [line.rstrip() for line in open("input").readlines()]

mapping = {}
starting_nodes = []
paths = []
directions = my_input.pop(0)

# parsing
rule = re.compile("([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)")
for line in my_input:
    matches = rule.match(line)
    base, left, right = matches.group(1), matches.group(2), matches.group(3)
    mapping[base] = (left, right)
    if base[2] == 'A':
        starting_nodes.append(base)
        paths.append([base])
 
def node_ends_in(node, char):
    if node[2] != char:
        return False
    return True

def get_dir(pos):
    return directions[pos%len(directions)]

# overengineered part 2 that doesn't even work (yet)
# tries to solve the general case where len(A->Z) != len(Z->Z') 
class NodeInfo:

    def __init__(self, some_node):
        self.node = some_node
        self.path = [some_node]
        self.steps_to_repeat = 0
        self.repeat_start = ''    
        self.ends_on_z = False
        
node_info = []
for node in starting_nodes:
    i = 0
    current_node = node
    info = NodeInfo((node, get_dir(i)))
    while True:
        d = get_dir(i)
        next_node = mapping[current_node][0 if d == 'L' else 1]
        next_node_d = (next_node, get_dir(i+1))
        if next_node_d in info.path: # starts repeating
            info.steps_to_repeat = i
            info.repeat_start = next_node_d
            info.ends_on_z = node_ends_in(next_node, 'Z')
            break
        info.path.append(next_node_d)
        current_node = next_node
        i += 1
    node_info.append(info)

# part 2
steps_to_z = []
for node in starting_nodes:
    i = 0
    current_node = node
    while True:
        d = get_dir(i)
        current_node = mapping[current_node][0 if d == 'L' else 1]
        if node_ends_in(current_node, 'Z'):
            steps_to_z.append(i+1)
            break
        i += 1
print(steps_to_z)
print(lcm(*steps_to_z))

# part 1
#current_pos = 'AAA'
#while current_pos != 'ZZZ':
#    direction = directions[i%len(directions)]
#    if direction == 'L':
#        current_pos = mapping[current_pos][0]
#    elif direction == 'R':
#        current_pos = mapping[current_pos][1]
#    i += 1 
#print(i)
