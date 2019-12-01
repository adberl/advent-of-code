import re

lines = open('input.txt', 'r').readlines()

start = 0
freq_list = [0]

for line in lines:
	start += int(line)

print("final freq: ", start)

start = 0
found = 0

while True:
	if found: break
	for line in lines:
		start += int(line)
		if start in freq_list:
			print("first freq encountered twice: ", start)
			found = 1
			break
		freq_list.append(start)
