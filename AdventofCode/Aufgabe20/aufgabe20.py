data = open("input.txt")
lines = [int(x)*811589153 for x in data.read().splitlines()]
lines = [[int(lines[i]) , i] for i in range(0,len(lines))]
 
n = len(lines)

#print([x[0] for x in lines])
for k in range(10):
    for i in range(n):
        j = 0
        while lines[j][1] !=i:
            j+=1
        x = lines[j][0]
        del lines[j]
        new_i = (x+j) %(n-1)
        if new_i == 0 and x < 0:
            new_i = len(lines)
        lines.insert(new_i,[x,i])
        #print(lines)
    #print([x[0] for x in lines])
   
mixed = [x[0] for x in lines]
j = mixed.index(0)
print(lines[(j+1000)%n][0] + lines[(j+2000)%n][0] + lines[(j+3000)%n][0])
