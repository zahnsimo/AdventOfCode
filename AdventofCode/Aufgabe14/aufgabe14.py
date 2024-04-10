data = open("input.txt")
lines = [line.split("->") for line in data.read().splitlines()]

blocked = set()
for line in lines:
    x,y = [int(a) for a in line[0].split(",")]
    blocked.add((x,y))
    for i in range(1,len(line)):
        x_new,y_new = [int(a) for a in line[i].split(",")]
        for j in range(x,x_new+1):
            blocked.add((j,y))
        for j in range(x_new,x+1):
            blocked.add((j,y))
        for j in range(y,y_new+1):
            blocked.add((x,j))
        for j in range(y_new,y+1):
            blocked.add((x,j))
        x,y = x_new,y_new

y_max = max(y for (x,y) in blocked)

def falling_sand(blocked):
    x = 500
    for y in range(0,y_max+2):
        if not (x,y+1) in blocked:
            pass
        elif not (x-1,y+1) in blocked:
            x -=1
        elif not (x+1,y+1) in blocked:
            x+=1
        else:
            blocked = blocked.add((x,y))
            return(x,y)
    blocked = blocked.add((x,y))
    return(x,y)

y = 1
i = 0
while y>0:
    (x,y) = falling_sand(blocked)
    i+=1

print(i)

