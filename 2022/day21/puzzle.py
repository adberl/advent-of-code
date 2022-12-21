monkeys_input = [l.rstrip().split(': ') for l in open("input").readlines()]

monkeys = {}
for left, right in monkeys_input:
    if right.isnumeric():
        monkeys[left] = int(right)
    else:
        monkeys[left] = tuple(right.split(' '))

def branch_contains_human(name):
    if name == 'humn':
        return True
    
    if isinstance(monkeys[name], int):
        return False
    else:
        left, op, right = monkeys[name]
        return branch_contains_human(left) or branch_contains_human(right)

def get_human_value(branch, value):
    if branch == 'humn':
        return value

    left, op, right = monkeys[branch]

    left_human = branch_contains_human(left)
    human_branch = left if left_human else right
    other_branch = right if left_human else left

    res = resolve(other_branch)
    if op == '+':
        return get_human_value(human_branch, value - res)
    elif op == '*':
        return get_human_value(human_branch, value // res)
    elif op == '-':
        if left_human:
            return get_human_value(human_branch, value + res)
        else:
            return get_human_value(human_branch, res - value)
    elif op == '/':
        if left_human:
            return get_human_value(human_branch, value * res)
        else:
            return get_human_value(human_branch, res // value)

# (4 + (2 * (humn - 3)) / 4 = 150 
# 4 + 2 * (humn - 3) = 150 * 4 = 600
# 2 * (humn - 3) = 600 - 4 = 596
# humn - 3 = 596 / 2 = 298
# humn = 298 + 3 = 301   

def resolve(name):
    if not name in monkeys:
        print('ERROR ERROR ERROR')
        
    if isinstance(monkeys[name], int):
        return monkeys[name]
    else:
        left, op, right = monkeys[name]

        if name == 'root': # comment out this if for part 1
            if(branch_contains_human(left)):
                return get_human_value(left, resolve(right))
            else:
                return get_human_value(right, resolve(left))

        if op == '+':
            return resolve(left) + resolve(right)
        elif op == '*':
            return resolve(left) * resolve(right)
        elif op == '-':
            return resolve(left) - resolve(right)
        elif op == '/':
            return resolve(left) // resolve(right)

print(resolve('root'))


