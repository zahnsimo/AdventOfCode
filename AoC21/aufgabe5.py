import numpy as np
data = open("input5.txt")
coords = [[[int(x) for x in pt.split(",")] for pt in line.split(" -> ")] for line in data.read().splitlines()]

n = len(coords)
x_min = min([coords[i][j][0] for i in range(n) for j in range(2)])
x_max = max([coords[i][j][0] for i in range(n) for j in range(2)])
y_min = min([coords[i][j][1] for i in range(n) for j in range(2)])
y_max = max([coords[i][j][1] for i in range(n) for j in range(2)])

d = np.zeros((y_max-y_min+1,x_max-x_min+1), dtype=int)

for c in coords:
    [x0,y0],[x1,y1] = c
    if x0 == x1:
        for y in range(min(y0,y1),max(y0,y1)+1):
            try:
                d[y-y_min,x0-x_min] +=1
            except:
                print(y-y_min,x0-x_min)
    elif y0 == y1:
        for x in range(min(x0,x1),max(x0,x1)+1):
            try:
                d[y0-y_min,x-x_min] +=1
            except:
                print(y0-y_min, x-x_min)
    else:
        m = (y1-y0)/(x1-x0)
        if abs(m) != 1:
            print(c,m,"ahhhh")
        elif m == 1:
            k = abs(y1-y0)
            for i in range(k+1):
                x = min(x0,x1) + i
                y = min(y0,y1) + i
                try:
                    d[y-y_min,x-x_min] +=1
                except:
                    print(y-y_min,x-x_min)
        else:
            k = abs(y1-y0)
            for i in range(k+1):
                x = min(x0,x1) + i
                y = max(y0,y1) - i
                try:
                    d[y-y_min,x-x_min] +=1
                except:
                    print(y-y_min,x-x_min)


#print(d)
print(np.count_nonzero(d>1))
        
