import numpy as np
data = open("input10.txt")
lines = data.read().splitlines()

right = {"(" : ")" , "[" : "]" , "{" : "}" , "<" : ">"}
sc = {")" : 3 , "]" : 57 , "}" : 1197 , ">" : 25137}
pt = {")" : 1 , "]" : 2 , "}" : 3 , ">" : 4}

def compl_score(line):
    s = []
    for x in line:
        if x in right.keys():
            s.append(x)
        elif x in right.values():
            if len(s) == 0:
                return 0
            elif x == right[s[-1]]:
                s.pop(-1)
            else:
                return 0
    score = 0
    while len(s) != 0:
        score *= 5
        y = s.pop(-1)
        score += pt[right[y]]
    return score
        

def score(line):
    score = 0
    s = []
    for x in line:
        if x in right.keys():
            s.append(x)
        elif x in right.values():
            if len(s) == 0:
                return sc[x] #?
            if x == right[s[-1]]:
                s.pop(-1)
            else:
                return sc[x]
    return score

#for line in lines:
#    print(score(line))

print(sum([score(line) for line in lines]))

#for line in lines:
#    print(compl_score(line))
print(np.median([compl_score(line) for line in lines if compl_score(line) != 0]))
