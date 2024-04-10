data = open("input.txt")
text = data.read()


def find_marker(text):
    cmp = 0
    start = 0
    end = 0
    while(end - start < 3):
        end = end + 1
        for j in range(start,end):
            cmp+=1
            if text[j] == text[end]:
                start = j+1
    return (end+1,cmp)

def find_marker2(text):
    cmp = 0
    start = 0
    end = 1
    while(end - start < 4):
        j = end-1
        while (j >= start and text[j] != text[end]):
            cmp+=1
            j = j-1
        start = j+1
        end = end + 1
    return (end,cmp)

def find_msg(text):
    cmp = 0
    start = 0
    end = 0
    while(end - start < 13):
        end = end + 1
        for j in range(start,end):
            cmp+=1
            if text[j] == text[end]:
                start = j+1
    return (end+1,cmp)

def find_msg2(text):
    cmp = 0
    start = 0
    end = 1
    while(end - start < 14):
        j = end-1
        while (j >= start and text[j] != text[end]):
            cmp+=1
            j = j-1
        start = j+1
        end = end + 1
    return (end,cmp)

text1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
text2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
text3 = "nppdvjthqldpwncqszvftbrmjlhg"
text4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
text5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

print(find_marker(text1))
print(find_marker(text2))
print(find_marker(text3))
print(find_marker(text4))
print(find_marker(text5))
print(find_marker("aabcdef"))

print("alternativ:")
print(find_marker2(text1))
print(find_marker2(text2))
print(find_marker2(text3))
print(find_marker2(text4))
print(find_marker2(text5))
print(find_marker2("aabcdef"))

print(find_marker(text))
print(find_marker2(text))
print(find_msg(text))
print(find_msg2(text))

