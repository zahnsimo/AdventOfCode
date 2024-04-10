import numpy as np
data = open("input11.txt")
octos=np.array([[int(x) for x in s] for s in data.read().splitlines()])

(m,n) = octos.shape

def inrange(i,j):
    return(i>=0 and i<m and j>=0 and j<n)

dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
def step(octos):
    octos[:] +=1
    s = [(x,y) for x in range(m) for y in range(n) if octos[x,y] > 9]
    for p in s:
        x,y = p[0],p[1]
        for d in dirs:
            dx,dy = d[0],d[1]
            if inrange(x+dx,y+dy):
                octos[x+dx,y+dy] +=1
                if octos[x+dx,y+dy] > 9 and not(x+dx,y+dy) in s:
                    s.append((x+dx,y+dy))
    for (x,y) in s:
        octos[x,y] = 0
    return(len(s))
                
flash = 0
i = 0
while flash < 100:
    flash = step(octos)
    i+=1
    if i%50 == 0:
        print(i)
print(i)
#for i in range(100):
#    flash += step(octos)
print(flash)
