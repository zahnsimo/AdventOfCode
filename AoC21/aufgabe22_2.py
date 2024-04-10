def parse(line):
    b = (line[1] == "n")
    coords = [[int(x) for x in s.strip("on off xyz=").split("..")] for s in line.split(",")]
    coords = [[coords[i][0],coords[i][1]+1] for i in range(len(coords))]
    return b,coords

data = open("input22.txt")
instructions = [parse(line) for line in data.read().splitlines()]

def overlap_interval(l0,l1):
    x0,x1 = l0
    x2,x3 = l1
    return not(x1<=x2 or x3<=x0)

def overlap(c0,c1):
    return all([overlap_interval(c0[i],c1[i]) for i in range(3)])

def cut_interval(l0,l1): # l1 without l0
    xs = sorted(l0+l1)
    ins = [[xs[i],xs[i+1]] for i in range(3)
           if overlap_interval([xs[i],xs[i+1]],l1)
           and overlap_interval([xs[i],xs[i+1]],l0)] #l1 and l0
    outs = [[xs[i],xs[i+1]] for i in range(3)
           if overlap_interval([xs[i],xs[i+1]],l1)
           and not overlap_interval([xs[i],xs[i+1]],l0)] #l1 without l0
    return ins,outs
    

def cut(c0,c1): #c1 without c0
    ints = [cut_interval(c0[i],c1[i]) for i in range(3)]
    cubes = [ [l, c1[1], c1[2]] for l in ints[0][1]]
    cubes+= [ [l0, l1, c1[2]] for l0 in ints[0][0] for l1 in ints[1][1]]
    cubes+= [ [l0, l1, l2] for l0 in ints[0][0] for l1 in ints[1][0]
              for l2 in ints[2][1] ]
    return cubes

def size(c):
    return((c[0][1]-c[0][0])*(c[1][1]-c[1][0])*(c[2][1]-c[2][0]))

onset = []
for instr in instructions:
    b , c = instr
    if b:
        new_cubes = [c]
        for c0 in onset:
            for c1 in new_cubes:
                if overlap(c0,c1):
                    new_cubes.remove(c1)
                    new_cubes += cut(c0,c1)
        onset += new_cubes
    else:
        new_cubes = []
        for c0 in onset:
            if overlap(c0,c):
                onset.remove(c0)
                new_cubes += cut(c,c0)
        onset += new_cubes
    #print(onset)
    on = sum([size(cube) for cube in onset])
    print(on)
#print(sum([size(cube) for cube in onset]))

test_cube = [[-50,51],[-50,51],[-50,51]]
outer_cubes = []
for c in onset:
    outer_cubes += cut(test_cube,c)
#outer_cubes = [cut(test_cube,c) for c in onset]
on_out = sum([size(cube) for cube in outer_cubes])
print(on,on_out,on-on_out)

