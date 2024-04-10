import numpy as np

def parse(line):
    b = (line[1] == "n")
    coords = [[int(x) for x in s.strip("on off xyz=").split("..")] for s in line.split(",")]
    return b,coords

data = open("input22.txt")
instructions = [parse(line) for line in data.read().splitlines()]


core = np.zeros((103,103,103), dtype = int)

def flip(core,instr):
    b,coords = instr
    for c in coords:
        c[0] = max(c[0], -51)
        c[1] = min(c[1] , 51)
    if b:
        core[coords[0][0]+51 : coords[0][1]+52 , coords[1][0]+51:coords[1][1]+52,
             coords[2][0]+51 : coords[2][1]+52] = 1
    else:
        core[coords[0][0]+51 : coords[0][1]+52 , coords[1][0]+51:coords[1][1]+52,
             coords[2][0]+51 : coords[2][1]+52] = 0
    return core


#for line in instructions:
#    core = flip(core,line)

#print(np.count_nonzero(core[1:101,1:101,1:101]))
#print(np.count_nonzero(core))
#print(np.where(core==1))

data2 = open("test22.txt")
instructions2 = [parse(line) for line in data2.read().splitlines()]
#print(len(instructions2),instructions2[0])

#onset = set()

def flip_alt(onset,instr):
    b,c = instr
    if b:
        for x in range(c[0][0],c[0][1]+1):
            for y in range(c[1][0],c[1][1]+1):
                for z in range(c[2][0],c[2][1]+1):
                    onset.add((x,y,z))
    else:
        for x in range(c[0][0],c[0][1]+1):
            for y in range(c[1][0],c[1][1]+1):
                for z in range(c[2][0],c[2][1]+1):
                    onset.discard((x,y,z))
    return onset

def overlap_interval(l0,l1):
    x0,x1 = l0
    x2,x3 = l1
    return not(x1<x2 or x3<x0)

def overlap(c0,c1):
    return all([overlap_interval(c0[i],c1[i]) for i in range(3)])

def split(b0,c0,b1,c1):
    #print(c0)
    #print(c1)
    xs = sorted([c0[0][0],c0[0][1],c1[0][0],c1[0][1]])
    ys = sorted([c0[1][0],c0[1][1],c1[1][0],c1[1][1]])
    zs = sorted([c0[2][0],c0[2][1],c1[2][0],c1[2][1]])
    cubes = [ [ [xs[i],xs[i+1]] , [ys[j],ys[j+1]] , [zs[k],zs[k+1]] ]
              for i in range(3) for j in range(3) for k in range(3)]
    #print(len(cubes),cubes)
    ons = []
    for q in cubes:
        if overlap(q,c1):
            if b1:
                ons.append(q)
        elif overlap(q,c0):
            if b0:
                ons.append(q)
    return ons

b0,c0 = instructions2[0]
b1,c1 = instructions2[1]
ons = split(b0,c0,b1,c1)
print(len(ons),ons)

onset = []

for line in instructions2:
    pass


#for line in instructions2:
#    onset = flip_alt(onset,line)
#    print(len(onset))
