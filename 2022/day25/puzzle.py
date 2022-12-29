numbers = [l.rstrip() for l in open("input").readlines()]

sc = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}

pof = [5**i*2 for i in range(30)]

def from_snafu(number):
    ret_num = 0
    for i,x in enumerate(reversed(number)):
        ret_num += 5**i * sc[x]
    return ret_num

def to_snafu(number):
    exp = 0
    res = []
    for g in range(len(pof)):
        if sum(pof[:g]) >= number:
            exp = g-1
            break
    
    while exp >= 0:
        k = [-2, -1, 0] if number < 0 else [2, 1, 0]
        for i in k:
            r1, r2 = 5**exp * i - sum(pof[:exp]), 5**exp * i + sum(pof[:exp])
            left_range, right_range = min(r1, r2), max(r1, r2)
            
            # if our number is in range, then we set it and continue
            if left_range <= number <= right_range:
                my_number = 5**exp * i
                number = number - my_number
                res.append(i)
                break
        exp -= 1
    return ''.join([{v:k for k,v in sc.items()}[i] for i in res])

# 31487399529835
print(to_snafu(sum([from_snafu(x) for x in numbers])))