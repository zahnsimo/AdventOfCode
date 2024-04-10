data = open("input24.txt")
programm = [line.split(" ") for line in data.read().splitlines()]

def run(programm, x):
    s = str(x)
    i = 0 #pointer for next input value of number x
    var = [0,0,0,0,0] #stores values of w,x,y,z, ord-118 and maybe some int-input
    for line in programm:
        #print(var[1:])
        a = line[1]
        b = line[-1]
        if not (b in {"w","x","y","z"}):
            var[0] = int(b)
            b = "v"
        if line[0] == "inp":
            var[ord(a)-118] = int(s[i])
            i+=1
        elif line[0] == "add":
            var[ord(a)-118] += var[ord(b)-118]
        elif line[0] == "mul":
            var[ord(a)-118] *= var[ord(b)-118]
        elif line[0] == "div":
            var[ord(a)-118] //= var[ord(b)-118]
        elif line[0] == "mod":
            var[ord(a)-118] = var[ord(a)-118]%var[ord(b)-118]
        elif line[0] == "eql":
            var[ord(a)-118] = int(var[ord(a)-118] == var[ord(b)-118])
    return var[1:]

#print(sum([line[0] == "inp" for line in programm]))
print([i for i in range(len(programm)-18) if programm[i][0] != programm[i+18][0]])
print([i for i in range(len(programm)-18) if programm[i][1] != programm[i+18][1]])
print([programm[i] for i in range(len(programm)-18) if programm[i][-1] != programm[i+18][-1]])
print(sum([[1] == "w" for line in programm]))
print(run(programm[-18:],4))
"""
x = 10**14-1
while x >= 10**13:
    if not "0" in str(x):
        var = run(programm,x)
        if var[-1] == 0:
            print(x)
            break
    x-=1
    if (x+1)%10**4 == 0:
        print(x, var)
print(run(programm,11))
"""
