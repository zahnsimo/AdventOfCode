data = open("input.txt")
lines = data.readlines()
total = 0

for line in lines:
    opp = ord(line[0]) - 64
    mine = ord(line[2]) - 64 - 23
    score = ((mine - opp + 1)%3) * 3 + mine
    total = total + score

print(total)

total2 = 0
for line in lines:
    opp = ord(line[0]) - 64
    outcome = ord(line[2]) - 64 - 24
    mine = (opp + outcome - 2) % 3 + 1
    score = outcome * 3 + mine
    total2 = total2 + score

print(total2)
