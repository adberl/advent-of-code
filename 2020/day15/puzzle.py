with open('input', 'r') as f:
	numbers = [i.strip().split(',') for i in f.readlines()]

nums = {}
for i, e in enumerate(numbers[0]):
	nums[int(e)] = [i + 1]

last_spoken = len(nums)
last_number = int(numbers[0][-1])
newlast = -1
#print(nums, last_spoken, last_number)
while True:
	if last_spoken == 30000000:
		print(last_number)
		break
	if(len(nums[last_number]) == 1): # it has just been added
		last_spoken += 1
		last_number = 0
		if(len(nums[last_number]) == 2):
			newl = [nums[last_number][-1]]
			newl.append(last_spoken)
			nums[last_number] = newl
		else:
			nums[last_number].append(last_spoken)
	else: # already added
		newnum = nums[last_number][-1] - nums[last_number][0]
		last_spoken += 1
		last_number = newnum
		if(newnum in nums):
			if(len(nums[newnum]) == 2):
				newl = [nums[last_number][-1]]
				newl.append(last_spoken)
				nums[newnum] = newl
			else:
				nums[newnum].append(last_spoken)
		else:
			nums[newnum] = [last_spoken]
#	print(nums)
