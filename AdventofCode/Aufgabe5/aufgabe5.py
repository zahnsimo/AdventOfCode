import re

data = open("input.txt")
lines = data.readlines()
n = len(lines[0]) // 4
stacks = []

for i in range(0,n):
    stack = []
    l = 0
    while lines[l][0] == "[":
        k = 4*i + 1
        if lines[l][k] != " ":
            stack.append(lines[l][4*i+1])
        l = l+1
    stacks.append(stack)


for i in range(l+2, len(lines)):
    line = lines[i]
    line_split = re.split(r"move|from|to" , line)
    a = int(line_split[1])
    b = int(line_split[2])
    c = int(line_split[3])
    for j in range(0, a):
        item = stacks[b-1].pop(0)
        stacks[c-1].insert(0,item)

answer = ""
for i in range(0,n):
    answer = answer + stacks[i][0]

print(answer)
