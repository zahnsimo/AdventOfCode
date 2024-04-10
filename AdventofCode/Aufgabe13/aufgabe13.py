import json
import math
data = open("input.txt")
lines =[json.loads(line) for line in data.read().splitlines() if line]

def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def compare(l1,l2):
    if l1 == l2:
        return 0
    if type(l1)==int and type(l2)==int:
        return(sign(l2-l1))
    if type(l1)==list and type(l2)==int:
        return(compare(l1,[l2]))
    if type(l1)==int and type(l2)==list:
        return(compare([l1],l2))
    if type(l1)==list and type(l2)==list:
        if len(l1)==0:
            return 1
        elif len(l2)==0:
            return -1
        else:
            n = min(len(l1),len(l2))
            i = 0
            while(i < n and compare(l1[i],l2[i]) == 0):
                i+=1
            if i == n:
                return sign(len(l2)- len(l1))
            else:
                return(compare(l1[i],l2[i]))

print(sum((i+1) * max(compare(lines[2*i],lines[2*i+1]),0) for i in range(0,n)))

i1 = sum(max(compare(line,[[2]]),0) for line in lines) + 1
i2 = sum(max(compare(line,[[6]]),0) for line in lines) + 2
print(i1,i2,i1*i2)


