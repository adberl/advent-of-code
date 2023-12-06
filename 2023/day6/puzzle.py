my_input = [line.rstrip() for line in open("input").readlines()]

times = [int(x) for x in my_input[0].split(": ")[1].split(' ') if x != '']
records = [int(x) for x in my_input[1].split(": ")[1].split(' ') if x != '']

# part1
res = 1
for race in range(len(times)):
    race_start = -1
    race_end = -1
    for i in range(times[race]+1):
        time_for_race = times[race]
        if i * (time_for_race-i) > records[race]:
            race_start = i if race_start == -1 else race_start
            race_end = i
    print(f"For race time {times[race]} with record {records[race]} we got: {race_start}, {race_end} which is: {race_end-race_start+1}")
    res *= race_end-race_start+1
print(res)
                
# part2
one_time = int(''.join([x for x in my_input[0].split(": ")[1].split(' ') if x != '']))
one_record = int(''.join([x for x in my_input[1].split(": ")[1].split(' ') if x != '']))

where_we_start = -1
where_we_end = -1

is_better_time = lambda x: x * (one_time-x) > one_record
print(is_better_time(10000000))
midpoint = 10000000 # determined empirically above :)

left_cond = lambda x: is_better_time(x) and not is_better_time(x-1)
right_cond = lambda x: is_better_time(x) and not is_better_time(x+1)

midpoint_left = midpoint/2
left = 0
right = midpoint
while not left_cond(midpoint_left):
    if is_better_time(midpoint_left):
        right = midpoint_left
        midpoint_left = midpoint_left//2
    else:
        left = midpoint_left
        midpoint_left = (midpoint_left+right)//2 

midpoint_right = (one_time+midpoint)/2
left = midpoint
right = one_time
while not right_cond(midpoint_right):
    if is_better_time(midpoint_right):
        left = midpoint_right
        midpoint_right = (midpoint_right+right)//2
    else:
        right = midpoint_right
        midpoint_right = (midpoint_right+left)//2

print(midpoint_left, midpoint_right, midpoint_right-midpoint_left+1)

