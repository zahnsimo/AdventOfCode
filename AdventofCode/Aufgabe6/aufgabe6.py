data = open("input.txt")
text = data.read()

def marker(i, text):
    return (text[i] != text[i+1] and text[i] != text[i+2]
            and text[i] != text[i+3] and text[i+1] != text[i+2]
            and text[i+1] != text[i+3] and text[i+2] != text[i+3])



def find_marker(text):
    i = 0
    while not (marker(i,text)):
        i = i+1
    return i+4



def msg_marker(i,text):
    ans = True
    for j in range(0,13):
        for k in range(j+1,14):
            ans = ans and (text[i+j] != text[i+k])
    return ans

def find_msg(text):
    i = 0
    while not msg_marker(i,text):
        i = i+1
    return i+14

#text = "bvwbjplbgvbhsrlpgdmjqwftvncz"
print(find_marker(text))

print(find_msg(text))






