data = open("input6.txt")
fish = [int(x) for x in data.read().split(",")]
count = [fish.count(i) for i in range(9)]

def step(l):
    new = l.count(0)
    l_new = [(x-1)%7 if x<7 else x-1 for x in l] + [8 for i in range(new)]
    #print(l_new)
    return l_new

def step_alt(c):
    c_new = [c[(i+1)%9] if i != 6  else c[7]+c[0] for i in range(9)]
    return c_new

for i in range(256):
    #print(count, sum(count))
    count = step_alt(count)

print(count, sum(count))



    
