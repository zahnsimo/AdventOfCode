data = open("input.txt")
lines = data.readlines()

t = 0
for line in lines:
    [elf1,elf2] = line.split(",")
    [s1,e1] = elf1.split("-")
    [s2,e2] = elf2.split("-")
    if int(s1) >= int(s2) and int(e1) <= int(e2):
        t = t + 1
    elif int(s1) <= int(s2) and int(e1) >= int(e2):
        t = t + 1

print(t)

t2 = 0
for line in lines:
    [elf1,elf2] = line.split(",")
    [s1,e1] = elf1.split("-")
    [s2,e2] = elf2.split("-")
    if not(int(e2) < int(s1) or int(e1) < int(s2)):
        t2 = t2 + 1

print(t2)
