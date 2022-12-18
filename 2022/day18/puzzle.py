cubes_input = [l.rstrip() for l in open("input").readlines()]

#cubes have 6 sides
def load_cubes():
    cubes = []
    max_size = 0
    for cube in cubes_input:
        x,y,z = [int(x) for x in cube.split(',')]
        cubes.append((x,y,z))
        max_size = max(max_size,x,y,z)
    return cubes, max_size
cubes, max_size = load_cubes()

def get_movements():
    movement = [0, 0, 0]
    all_movements = []
    for i in range(3):
        for j in [-1, 1]:
            tmp_movement = movement.copy()
            tmp_movement[i] = j
            all_movements.append(tmp_movement)
    return all_movements

def get_trapped_air():
    potential_air_trapped = set()
    for x in range(max_size):
        for y in range(max_size):
            for z in range(max_size):
                my_cube = (x,y,z)
                if my_cube in cubes:
                    continue
                potential_air_trapped.add(my_cube)
    return potential_air_trapped

air_pockets = get_trapped_air()

while True: # filter air pockets
    air_pockets_copy = air_pockets.copy()

    for air_pocket in air_pockets_copy:
        air_pocket_neighbours = 0
        lava_neighbours = 0
        for x,y,z in get_movements():
            neighbour = (air_pocket[0] - x, air_pocket[1] - y, air_pocket[2] - z)

            air_pocket_neighbours += neighbour in air_pockets
            lava_neighbours += neighbour in cubes

        if lava_neighbours == 6 or lava_neighbours+air_pocket_neighbours == 6: # surrounded on all sides
            continue
        
        air_pockets.remove(air_pocket)
        
    if len(air_pockets_copy) == len(air_pockets): # we removed all the fake air pockets
        break

def get_neighbours(cube):
    total_sides = 6
    for x,y,z in get_movements():
        new_cube = (cube[0] - x, cube[1] - y, cube[2] - z)
        if new_cube in cubes:
            total_sides -= 1

    return total_sides

total_sides_exposed = 0
cubes += air_pockets # comment this line for part 1
for cube in cubes:
    total_sides_exposed += get_neighbours(cube)
print(total_sides_exposed)