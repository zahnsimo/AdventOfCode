data = open("input.txt")
lines = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".split("\n\n")
lines = data.read().split("\n\n")
board = lines[0].splitlines()
instructions = lines[1].strip(" ")

"""
def parse(board):
    empty = set()
    walls = set()
    off = set()
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == " ":
                off.add((x,y))
            elif board[y][x] == ".":
                empty.add((x,y))
            elif board[y][x] == "#":
                walls.add((x,y))
    return(empty,walls,off)

def parse_ins(ins):
    i = 0
    path = []
    next_R = ins.find("R")
    next_L = ins.find("L")
    while i < len(ins):
        if next_R == -1:
            next_R = len(ins)
        if next_L == -1:
            next_L = len(ins)
        if next_R < next_L:
            steps = int(ins[i:next_R])
            path.append((steps,1))

            i = next_R+1
            next_R = ins.find("R" , i)
        else:
            steps = int(ins[i:next_L])
            path.append((steps,-1))
            i = next_L+1
            next_L = ins.find("L" , i)
    (steps,dd) = path.pop(-1)
    path.append((steps,0))
    return path

DIRS = [[1,0] , [0,1] , [-1,0] , [0,-1]]
def move(x,y,steps,d):
    dx,dy = DIRS[d]
    i = 0
    while i < steps:
        x1 = x+dx
        y1 = y+dy
        if (x1,y1) in walls:
            break
        elif (x1,y1) in empty:
            i+=1
        elif dx == 0:
            y1 = 0
        else:
            x1 = 0
        x,y = x1,y1
    return x,y
            
empty,walls,off = parse(board)
#print(empty,"\n",walls,"\n",off)
path = parse_ins(instructions)
print(path)

y0 = 0
x0 = min(x for (x,y) in empty if y == y0)
print(x0,y0)
x,y = x0,y0
d = 0
for c in path:
    s,dd = c
    x,y = move(x,y,s,d)
    d = (d+dd)%4
    print(x,y,d)
print(1000 * (y+1) + 4 * (x+1) + d)
"""

def parse(lines):
    rows = {}
    max_x = 0
    for y in range(len(lines)):
        x = 0
        walls = []
        while x < len(lines[y]) and lines[y][x] == " ":
            x+=1
        start = x
        while x < len(lines[y]) and lines[y][x] != " ":
            if lines[y][x] == "#":
                walls.append(x)
            x+=1
        end = x-1
        max_x = max(max_x , end)
        rows.update({y : {"start" : start , "end" : end , "walls" : walls}})
    columns = {}
    for x in range(max_x):
        y = 0
        walls = []
        while x >= len(lines[y]) or lines[y][x] == " ":
            y+=1
        start = y
        while y < len(lines) and x < len(lines[y]) and lines[y][x] != " ":
            if lines[y][x] == "#":
                walls.append(y)
            y+=1
        end = y-1
        columns.update({x : {"start" : start , "end" : end , "walls" : walls}})
    return rows,columns

def parse_ins(ins):
    i = 0
    path = []
    next_R = ins.find("R")
    next_L = ins.find("L")
    while i < len(ins):
        if next_R == -1:
            next_R = len(ins)
        if next_L == -1:
            next_L = len(ins)
        if next_R < next_L:
            steps = int(ins[i:next_R])
            path.append((steps,1))
            i = next_R+1
            next_R = ins.find("R" , i)
        else:
            steps = int(ins[i:next_L])
            path.append((steps,-1))
            i = next_L+1
            next_L = ins.find("L" , i)
    (steps,dd) = path.pop(-1)
    path.append((steps,0))
    return path

DIRS = [[1,0] , [0,1] , [-1,0] , [0,-1]]

def move(x,y,steps,d):
    if d%2 == 1:
        line = columns[x]
        z = y
    else:
        line = rows[y]
        z = x
    if d < 2:
        dz = 1
    else:
        dz = -1
    s = line["start"]
    e = line["end"]
    l = e-s+1
    i = 0
    while i < steps and not (z+dz) in line["walls"]:
        z += dz
        if z > e:
            z = s
        elif z < s:
            z = e
        i+=1
    if d %2 == 1:
        return (x,z,d)
    else:
        return (z,y,d)

rows,columns = parse(board)
path = parse_ins(instructions)
#print("rows",rows,  "\n" ,"columns", columns)
#print(path)
y = 0
x = rows[y]["start"]
d = 0
print(x,y,d)
for c in path:
    s,dd = c
    x,y,d = move(x,y,s,d)
    d = (d+dd)%4
    #print(x,y,d)
print(1000 * (y+1) + 4 * (x+1) + d)

