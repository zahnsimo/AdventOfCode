data = open("input.txt")
lines = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""".splitlines()
lines = data.read().splitlines()

def snafu_to_dec(s):
    total = 0
    n = len(s)
    for i in range(n):
        a = s[i]
        if a == "=":
            x = -2
        elif a == "-":
            x = -1
        else:
            x = int(a)
        total += x * (5**(n-i-1))
    return total

def qr(n):
    q = (n+2)//5
    r = (n+2)%5 - 2
    return(q,r)

def dec_to_snafu(n):
    s = ""
    while n > 0:
        q,r = qr(n)
        if r == -2:
            a = "="
        elif r == -1:
            a = "-"
        else:
            a = str(r)
        s = a+s
        n = q
    return s
print(dec_to_snafu(sum(snafu_to_dec(s) for s in lines)))
#for s in lines:
#    n = snafu_to_dec(s)
#    print(s,n,dec_to_snafu(n))
#    print(s == dec_to_snafu(n))
    
#print(snafu_to_dec(s))
#print(qr(8))
#print(dec_to_snafu(12345))
