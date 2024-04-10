import json
numbers = [json.loads(line) for line in """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]""".splitlines()]

#checks magnitude:
numbers2 = [json.loads(line) for line in """[[1,2],[[3,4],5]]
[[[[0,7],4],[[7,8],[6,0]]],[8,1]]
[[[[1,1],[2,2]],[3,3]],[4,4]]
[[[[3,0],[5,3]],[4,4]],[5,5]]
[[[[5,0],[7,4]],[5,5]],[6,6]]
[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]""".splitlines()]

def add(n1,n2):
    return [n1,n2]

def split(x):
    return [x//2,x-x//2]


def reduce(number):
    if type(number) == int:
        return number
    else:
        pointer = [0]
        pass
        #here!
        

def magnitude(number):
    if type(number) == int:
        return number
    else:
        l = number[0]
        r = number[1]
        return 3*magnitude(l)+2*magnitude(r)
    
#print([magnitude(number) for number in numbers2])
