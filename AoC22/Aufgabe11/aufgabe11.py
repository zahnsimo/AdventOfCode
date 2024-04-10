data = open("input.txt")
notes = data.read().splitlines()

def parse(notes):
    monkeys = {}
    n = (len(notes)+1)//7
    for i in range(0,n):
        monkeys.update({i:{}})
        items = [int(x) for x in notes[7*i+1].strip("Starting items:").split(",")]
        monkeys[i].update({"items": items})
        operation = notes[7*i+2].split(" ")
        v1 = operation[5]
        v2 = operation[7]
        op = operation[6]
        monkeys[i].update({"op" : {"v1" : v1 , "v2" : v2 , "op" : op}})
        mod = int(notes[7*i+3].strip("Test: divisible by"))
        monkeys[i].update({"test" : mod})
        tr = int(notes[7*i+4].strip("If true: throw to monkey"))
        monkeys[i].update({"ifT": tr})
        f = int(notes[7*i+5].strip("If false: throw to monkey"))
        monkeys[i].update({"ifF": f})
        monkeys[i].update({"nop": 0})
    return(monkeys)

def operation(v1,v2,op,x):
    if v1 == "old":
        v1 = x
    else:
        v1 = int(v1)
    if v2 == "old":
        v2 = x
    else:
        v2 = int(v2)
    if op == "+":
        return(v1+v2)
    elif op == "-":
        return(v1-v2)
    elif op == "*":
        return(v1*v2)
monkeys = parse(notes)
M = 1
for i in range(0,len(monkeys)):
    M*= monkeys[i]["test"]
for k in range(0,10000):
    for i in range(0,len(monkeys)):
        v1 = monkeys[i]["op"]["v1"]
        v2 = monkeys[i]["op"]["v2"]
        op = monkeys[i]["op"]["op"]
        mod = monkeys[i]["test"]
        m_t = monkeys[i]["ifT"]
        m_f = monkeys[i]["ifF"]
        monkeys[i]["nop"] += len(monkeys[i]["items"])
        while monkeys[i]["items"] != []:
            x = monkeys[i]["items"].pop(0) % M
            x = operation(v1,v2,op,x)
            if (x%mod == 0):
                monkeys[m_t]["items"].append(x)
            else:
                monkeys[m_f]["items"].append(x)
    #print("Round",k)
    #for i in range(0,len(monkeys)):
    #    print("Monkey",i, monkeys[i]["items"])

for i in range(0,len(monkeys)):
    print("Monkey",i,monkeys[i]["nop"])
print(monkeys[3]["nop"] * monkeys[5]["nop"])

#print(parse(notes))
