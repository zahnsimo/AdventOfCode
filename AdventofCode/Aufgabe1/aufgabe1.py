data = open("input.txt")
[max1,max2,max3] = [0,0,0]


lines = data.readlines()
s = 0
for line in lines:
    if (line.strip()):
        s = s + int(line)
    else:
        if s > max1:
            [max1,max2,max3] = [s,max1,max2]
        elif s > max2:
            [max1,max2,max3] = [max1,s,max2]
        elif s > max3:
            [max1,max2,max3] = [max1,max2,s]
        s = 0
print([max1,max2,max3])
total = max1 + max2 + max3
print(total)
