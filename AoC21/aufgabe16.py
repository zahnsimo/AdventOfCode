import math
data = open("input16.txt")
packet_hex = data.read().replace("\n","")
#packet_hex = "9C0141080250320F1802104A08"
packet_int = int(packet_hex,16)
packet_bin = str(bin(packet_int))[2:].zfill(4*len(packet_hex))


def parse(p,i): #never change i in fct
    v = int(p[i:i+3],2)
    t = int(p[i+3:i+6],2)
    if t == 4:
        j = i+6
        s = ""
        while p[j] == "1":
            s += p[j+1:j+5]
            j+=5
        s+=p[j+1:j+5]
        n = int(s,2)
        packet = {"v" : v , "t" : t , "val" : n}
        return(packet,j+5)
    else:
        packet = {"v" : v, "t" : t , "sub" : []}
        if p[i+6] == "0":
            l = int(p[i+7:i+22],2)
            j = i+22
            while j < i+22+l:
                sub,j = parse(p,j)
                packet["sub"].append(sub)
            return(packet,j)
        else:
            l = int(p[i+7:i+18],2)
            j = i+18
            total = 0
            while total < l:
                sub,j = parse(p,j)
                packet["sub"].append(sub)
                total +=1
            return(packet,j)
            
def add_version(packet):
    if "sub" in packet.keys():
        total = packet["v"]
        for sub in packet["sub"]:
            total += add_version(sub)
        return total
    else:
        return packet["v"]
    
def value(packet):
    if packet["t"] == 0:
        return sum([value(sub) for sub in packet["sub"]])
    elif packet["t"] == 1:
        return math.prod([value(sub) for sub in packet["sub"]])
    elif packet["t"] == 2:
        return min([value(sub) for sub in packet["sub"]])
    elif packet["t"] == 3:
        return max([value(sub) for sub in packet["sub"]])  
    elif packet["t"] == 4:
        return packet["val"]
    elif packet["t"] == 5:
        return int(value(packet["sub"][0]) > value(packet["sub"][1]))
    elif packet["t"] == 6:
        return int(value(packet["sub"][0]) < value(packet["sub"][1]))
    elif packet["t"] == 7:
        return int(value(packet["sub"][0]) == value(packet["sub"][1]))

packet,j = parse(packet_bin,0)
print(add_version(packet))
print(value(packet))
