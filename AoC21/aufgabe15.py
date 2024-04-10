import numpy as np
data = open("input15.txt")
risk = np.array([[int(x) for x in line] for line in """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".splitlines()])
(m,n) = risk.shape

big_cave = np.zeros((5*m,5*n),dtype = int)
for i in range(5):
    for j in range(5):
        big_cave[i*m:(i+1)*m,j*n:(j+1)*n] = (risk[:,:]+i+j-1)%9+1
#print(big_cave)

dirs = [np.array(x) for x in [[-1,0],[0,1],[1,0],[0,-1]]]
dist = np.zeros((5*m,5*n),dtype =int)

def inrange(x,y):
    return(x>=0 and x<5*m and y>=0 and y<5*n)

s = [(0,0)]
while len(s) > 0:
    c = s.pop(0)
    (x0,y0) = c[0],c[1]
    for d in dirs:
        new = c+d
        (x,y) = new[0],new[1]
        if inrange(x,y) and (dist[x,y] == 0 or dist[x,y] > dist[x0,y0] + big_cave[x,y]):
            dist[x,y] = dist[x0,y0] + big_cave[x,y]
            s.append((x,y))
print(dist[-1,-1])
