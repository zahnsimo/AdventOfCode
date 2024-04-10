import numpy as np
data = open("input19.txt")
scanners = [[np.array([int(x) for x in line.split(",")],dtype = int)
             for line in bloc.splitlines()[1:]]
            for bloc in data.read().split("\n\n")]

FLIPS = [np.array(a,dtype = int) for a in [ [[1,0,0],[0,1,0],[0,0,1]],
                                            [[1,0,0],[0,0,-1],[0,1,0]],
                                            [[1,0,0],[0,-1,0],[0,0,-1]],
                                            [[1,0,0],[0,0,1],[0,-1,0]],
                                            [[-1,0,0],[0,-1,0],[0,0,1]],
                                            [[-1,0,0],[0,0,-1],[0,-1,0]],
                                            [[-1,0,0],[0,1,0],[0,0,-1]],
                                            [[-1,0,0],[0,0,1],[0,1,0]],
                                            [[0,1,0],[0,0,1],[1,0,0]],
                                            [[0,1,0],[-1,0,0],[0,0,1]],
                                            [[0,1,0],[0,0,-1],[-1,0,0]],
                                            [[0,1,0],[1,0,0],[0,0,-1]],
                                            [[0,-1,0],[0,0,-1],[1,0,0]],
                                            [[0,-1,0],[1,0,0],[0,0,1]],
                                            [[0,-1,0],[0,0,1],[-1,0,0]],
                                            [[0,-1,0],[-1,0,0],[0,0,-1]],
                                            [[0,0,1],[1,0,0],[0,1,0]],
                                            [[0,0,1],[0,-1,0],[1,0,0]],
                                            [[0,0,1],[-1,0,0],[0,-1,0]],
                                            [[0,0,1],[0,1,0],[-1,0,0]],
                                            [[0,0,-1],[-1,0,0],[0,1,0]],
                                            [[0,0,-1],[0,1,0],[1,0,0]],
                                            [[0,0,-1],[1,0,0],[0,-1,0]],
                                            [[0,0,-1],[0,-1,0],[-1,0,0]] ]]

def find_overlap(i,j):
    m = len(scanners[i])
    n = len(scanners[j])
    for F in FLIPS:
        A = np.array([[scanners[i][k] - F.dot(scanners[j][l]) for l in range(n)]
                  for k in range(m)] )
        values, indices , counts = np.unique(A, return_counts = True,return_index = True)
        if np.count_nonzero(counts > 11) >=3:
            if np.count_nonzero(counts > 11) > 3:
                print("ohoh" , i , j)
            rel = [[values[i],(indices[i])%3] for i in range(len(counts)) if counts[i]>11]
            rel.sort(key=lambda x: x[1])
            rel_coords = [l[0] for l in rel]
            return(rel_coords, F)

s = list(range(1,len(scanners)))
l = [0]
rel_pos = {0 : {"rel_coords": np.array([0,0,0],dtype = int) , "or": FLIPS[0]}}
while len(s)>0:
    for i in l:
        for j in s:
            if find_overlap(i,j):
                rel_coords, F = find_overlap(i,j)
                l.append(j)
                s.remove(j)
                rel_pos.update({j : {"rel_coords" : rel_pos[i]["rel_coords"]
                                    + np.matmul(rel_pos[i]["or"],rel_coords),
                                    "or" : np.matmul(rel_pos[i]["or"] , F)}})
                print(j,rel_pos[j]["rel_coords"])

beacons = set()
for j in range(len(scanners)):
    rel_coords = rel_pos[j]["rel_coords"]
    F = rel_pos[j]["or"]
    for k in range(len(scanners[j])):
        new_beacon = rel_coords + np.matmul(F,scanners[j][k])
        
        beacons.add(tuple(new_beacon))
    print(j,len(beacons))


#for c in sorted(beacons):
#    print(c)
#print([c , "\n" for c in sorted(beacons)])
    
