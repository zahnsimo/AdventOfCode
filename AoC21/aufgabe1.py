data = open("""input1.txt""")
lines = [int(x) for x in data.read().splitlines()]

print(sum([lines[i]>lines[i-1] for i in range(1,len(lines))]))

print(sum([lines[i+2]>lines[i-1] for i in range(1,len(lines)-2)]))
