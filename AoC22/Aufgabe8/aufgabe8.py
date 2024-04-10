data = open("input.txt")
trees = [[int(x) for x in line] for line in data.read().splitlines()]

m = len(trees)
n = len(trees[0])

s = []

for i in range(0,m):
    s.append([])
    maxl = -1
    for j in range(0,n):
        if trees[i][j]>maxl:
            maxl = trees[i][j]
            s[i].append(1)
        else:
            s[i].append(0)
    maxr = -1
    for j in range(0,n):
        if trees[i][n-1-j]>maxr:
            maxr = trees[i][n-1-j]
            s[i][n-1-j] = 1
for j in range(0,n):
    maxt = -1
    for i in range(0,n):
        if trees[i][j]>maxt:
            maxt = trees[i][j]
            s[i][j] = 1
    maxb = -1
    for i in range(0,n):
        if trees[m-1-i][j]>maxb:
            maxb = trees[m-1-i][j]
            s[m-1-i][j] = 1

print(sum(s[i][j] for i in range(0,n) for j in range(0,n)))

score = []
for i in range(1,m-1):
    score.append([])
    for j in range(1,n-1):
        l = 1
        r = 1
        u = 1
        d = 1
        while trees[i][j-l]<trees[i][j] and j-l>0:
            l+=1
        while trees[i][j+r]<trees[i][j] and j+r<n-1:
            r+=1
        while trees[i-u][j]<trees[i][j] and i-u>0:
            u+=1
        while trees[i+d][j]<trees[i][j] and i+d<m-1:
            d+=1
        score[i-1].append(l*r*u*d)

print(max(score[i][j] for i in range(0,m-2) for j in range(0,n-2)))

