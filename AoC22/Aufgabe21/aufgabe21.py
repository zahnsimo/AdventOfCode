data = open("input.txt")
lines = [line.split(" ") for line in """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".splitlines()]
#lines = [line.split(" ") for line in data.read().splitlines()]

def parse(lines):    
    numbers = {}
    operations = []
    for line in lines:
        name = line[0].removesuffix(":")
        if name == "root":
            name1 = line[1]
            name2 = line[3]
        elif name != "humn":
            if len(line) == 2:
                n = int(line[1])
                numbers.update({name : n})
            else:
                v1, op, v2 = line[1:]
                operations.append([name ,v1,op,v2])
    return(numbers,operations , name1,name2)

def do_op(x,y,op):
    if op == "+":
        return x+y
    elif op == "-":
        return x-y
    elif op == "*":
        return x*y
    elif op == "/":
        return x//y
rev_op = {"+":"-" , "-":"+" , "*":"/" , "/": "*"}
def reverse_op(z,y,op,i):
    if i == 2:
        rev = rev_op[op]
        return do_op(z,y,rev)
    elif i == 1 and (op == "+" or op == "*"):
        rev = rev_op[op]
        return do_op(z,y,rev)
    else:
        return do_op(y,z,op)

numbers,operations , name1,name2 = parse(lines)

new = ""
while len(operations)>0:
    cur = operations.pop(0)
    name,v1,op,v2 = cur
    if v1 in numbers and v2 in numbers:
        x = numbers[v1]
        y = numbers[v2]
        z = do_op(x,y,op)
        numbers.update({name:z})
        if name == name1:
            new = name2
            new_val = z
            #print("new:",new,new_val)
            numbers.update({name2:z})
        elif name == name2:
            new = name1
            new_val = z
            #print("new:",new,new_val)
            numbers.update({name1:z})
    elif v1 in numbers and name == new:
        x = numbers[v1]
        y = reverse_op(new_val,x,op,1)
        new = v2
        new_val = y
        numbers.update({v2:y})
        #print("new:", new , new_val)
    elif v2 in numbers and name == new:
        y = numbers[v2]
        x = reverse_op(new_val,y,op,2)
        new = v1
        new_val = x
        numbers.update({v1:x})
        #print("new:",new,new_val)
    else:
        operations.append(cur)

print(numbers["humn"])


"""
while len(operations)>0:
    cur = operations.pop(0)
    name,v1,op,v2 = cur
    if v1 in numbers and v2 in numbers:
        x = numbers[v1]
        y = numbers[v2]
        z = do_op(x,y,op)
        numbers.update({name:z})
    else:
        operations.append(cur)

print(numbers["root"])
"""
