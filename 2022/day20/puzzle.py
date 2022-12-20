encrypted_file = [int(l.rstrip()) for l in open("input").readlines()]

class Number():
    def __init__(self, initial_id, value):
        self.iid = initial_id
        self.val = value

    def __repr__(self):
        return f'{self.val}'
        #return f'(id:{self.iid},val:{self.val})'

decryption_key = 811589153 # this is 1 for part 1
numbers = []
for idx, number in enumerate(encrypted_file):
    numbers.append(Number(idx, number*decryption_key))

max_id = len(numbers)
mixings = 10 # this is 1 for part 1
for _ in range(mixings):
    for iid in range(max_id):
        new_numbers = numbers.copy()
        for cid, number in enumerate(numbers):
            if iid == number.iid:
                if number.val == 0:
                    break
                my_number = new_numbers.pop(cid)
                    # 0 doesn't move
    
                moving_forward = my_number.val > 0
                movement = cid + my_number.val

                newid = movement % (max_id-1)
                new_numbers.insert(newid, my_number)

                #print(f'num:{number}|newid:{newid}|movement:{cid+number.val}')
                break
        numbers = new_numbers
        #print(numbers)

zeroid = 0
for idx, number in enumerate(numbers):
    if number.val == 0:
        zeroid = idx
        break

coords = []
for k in [1000, 2000, 3000]:
    coords.append(numbers[(zeroid + k) % max_id].val)

print('Solution:')
print(coords)
print(sum(coords))