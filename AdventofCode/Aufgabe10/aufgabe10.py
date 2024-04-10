data = open("input.txt")
lines = [line.split(" ") for line in data.read().splitlines()]

c = 0
x = 1
s = 0
image = ""
for line in lines:
    if line[0] == "addx":
        if (c-x)%40 == 39 or (c-x)%40 == 0:
            image += "##"
        elif (c-x)%40 == 1:
            image +="# "
        elif (c-x)%40 == 38:
            image += " #"
        else:
            image += "  "
        c+=2
        if c%40 == 20:
            s+= c*x
        elif c%40 == 21:
            s+= (c-1)*x
        x+= int(line[1])
    if line[0] == "noop":
        if (c-x)%40 == 0 or (c-x)% 40 == 1 or (c-x)% 40 == 39:
            image += "#"
        else:
            image += ' '
        c+=1
        if c%40 == 20:
            s+= c*x
print(s)
    
print(image[0:39])
print(image[40:79])
print(image[80:119])
print(image[120:159])
print(image[160:199])
print(image[200:239])
