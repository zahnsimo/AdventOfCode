import numpy as np
data = open("input.txt")
#directions = data.read().replace("\n","")
directions = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

shapes = [[(0,0),(1,0),(2,0),(3,0)] ,
          [(1,0),(0,1),(1,1),(2,1),(1,2)] ,
          [(0,0),(1,0),(2,0),(2,1),(2,2)] ,
          [(0,0),(0,1),(0,2),(0,3)] ,
          [(0,0),(1,0),(0,1),(1,1)]]

rows = [[]]
for x in range(0,9):
    rows[0].append(1)
for y in range(1,8):
    rows.append([])
    rows[-1].append(1)
    for x in range(1,8):
        rows[-1].append(0)
    rows[-1].append(1)

def isblocked(coords,rows):
    return any(rows[y][x] for (x,y) in coords)

def draw(rows):
    y = len(rows)-1
    while y>=0:
        s = ""
        for x in rows[y]:
            if x:
                s += "#"
            else:
                s+= " "
        print(s)
        y-=1
    print("\n")

h = 0
t = 0
deleted = 0
h_max = [0,0,0,0,0,0,0]
found_period = False
r = 0
h_max_save = []
test = 0
while not found_period:
#for r in range(0,100001):
    coords = [(x+3,y+h+4) for (x,y) in shapes[r%5]]
    coords_down = [(x,y-1) for (x,y) in coords]
    while not isblocked(coords_down,rows) or (t%2) == 0:
        if t%2 == 1:
            coords = coords_down
        else:
            if directions[(t//2)%len(directions)] == ">":
                d = 1
            elif directions[(t//2)%len(directions)] == "<":
                d = -1
            new_coords = [(x+d,y) for (x,y) in coords]
            if not isblocked(new_coords,rows):
                coords = new_coords
        coords_down = [(x,y-1) for (x,y) in coords]
        t +=1
    t+=1
    for c in coords:
        x,y = c
        rows[y][x] =1
        h_max[x-1] = max(h_max[x-1] , y)
    max_y = max(y for (x,y) in coords)
    for j in range(0,min(h_max)):
        deleted +=1
        rows.pop(0)
        h -= 1
        h_max = [h_max[x]-1 for x in range(0,7)]
        max_y -=1
    for j in range(h , max_y):
        rows.append([])
        rows[-1].append(1)
        for x in range(1,8):
            rows[-1].append(0)
        rows[-1].append(1)
    h+= max(max_y-h , 0)
    if r >= 100 and r <= 110:
        h_max_save.append(h_max)
    if r > 100 and h_max == h_max_save[0]:
        print("r:" , r , "h:" , h , "h_max:" , [y + deleted for y in h_max])
        period_found = True
    #draw(rows)
    #if r%1000 == 0:
    #    print("r:", r , "h:" , h , "h_max:" , h_max , "deleted" , deleted)
    #print("r:", r , "h:" , h , "h_max:" , h_max , "deleted" , deleted)
    #if r%10000 == 0:
    #    print("r:" , r , "h_max:" , [y + deleted for y in h_max])
    if r == 2021:
        print("r:" , r , "h_max:" , [y + deleted for y in h_max])
    r+=1
