my_input = [line.rstrip() for line in open("input").readlines()]

left_list = []
right_list = []

for line in my_input:
    a, b = [int(x) for x in line.split('   ')]
    left_list.append(a)
    right_list.append(b)
    
left_list = sorted(left_list)
right_list = sorted(right_list)

#part 1
total = 0
for i in range(len(left_list)):
    total += abs(left_list[i] - right_list[i])

print(total)

#part 2
similarity = 0
for j in left_list:
    similarity += right_list.count(j) * j
    
print(similarity)
