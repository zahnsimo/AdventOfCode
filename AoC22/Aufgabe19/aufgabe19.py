import numpy as np
data = open("input.txt")
#lines = data.read().splitlines()
lines = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".splitlines()

def parse(lines):
    bp = []
    for line in lines:
        words = line.split(" ")
        ore_costs = [int(words[6]),0,0,0]
        clay_costs = [int(words[12]),0,0,0]
        obs_costs = [int(words[18]),int(words[21]),0,0]
        geode_costs = [int(words[27]),0,int(words[30]),0]
        bp.append([ore_costs,clay_costs,obs_costs,geode_costs])
    return bp
print(parse(lines))

bp = parse(lines)
costs = bp[0]

def quality(costs):
    m = 0
    #ore_costs , clay_costs , obs_costs , geode_costs = costs
    robots = []
    material = []
    s = []
    for i in range(25):
        robots.append([1,0,0,0])
        material.append([0,0,0,0])
        s.append(-1)
    t = 0
    c=0
    more_options = False
    while c < 2 and sum(s)<24:
        t+=1
        #while len(material) <t+1:
        #    material.append([0,0,0,0])
        #while len(robots) <t+1:
        #    robots.append([0,0,0,0])
        #print(t,robots[t],material[t-1],material[t])
        material[t] = [robots[t-1][i] + material[t-1][i] for i in range(4)]
        print(t,material[t],robots[t])
        if t == 24:
            c+=1
            m = max(m,material[24][3])
            print("hi:",m)
            while t >=1 and s[t-1]<4:
                t-=1
        #if len(s)<t+1:
        #    s.append(-1)
        next = s[t] + 1
        while next < 4 and not all(costs[next][i] <= material[t][i] for i in range(4)):
            next +=1
        if next < 4:
            robots[t+1][next]+=1
        #if t == 24:
        #    print("hi")
        #    m = max(m, material[t][3])
        #    while t >= 0 and s[t] < 4:
        #        t-=1
    return m

print(quality(costs))
     
        
