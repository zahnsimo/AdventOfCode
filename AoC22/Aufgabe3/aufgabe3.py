data = open("input.txt")
lines = data.readlines()

def prio(l):
    if ord(l) > 96:
        return ord(l)-96
    else:
        return ord(l)-38

s = 0
l = "a"

for line in lines:
    m = len(line)//2
    for i in range(0,m):
        for j in range(m,len(line)):
            if line[i] == line[j]:
                letter = line[i]
    #print(letter)
    s = s + prio(letter)

print(s)

t = 0

for l in range(0, len(lines), 3):
    for i in range(0, len(lines[l])-1):
        for j in range(0, len(lines[l+1])-1):
            if lines[l][i] == lines[l+1][j]:
                for k in range(0, len(lines[l+2])-1):
                    if lines[l][i] == lines[l+2][k]:
                        letter = lines[l][i]
    t = t + prio(letter)

print(t)


