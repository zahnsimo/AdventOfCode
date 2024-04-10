data = open("input14.txt")
lines = data.read().splitlines()

s = lines[0]
rules = [line.split(" -> ")for line in lines[2:]]
letters = set([x for x in s]+[r[1] for r in rules])
pairs = dict([(x+y,0) for x in letters for y in letters])
start = s[0]
end = s[-1]
for i in range(len(s)-1):
    pairs[s[i:i+2]] = pairs[s[i:i+2]] + 1
def step_alt(pairs):
    pairs_new = dict([(x+y,0) for x in letters for y in letters])
    for p in pairs:
        for r in rules:
             if p == r[0]:
                 pairs_new[p[0]+r[1]] += pairs[p]
                 pairs_new[r[1]+p[1]] += pairs[p]
                 break
    return pairs_new

def count_letters(pairs):
    c = {}
    for x in letters:
        s = sum([pairs[x+y] for y in letters] + [pairs[y+x] for y in letters])
        if x == start or x == end:
            s+=1
        if s%2 == 0:
            c.update({x:s//2})
        else:
            print("whoops")
            break
    return c

for i in range(40):
    pairs = step_alt(pairs)
    c = count_letters(pairs)
print(max(c.values()),min(c.values()) , max(c.values()) - min(c.values()))
"""
def step(s):
    s_new = ""
    for i in range(len(s)-1):
        s_new += s[i]
        for r in rules:
            if s[i:i+2] == r[0]:
                s_new += r[1]
                break
    s_new += s[-1]
    return s_new

for i in range(40):
    #print(s)
    print(i,len(s))
    s = step(s)
#print(s)

c = []
for x in letters:
    c.append(s.count(x))
print(max(c),min(c), max(c)-min(c))
"""
