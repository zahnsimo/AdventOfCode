data = open("input.txt")
lines = [[s.strip("Sensor at closest beacon is at") for s in line.split(":")] for line in data.read().splitlines()]
coords = [[[int(r[2:]) for r in t.split(", ")] for t in s] for s in lines]

x_min,x_max = 0,4000000
y_min,y_max = 0,4000000

def dist(x0,y0,x1,y1):
    return(abs(x0-x1) + abs(y0-y1))

def test_line(coords,y_test):
    intervalle = []
    pos = set()
    for c in coords:
        x0,y0,x1,y1 = c[0][0],c[0][1],c[1][0],c[1][1]
        d = dist(x0,y0,x1,y1)
        if d-abs(y_test-y0) >=0:
            intervalle.append((x0-d+abs(y_test-y0),x0+d-abs(y_test-y0)))
        if y1 == y_test:
            pos.add(x1)
    intervalle = sorted(intervalle)
    l = 0
    x_l,x_r = intervalle[0]
    print("Untere Grenze:", x_l)
    for i in range(0,len(intervalle)-1):
        if x_r>=intervalle[i+1][0]-1:
            if x_r<intervalle[i+1][1]:
                x_r = intervalle[i+1][1]
        else:
            l += x_r-x_l + 1
            print("Lücke von", x_r+1 ,"bis", intervalle[i+1][0]-1)
            x_l,x_r = intervalle[i+1]
    l += x_r-x_l+1
    print("Obere Grenze:", x_r)
    return(l - len(pos))

def find_beacon(coords):
    for y in range(y_min,y_max+1):
        intervalle = []
        for c in coords:
            x0,y0,x1,y1 = c[0][0],c[0][1],c[1][0],c[1][1]
            d = dist(x0,y0,x1,y1)
            if d-abs(y-y0) >=0:
                intervalle.append((x0-d+abs(y-y0),x0+d-abs(y-y0)))
        intervalle = sorted(intervalle)
        x_l,x_r = intervalle[0]
        for i in range(0,len(intervalle)-1):
            if x_r>=intervalle[i+1][0]-1:
                if x_r<intervalle[i+1][1]:
                    x_r = intervalle[i+1][1]
            else:
                return(4000000*(x_r+1)+y)
        if(y%10000 == 0):
            print(y)
y_test = 2000000
print(test_line(coords,y_test))
#print(find_beacon(coords))
