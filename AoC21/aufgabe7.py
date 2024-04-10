data = open("input7.txt")
crabs = [int(x) for x in data.read().split(",")]

x_min, x_max = min(crabs), max(crabs)

def tr(x):
    return 0.5*x*(x+1)

cost = sum([tr(x_max-y) for y in crabs])
for x in range(x_min,x_max+1):
    cost_new = sum([tr(abs(x-y)) for y in crabs])
    if cost_new < cost:
        cost = cost_new
    #print(cost_new)
print(cost)
        
    

