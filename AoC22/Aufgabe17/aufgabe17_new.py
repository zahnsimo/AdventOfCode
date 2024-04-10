import numpy as np
data = open("input.txt")
#directions = data.read().replace("\n","")
directions = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

shapes = [[[0,0,0,0] , [0,0,0,0]],
          [[1,0,1] , [0,2,0]],
          [[0,0,0] , [0,0,2]],
          [[0] , [3]] ,
          [[0,0] , [1,1]]] #first list: lower shape, second: upper shape

h = 0
t = 0
h_max = [0,0,0,0,0,0,0]
delta = 0
for r in range(0,10000001):
    shape = shapes[r%5][0]
    w = len(shape)
    x_l = 2
    y_l = h+4
    #print(t,x_l,shape)
    while (t%2) == 0 or all(y_l + shape[x] > h_max[x+x_l]+1 for x in range(0,w)) :
        if t%2 == 1:
            y_l -=1
        else:
            if directions[(t//2)%len(directions)] == ">" and x_l + w <7:
                d = 1
            elif directions[(t//2)%len(directions)] == "<" and x_l >0:
                d = -1
            #if r%5 != 1 and y_l > h_max[x_l+w*(d+1)//2]:
            #    x_l+=d
            #elif r%5 ==1 and y_l+1 > h_max[x_l+1 +d] and y_l > h_max[x_l + d]:
            #    x_l+=d
            if all(y_l + shape[x]>h_max[x+x_l+d] for x in range(0,w)):
                x_l +=d
            d = 0
        t+=1
        #print(t,x_l,shape)
    t+=1
    upper_shape = shapes[r%5][1]
    for i in range(0,w):
        h_max[x_l+i] = y_l + shape[i] + upper_shape[i]
    h = max(h_max)
    h_min = min(h_max)
    if h_min >0:
        h_max = [y-h_min for y in h_max]
        h -= h_min
    delta+=h_min
    if (t//2)%len(directions) == 0:
        print("r:" , r , "h_max:" , h_max , "delta:",delta,"\n\n")
    if r%10000 == 0:
        print("r:" , r , "h_max:" , h_max , "delta:",delta)
    #if r == 2021:
    #    print("r:" , r , "h_max:" , h_max, "delta:", delta)



