import re
import numpy as np

lines = open('input.txt', 'r').readlines()

twochars = 0
threechars = 0

for line in lines:

	char_list = np.zeros(26, dtype=int)
	
	for character in line:
		if (character == '\n'):
			continue
		
		char_list[ord(character) - ord('a')] += 1
	
	two_occured = 0
	three_occured = 0
	for char_occured in char_list:
		if (char_occured == 2):
			two_occured = 1
		elif (char_occured == 3):
			three_occured = 1
	twochars += two_occured
	threechars += three_occured

for line in lines:
	for line2 in lines:
		difference = 0
		for i in range(0, len(line)):
			if(difference > 1): break
			if(line[i] != line2[i]):
				difference += 1
		
		if (difference == 1):
			print(line, line2)

print(twochars * threechars)
