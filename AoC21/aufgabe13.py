data = open("input13.txt")
lines = data.read().split("\n\n")

coords = [(int(x),int(y)) for (x,y) in [line.split(",") for line in lines[0].splitlines()]]
print(coords[1])

inst = [(s.strip("fold along "), int(x)) for (s,x) in [line.split("=") for line in lines[1].splitlines()]]
print(inst[0])

def xfold(coords, x0):
    coords_new = []
    for c in coords:
        (x,y) = c[0],c[1]
        if x > x0:
            x = 2*x0 - x
        coords_new.append((x,y))
    return coords_new

def yfold(coords, y0):
    coords_new = []
    for c in coords:
        (x,y) = c[0],c[1]
        if y > y0:
            y = 2*y0 - y
        coords_new.append((x,y))
    return coords_new

print(len(set(coords)))
for p in inst:
    d,dd = p[0],p[1]
    if d == "x":
        coords = xfold(coords,dd)
    elif d == "y":
        coords = yfold(coords,dd)
    print(len(set(coords)))

x_min,x_max = min(c[0] for c in coords), max(c[0] for c in coords)
y_min,y_max = min(c[1] for c in coords), max(c[1] for c in coords)
for y in range(y_min,y_max+1):
    s = ""
    for x in range(x_min,x_max+1):
        if (x,y) in coords:
            s +="#"
        else:
            s +=" "
    print(s)

