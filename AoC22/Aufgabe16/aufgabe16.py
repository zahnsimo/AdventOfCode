import numpy as np
data = open("input.txt")
lines = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()
lines = data.read().splitlines()

def parse(lines):
    valves = {}
    for line in lines:
        A,B = line.split(";")
        A = A.split(" ")
        name = A[1]
        rate = int(A[4].removeprefix("rate="))
        adj = B.strip(" tunnels lead to valves ").split(", ")
        valves.update({name:{"rate" : rate , "adj" : adj}})
    return valves


def dist(v,V):
    ind = V.index(v) if v in V else -1
    n = len(V)
    adjl = -np.ones(n , dtype = int)
    if ind >= 0:
        adjl[ind] = 0
    i = 1
    s = valves[v]["adj"]
    check = []
    while len(s)>0:
        new_s = []
        for w in s:
            if w in V:
                ind_w = V.index(w)
                if adjl[ind_w] == -1:
                    adjl[ind_w] = i
                    new_s += [x for x in valves[w]["adj"] if x not in check]
                elif adjl[ind_w] > i:
                    adjl[ind_w] = i                   
            else:
                check.append(w)
                new_s += [x for x in valves[w]["adj"] if x not in check]
        s = new_s
        i+=1
    return adjl
      

def run(valves):
    V = [v for v in valves if valves[v]["rate"] != 0]
    paths_inc = []
    n = len(V)
    adjA = dist("AA",V)
    adjL = [dist(V[i],V) for i in range(n)]
    for i in range(n):
        t = adjA[i]
        v = V[i]
        p = valves[v]["rate"] * (30 - t - 1)
        paths_inc.append({"n": [v] , "t" : t+1 , "p" : p})
    print(paths_inc)
    max_p = 0
    while len(paths_inc)>0:
        curr = paths_inc.pop(0)
        last_node = curr["n"][-1]
        last_ind = V.index(last_node)
        for i in range(n):
            v = V[i]
            if not v in curr["n"]:
                new_path = {}
                nodes = curr["n"].copy()
                nodes.append(v)
                t = curr["t"] + adjL[last_ind][i]
                p = curr["p"] + valves[v]["rate"] * (30 - t - 1)
                new_path = {"n" : nodes, "t" : t+1 , "p": p}
                if t < 30 and len(nodes) < n:
                    paths_inc.append(new_path)
                elif p > max_p:
                    max_p = p
                    print(p,nodes)
                
valves = parse(lines)
run(valves)        
