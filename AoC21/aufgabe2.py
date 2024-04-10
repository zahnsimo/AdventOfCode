data = open("""input2.txt""")
lines = [line.split(" ") for line in data.read().splitlines()]

x = 0
y = 0
aim = 0
for line in lines:
    if line[0] == "forward":
        x+= int(line[1])
        y+= aim * int(line[1])
    elif line[0] == "down":
        aim+= int(line[1])
    elif line[0] == "up":
        aim-= int(line[1])
    else:
        print("error")
        print(line)

print(x*y)
