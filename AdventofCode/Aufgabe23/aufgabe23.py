data = open("input.txt")
lines = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............""".splitlines()
lines = data.read().splitlines()

def parse(lines):
    pos = set()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                pos.add((x,y))
    return pos

def draw(pos):
    y_min, y_max = 0,len(lines)
    x_min,x_max = 0,len(lines[0])
    #y_min = min(y for (x,y) in pos)
    #y_max = max(y for (x,y) in pos)
    #x_min = min(x for (x,y) in pos)
    #x_max = max(x for (x,y) in pos)
    y = y_min
    while y <= y_max:
        s = ""
        x = x_min
        while x <= x_max:
            if (x,y) in pos:
                s += "#"
            else:
                s += "."
            x +=1
        y +=1
        print(s)
    print("\n")
pos = parse(lines)

DIRS = [[0,-1] , [1,-1] , [-1,-1] ,
        [0,1] , [1,1] , [-1,1] ,
        [-1,0] , [-1,1] , [-1,-1] ,
        [1,0] , [1,1] , [1,-1]]
def new_p(p,pos,r):
    x,y = p
    if any((x+dx , y+dy) in pos for [dx,dy] in DIRS):
        for i in range(4):
            d = (r+i)%4
            if all((x+dx,y+dy) not in pos for [dx,dy] in DIRS[(3*d):(3*d+3)]):
                dx,dy = DIRS[3*d]
                return (x+dx,y+dy)
        return (x,y)
    else:
        return (x,y)

def do_round(pos,r):
    prop = {}
    new_pos = set()
    for p0 in pos:
        p1 = new_p(p0 , pos, r)
        if not p1 in prop:
            prop.update({p1:[p0]})
        else:
            l = prop[p1]
            l.append(p0)
    for p1 in prop:
        if len(prop[p1]) == 1:
            if p1 != None:
                new_pos.add(p1)
        else:
            for p0 in prop[p1]:
                if p0 != None:
                    new_pos.add(p0)
    return new_pos


elves_moved = True
r = 0
while elves_moved:
    new_pos = do_round(pos,r)
    elves_moved = (pos != new_pos)
    pos = new_pos
    r+=1
print(r)

y_min = min(y for (x,y) in pos)
y_max = max(y for (x,y) in pos)
x_min = min(x for (x,y) in pos)
x_max = max(x for (x,y) in pos)
print((x_max-x_min+1)*(y_max-y_min+1) - len(pos))
    
