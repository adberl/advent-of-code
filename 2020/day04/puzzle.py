import re

f = open('input', 'r').readlines()

passports = []
current_passport = {}
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']#, 'cid']
valid = 0

def validate(passport):
	print(' ------------ new passport ------------- ')
	print(passport)
	ret = False
	for key in passport:
		value = passport[key]
		if(key == 'byr'):
			ret = yearcheck(value, 1920, 2002)
		elif(key == 'iyr'):
			ret = yearcheck(value, 2010, 2020)
		elif(key == 'eyr'):
			ret = yearcheck(value, 2020, 2030)
		elif(key == 'hgt'):
			lasttwo = value[-2:]
			if(lasttwo == 'cm'):
				ret = is_in_interval(value[:-2], 150, 193)
			elif(lasttwo == 'in'):
				ret = is_in_interval(value[:-2], 59, 76)
			else: 
				ret = False
		elif(key == 'hcl'):
			if(value[0] != '#'):
				ret = False
			#if(not re.match('[a-f0-9]{6}', value[1:])):
			ret = not re.match('[a-f0-9]{6}', value[1:]) == None
		elif(key == 'ecl'):
			ret = False
			for col in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				if(value == col):
					ret = True			
		elif(key == 'pid'):
			ret = len(value) == 9 and value.isnumeric()
		elif(key == 'cid'):
			ret = True
		else:
			print(f'WE HIT AN ELSE???? {key} {value}')
			ret = False
		if ret == False:
			print(f'validated {key} with {value} and {ret}')
			return False
	print(f'validated {key} with {value} and {ret}')
	return ret
	
def yearcheck(year, least, most):
	if( len(year) != 4):
		return False
	return is_in_interval(year, least, most)

def is_in_interval(number, least, most):
	if(int(number) < least or int(number) > most):
		print(number, least, most)
		return False
	return True

for line in f:
	if line == '\n':
		passports.append(current_passport)

		has_all = validate(current_passport)

		for one in fields:
			if(not one in current_passport):
				has_all = False
		
		if has_all:
			valid += 1

		current_passport = {}
		continue

	line = line.split(' ')
	for entry in line:
		field, value = entry.split(':')
		value = value.strip()
		current_passport[field] = value

print(f'Valid passports: {valid}')
