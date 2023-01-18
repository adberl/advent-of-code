cubes = [[int(i) for i in l.rstrip().split(',')] for l in open("input").readlines()]

def get_movements():
    g = []
    for i in range(3): # 3D space
        for a in [0, 1]: # it can either stay the same or increase by 1
            tmp_coord = [0, 0, 0]
            m = []
            for b in [0, 1]:
                for c in [0, 1]:
                    tmp_coord[i] = a
                    tmp_coord[i-2] = b
                    tmp_coord[i-1] = c
                    m.append(tmp_coord.copy())
            g.append(m.copy())
    return g

movements = get_movements()
f = open('myshape.stl', 'w')

for idx, cube in enumerate(cubes):
    f.write(f'solid DROPLET{idx}\n')
    f.write('\tfacet\n')
    for m in movements:
        for i in [0, 1]:
            f.write('\t\touter loop\n')
            for vert in m[i:i+3]:
                vertex = [str(float(sum(x))) for x in zip(cube, vert)]
                f.write('\t\t\tvertex ')
                f.write(' '.join(vertex) + '\n')
            f.write('\t\tendloop\n')
    f.write('\tendfacet\n')
    f.write(f'endsolid DROPLET{idx}\n')



