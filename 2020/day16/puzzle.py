with open('input', 'r') as f:
	lines = [i.strip() for i in f.readlines()]

ranges = set()
badnumbers = []
fields = {}
good_tickets = []

def process_data():
	part = 1
	for line in lines:
		if(line == ''):
			part += 1
			continue
		elif(part == 1): #part1
			name, goodpart = line.split(': ')
			range1, range2 = goodpart.split(' or ')
			start1, end1 = range1.split('-')
			start2, end2 = range2.split('-')
			range1 = set(range(int(start1), int(end1)+1))
			range2 = set(range(int(start2), int(end2)+1))
			ranges.update(range1 | range2)
			fields[name] = range1 | range2
		elif(part == 2): #part2 (this is my ticket)
			if('ticket' in line):
				continue
			numbers = [int(i) for i in line.split(',')]
			good_tickets.append(numbers)
		elif(part == 3):
			if('ticket' in line):
				continue
			numbers = [int(i) for i in line.split(',')]
			bad_ticket = False
			for num in numbers:
				if not num in ranges:
					badnumbers.append(num)
					bad_ticket = True
			if not bad_ticket:
				good_tickets.append(numbers)
		else:
			break

process_data()

ticket_len = len(good_tickets[0])
potential_fields = {}
print(f'Part 1: {sum(badnumbers)}')

for i in range(ticket_len):
	potential_fields[i] = []

for i in range(ticket_len):
	for field in fields:
		good_ticket_field = True
		for ticket in good_tickets:
#			print(f'checking {ticket[i]} if is in {field}')
			if not ticket[i] in fields[field]:
#				print(f'{ticket[i]} is not in {field}')
				good_ticket_field = False
				break
		if good_ticket_field:
#			print(f'[i] might be a {field}')
			potential_fields[i].append(field)

while True:
	modified = False
	for field in potential_fields:
		if len(potential_fields[field]) == 1:
			already_unique = potential_fields[field][0]
			for field2 in potential_fields:
				if already_unique in potential_fields[field2] and field != field2:
					potential_fields[field2].remove(already_unique)
					modified = True
	if not modified:
		break

total = 1
for field in potential_fields:
	if 'departure' in potential_fields[field][0]:
		total *= good_tickets[0][field]
print(f'Part 2: {total}')
