data = open("input.txt")
lines = [line.split(" ") for line in data.read().splitlines()]

ordner = []
for i in range(0,len(lines)):
    if lines[i][1] == "cd" and lines[i][2] != "..":
        name = lines[i][2]
        #print(name)
        level = 1
        j = i+2
        s = 0
        while level > 0 and j < len(lines):
            if lines[j][1] ==  "ls":
                pass
            elif lines[j][1] == "cd":
                if lines[j][2] == "..":
                    level -=1
                else:
                    level +=1
            elif lines[j][0] == "dir":
                pass
            else:
                #print(j,lines[j])
                s += int(lines[j][0])
            j+=1
        ordner.append((name,s))

print(sum(y for (x,y) in ordner if y <= 100000))
free = 70000000 - ordner[0][1]
toomuch = 30000000 - free
print(free,toomuch)
print(min(y for (x,y) in ordner if y >= toomuch))    
