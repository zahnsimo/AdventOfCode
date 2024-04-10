data = open("input17.txt")
target = [[int(x) for x in s.split("..")] for s in "target area: x=155..215, y=-132..-72".strip("target area: x=").split(", y=")]


def sgn(x):
    if x >= 0:
        return 1
    else:
        return -1

def inrange(x0,y0): #assume all x-coords are pos
    x,y = 0,0
    vx,vy = x0,y0
    while y >= target[1][0]:
        if (x in range(target[0][0],target[0][1]+1)
            and y in range(target[1][0],target[1][1]+1)):
            return True
        x += vx
        y += vy
        vx = max(vx-1,0)
        vy -= 1
    return False

def maxy(y0):
    y = 0
    vy = y0
    while vy > 0:
        y += vy
        vy -= 1
    return y

#y0 = 100
#xrange = [x0 for x0 in range(0,target[0][1]) if inrange(x0,y0)]
#while len(xrange) > 0:
#    y0+=1
#    xrange = [x0 for x0 in range(0,target[0][1]) if inrange(x0,y0)]
#print(y0,maxy(y0))

#for y0 in range(100,200):
#    print(y0,[x0 for x0 in range(0,target[0][1]) if inrange(x0,y0)])


#print([(x0,y0) for y0 in range(-20,20) for x0 in range(0,target[0][1]+1) if inrange(x0,y0)])

print(sum([sum([inrange(x0,y0) for x0 in range(0,target[0][1]+1) ]) for y0 in range(-200,200) ] ))

    

        
    
