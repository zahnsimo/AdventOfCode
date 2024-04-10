data = open("input.txt")
map = data.read().splitlines()

def find_S(map):
    i = 0
    j = map[0].find("S")
    while j == -1:
        i+=1
        j = map[i].find("S")
    map[i] = map[i].replace("S", "a")
    return(i,j)

def find_E(map):
    i = 0
    j = map[0].find("E")
    while j == -1:
        i+=1
        j = map[i].find("E")
    map[i] = map[i].replace("E", "z")
    return(i,j)


def find_path(map):
    m = len(map)
    n = len(map[0])
    xS,yS = find_S(map)
    xE,yE = find_E(map)
    dist = []
    for i in range(0,m):
        dist.append([])
        for j in range(0,n):
            dist[i].append(-1)
    l = [(xE,yE)]
    d = 0
    while l != []:
        l_new = []
        for (x,y) in l:
            if dist[x][y] == -1:
                dist[x][y] = d
                if map[x][y] == "a":
                    return(d)
                if x+1 < m and ord(map[x][y]) - ord(map[x+1][y]) <=1:
                    l_new.append((x+1,y))
                if x-1 >= 0 and ord(map[x][y]) - ord(map[x-1][y]) <=1:
                    l_new.append((x-1,y))
                if y+1 <n and ord(map[x][y]) - ord(map[x][y+1]) <=1:
                    l_new.append((x,y+1))
                if y-1 >=0 and ord(map[x][y]) - ord(map[x][y-1]) <=1:
                    l_new.append((x,y-1))
        d +=1
        l = l_new
        #return(dist[xS][yS])

print(find_path(map))
        
