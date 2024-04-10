data = open("input9.txt")
height = [[int(x) for x in line] for line in data.read().splitlines()]

m = len(height)
n = len(height[0])


def offrange(i,j):
    return (i<0 or i>m-1 or j<0 or j>n-1)

total = 0
basins = []
for i in range(m):
    for j in range(n):
        h = height[i][j]
        adj = set([(i+1,j),(i-1,j),(i,j+1),(i,j-1)])
        if all([(offrange(x,y) or height[x][y]>h) for (x,y) in adj]):
            #print(i,j)
            basin = set([(i,j)])
            new = set([(i,j)])
            while len(new) > 0:
                c = new.pop()
                (x,y) = c[0],c[1]
                adjc = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                for (a,b) in adjc:
                    if (not offrange(a,b)) and (not (a,b) in basin) and height[a][b] > height[x][y] and height[a][b] <9:
                        basin.add((a,b))
                        new.add((a,b))
            #print(i,j,len(basin))
            basins.append(len(basin))
            total += h+1
print(total)
basins.sort()
print(basins)
print(basins[-1]*basins[-2]*basins[-3])
