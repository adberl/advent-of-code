
def partone():
	good_password = 0
	
	f = open('input', 'r').readlines()
	for line in f:
		policy, password = line.strip().split(':')
		
		nr, letter = policy.split(' ')
		minn, maxn = nr.split('-')
	
		count = password.count(letter)
		
		if count >= int(minn) and count <= int(maxn):
			good_password +=1
		
	print(good_password)

def parttwo():
	good_password = 0
	
	f = open('input', 'r').readlines()
	for line in f:
		policy, password = line.strip().split(':')
		
		nr, letter = policy.split(' ')
		minn, maxn = nr.split('-')
		password = password.lstrip()
		
		left = password[int(minn) - 1] == letter 
		right = password[int(maxn) - 1] == letter

		if left ^ right:
			good_password +=1
		
	print(good_password)

parttwo()

