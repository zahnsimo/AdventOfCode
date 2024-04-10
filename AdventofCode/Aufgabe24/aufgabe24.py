import numpy as np
data = open("input.txt")
lines = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".splitlines()
lines = data.read().splitlines()

def parse(lines):
    start = lines[0].find(".")
    end = lines[-1].find(".")
    n = len(lines) - 2
    m = len(lines[0]) - 2
    A = np.zeros([m,n] , dtype = int)
    for y in range(1,n+1):
        for x in range(1,m+1):
            if lines[y][x] == ">":
                A[x-1,y-1] = 0
            elif lines[y][x] == "v":
                A[x-1,y-1] = 1
            elif lines[y][x] == "<":
                A[x-1,y-1] = 2
            elif lines[y][x] == "^":
                A[x-1,y-1] = 3
            else:
                A[x-1,y-1] = -1
    return A,m,n,start,end

A,m,n,start,end = parse(lines)
print(m,n,start,end)

def blizzard(x,y,t):
    if x == start and y == 0:
        return False
    elif x == end and y == n+1:
        return False
    else:
        return (A[(x-1-t)%m,y-1] == 0 or A[x-1,(y-1-t)%n] == 1
                or A[(x-1+t)%m,y-1] == 2 or A[x-1,(y-1+t)%n] == 3)
                
                
def in_bounds(x,y):
    return ((x>0 and x < m+1 and y > 0 and y<n+1) or (x ==start and y ==0)
            or (x == end and y == n+1))

DIRS = [[1,0] , [0,1] , [-1,0] , [0,-1] , [0,0]]

def find_path(t_start,x0,y0,x1,y1):
    t = t_start
    q = {(x0,y0)}
    while len(q) > 0:
        t +=1
        new_q = set()
        for (x,y) in q:
            for [dx,dy] in DIRS:
                if x+dx == x1 and y+dy == y1:
                    return t
                elif in_bounds(x+dx,y+dy) and not blizzard(x+dx,y+dy,t):
                    new_q.add((x+dx,y+dy))
        q = new_q

t1 = find_path(0 , start,0,end,n+1)
t2 = find_path(t1,end,n+1,start,0)
t3 = find_path(t2,start,0,end,n+1)
print(t1,t2,t3)

