data = open("input12.txt")
lines = data.read().splitlines()

def parse(lines):
    nodes = {}
    for line in lines:
        x,y = line.split("-")
        if not x in nodes:
            up = ord(x[0]) in range(65,91)
            nodes.update({x : {"adj" : set([y]) , "up" : up}})
        else:
            nodes[x]["adj"].add(y)
        if not y in nodes:
            up = ord(y[0]) in range(65,91)
            nodes.update({y : {"adj" : set([x]) , "up" : up}})
        else:
            nodes[y]["adj"].add(x)            
    return nodes
nodes = parse(lines)

comp = []
inc = [[x] for x in nodes["start"]["adj"]] #initialisiere liste incomplete paths
while len(inc) > 0:
    p = inc.pop(0)
    x = p[-1]
    for y in nodes[x]["adj"]:
        p1 = p.copy()
        if y == "end":
            p1.append(y)
            comp.append(p1)
        elif y != "end" and y != "start" and (nodes[y]["up"] or not y in p1 or all(nodes[z]["up"] or p.count(z)<=1 for z in p)):
            p1.append(y)
            inc.append(p1)
print(len(comp))


            
