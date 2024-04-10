import numpy as np
data = open("input.txt")
cubes = [[int(x) for x in line.split(",")] for line in data.read().splitlines()]

def connected_sides(cube,l):
    x0,y0,z0 = cube
    return sum(((abs(x0-x)+abs(y0-y)+abs(z0-z)) == 1) for [x,y,z] in l)

def count_sides(cubes):
    total = 0
    l = []
    for cube in cubes:
        s = connected_sides(cube,l)
        total +=(6-2*s)
        l.append(cube)
    return total

x_min = min(c[0] for c in cubes)
x_max = max(c[0] for c in cubes) -x_min +1
y_min = min(c[1] for c in cubes)
y_max = max(c[1] for c in cubes) -y_min +1
z_min = min(c[2] for c in cubes)
z_max = max(c[2] for c in cubes) -z_min +1

cubes = [[x-x_min+1,y-y_min+1,z-z_min+1] for [x,y,z] in cubes]

def inside_bounds(x,y,z):
    return (x >=0 and x <=x_max+1 and y >=0 and y <=y_max+1 and z >=0 and z <=z_max+1)

DIRS = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]

A = np.ones((x_max+2, y_max+2,z_max+2) , dtype=int)
for c in cubes:
    x,y,z = c
    A[x,y,z] = 0

q = [(0,y,z) for y in range(0,y_max+2) for z in range(0,z_max+2)]
for c in q:
    x,y,z = c
    A[x,y,z] = -1
while len(q) > 0:
    c = q.pop(0)
    x,y,z = c
    for dir in DIRS:
        a,b,c = dir
        if inside_bounds(x+a,y+b,z+c) and A[x+a,y+b,z+c]==1:
            q.append([x+a,y+b,z+c])
            A[x+a,y+b,z+c] = -1

innen = np.where(A == 1)
innen = [(innen[0][i],innen[1][i],innen[2][i]) for i in range(0,len(innen[0]))]

all_sides = count_sides(cubes)
inner_sides = count_sides(innen)
print(all_sides,inner_sides,all_sides-inner_sides)
