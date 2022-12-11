monkys = [l.rstrip() for l in open("input").readlines()]
monkeys = []

class Monkey():
	def __init__(self, items, operation, test, true, false):
		self.items = items
		self.operation = operation
		self.test = test
		self.true = true
		self.false = false
		self.inspections = 0

	def catch_item(self, item):
		self.items.append(item)

	def __str__(self):
		return f'\nitems: {self.items}\n op: {self.operation}\n test: {self.test}\n true: {self.true}\n false: {self.false}\n inspections: {self.inspections}'

	def __repr__(self):
		return self.__str__()

	def inspect_item(self):
		self.inspections += 1
		worry = self.items.pop(0)
		
		op = lambda old : eval(self.operation) # evil function use
		worry = op(worry)
		worry = worry % (5*11*2*13*7*3*17*19)

		if worry % self.test == 0: # true
			return self.true, worry
		else: # false
			return self.false, worry

def parse_input():

	items = []
	operation = test = true = false = None
	currentop = 0
	monkyno = -1

	for line in monkys:
		#print(line, currentop)
		if currentop == 0:
			monkyno += 1
		elif currentop == 1:
			items = [int(i) for i in line.split(': ')[1].split(', ')]
		elif currentop == 2:
			operation = line.split(' new = ')[1]
		elif currentop == 3:
			test = int(line.split(' by ')[1])
		elif currentop == 4:
			true = int(line.split(' monkey ')[1])
		elif currentop == 5:
			false = int(line.split(' monkey ')[1])
		else: # empty line, reset monky
			newmonky = Monkey(items, operation, test, true, false)
			monkeys.append(newmonky)

			items = []
			operation = test = true = false = None

		currentop = (currentop + 1) % 7

parse_input()
MAX_ROUNDS = 10000

for i in range(MAX_ROUNDS):
	print(f'round {i+1}/{MAX_ROUNDS}')
	for monky in monkeys:
		for _ in range(len(monky.items)):
			newmonky, newworry = monky.inspect_item()
			monkeys[newmonky].catch_item(newworry)

monkey_business = sorted([monkey.inspections for monkey in monkeys])

print(monkeys)
print(monkey_business[-1]*monkey_business[-2])