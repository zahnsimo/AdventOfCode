data = open("input8.txt")
lines =[[s.split(" ") for s in line.split(" | ")] for line in data.read().splitlines()]

print(sum([sum([(len(x) in {2,3,4,7}) for x in line[1]]) for line in lines]))

print(all([sorted([len(x) for x in line[0]]) == [2,3,4,5,5,5,6,6,6,7] for line in lines]))

def decipher(line):
    l = [0,0,0,0,0,0,0,0,0,0]
    line[0].sort(key = lambda x : len(x))
    l[1] = line[0][0]
    l[4] = line[0][2]
    l[7] = line[0][1]
    l[8] = line[0][9]
    for i in range(6,9):
        if set(line[0][i]).union(set(l[1])) == set(l[8]):
            l[6] = line[0][i]
        elif set(line[0][i]).union(set(l[4])) == set(l[8]):
            l[0] = line[0][i]
        else:
            l[9] = line[0][i]
    for i in range(3,6):
        if set(line[0][i]).union(set(l[1])) == set(l[9]):
            l[5] = line[0][i]
        elif set(l[1]).issubset(set(line[0][i])):
            l[3] = line[0][i]
        else:
            l[2] = line[0][i]
    x = 0
    for s in line[1]:
        x*=10
        for i in range(10):
            if set(s) == set(l[i]):
                x+=i
                break
    return x

print(sum([decipher(line) for line in lines]))

"""
def signals(l):
    l.sort(key = lambda x : len(x))
    A = set(l[1]).difference(set(l[0]))
    m1 = set(l[2]).union(A)
    for i in range(6,9):
        if m1.issubset(set(l[i])):
            G = set(l[i]).difference(m1)
            break
    m2 = set(l[1]).union(set(G))
    for i in range(3,6):
        if m2.issubset(set(l[i])):
            D = set(l[i]).difference(m2)
            break
    B = set(l[2]).difference(set(l[0]).union(D))
    E = set(l[9]).difference(set(l[2]).union(A).union(G))
    for i in range(6,9):
        if set(l[i]).union(set(l[0])) == set(l[9]):
            C = set(l[9]).difference(set(l[i]))
            break
    F = set(l[0]).difference(C)
    return(A,B,C,D,E,F,G)

sum = 0
for line in lines:
    #print(line)
    A,B,C,D,E,F,G = signals(line[0])
    x = 0
    for s in line[1]:
        x *= 10
        if len(s) == 2:
            x+=1
        elif set(s) == A.union(C).union(D).union(E).union(G):
            x+=2
        elif set(s) == A.union(C).union(D).union(F).union(G):
            x+=3
        elif len(s) == 4:
            x+=4
        elif set(s) == A.union(B).union(D).union(F).union(G):
            x+=5
        elif set(s) == A.union(B).union(D).union(E).union(F).union(G):
            x+=6
        elif len(s) == 3:
            x+=7
        elif len(s) == 7:
            x+=8
        elif set(s) == A.union(B).union(C).union(D).union(F).union(G):
            x+=9
    #print(x)
    sum+=x

print(sum)
"""
