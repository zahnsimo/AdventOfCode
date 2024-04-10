data = open("input3.txt")
lines = data.read().splitlines()

n = len(lines)
k = len(lines[0])

gamma = sum(2**(k-j-1)* (sum(int(lines[i][j]) for i in range(n))/n >= 0.5) for j in range(k))
epsilon = 2**k - 1- gamma
print(gamma,epsilon, gamma*epsilon)

def oxy(lines):
    n = len(lines)
    k = len(lines[0])
    j = 0
    while len(lines)> 1:
        bit = sum(int(lines[i][j]) for i in range(n))/n >= 0.5
        lines = [line for line in lines if int(line[j])==bit]
        n = len(lines)
        j+=1
    line = lines[0]
    return sum(2**(k-j-1)*int(line[j]) for j in range(k))

def co2(lines):
    n = len(lines)
    k = len(lines[0])
    j = 0
    while len(lines)> 1:
        bit = sum(int(lines[i][j]) for i in range(n))/n < 0.5
        lines = [line for line in lines if int(line[j])==bit]
        n = len(lines)
        j+=1
    line = lines[0]
    return sum(2**(k-j-1)*int(line[j]) for j in range(k))


print(oxy(lines)*co2(lines))
