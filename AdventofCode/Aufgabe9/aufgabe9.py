#import numpy as np
data = open("input.txt")
lines = [line.split(" ") for line in data.read().splitlines()]

x = []
y = []
for i in range(0,10):
    x.append(0)
    y.append(0)

positions = {(0,0)}

def sign(x):
    if x >= 0:
        return 1
    elif x<0:
        return -1
    
def move_head(x_H,y_H, direction):
    if direction == "R":
        x_H += 1
    elif direction == "U":
        y_H += 1
    elif direction == "L":
        x_H -= 1
    elif direction == "D":
        y_H -= 1
    return([x_H,y_H])


def follow(x_H,y_H,x_T,y_T):
    if x_H == x_T + 2 and y_H == y_T:
        x_T +=1
    elif x_H == x_T + 2 and y_H == y_T + 1:
        x_T +=1
        y_T +=1
    elif x_H == x_T + 2 and y_H == y_T - 1:
        x_T +=1
        y_T -=1
    elif y_H == y_T + 2 and x_H == x_T:
        y_T +=1
    elif y_H == y_T + 2 and x_H == x_T + 1:
        y_T +=1
        x_T +=1
    elif y_H == y_T + 2 and x_H == x_T - 1:
        y_T +=1
        x_T -=1
    elif x_H == x_T - 2 and y_H == y_T:
        x_T -=1
    elif x_H == x_T - 2 and y_H == y_T + 1:
        x_T -=1
        y_T +=1
    elif x_H == x_T - 2 and y_H == y_T - 1:
        x_T -=1
        y_T -=1
    elif y_H == y_T - 2 and x_H == x_T:
        y_T -=1
    elif y_H == y_T - 2 and x_H == x_T + 1:
        y_T -=1
        x_T +=1
    elif y_H == y_T - 2 and x_H == x_T - 1:
        y_T -=1
        x_T -=1
    return([x_T,y_T])

def follow_alt(x_H,y_H,x_T,y_T):
    if abs(x_H-x_T) ==2 or abs(y_H-y_T)==2:
        x_T = x_H - sign(x_H-x_T)*(abs(x_H-x_T)//2)
        y_T = y_H - sign(y_H-y_T)*(abs(y_H-y_T)//2)
    return([x_T,y_T])

for line in lines:
    direction = line[0]
    for i in range(0,int(line[1])):
        x[0],y[0] = move_head(x[0],y[0],direction)
        for i in range(1,10):
            x[i],y[i] = follow_alt(x[i-1],y[i-1],x[i],y[i])
        positions.add((x[9],y[9]))

print(len(positions))

#print(pos_tail)
