data = open("input20.txt")
alg,image = data.read().split("\n\n")


alg = alg.replace("\n", "")
print(len(alg),alg.count("#"),alg.count("."), list(set(alg)))

def enhance(im,bg):
    im = im.splitlines()
    m = len(im)
    n = len(im[0])
    im_new = ""
    for i in range(-1,m+1):
        line = ""
        for j in range(-1,n+1):
            adj = [[i-1,j-1],[i-1,j],[i-1,j+1],
                    [i,j-1],[i,j],[i,j+1],
                    [i+1,j-1],[i+1,j],[i+1,j+1]]
            index = 0
            for p in adj:
                index *=2
                x,y = p[0],p[1]
                if (x < 0 or x > m-1 or y < 0 or y > n-1):
                    index += bg
                elif im[x][y]=="#":
                    index+=1
            line += alg[index]
        im_new += line + "\n"
    if bg==1:
        bg_new = (alg[-1] == "#")
    else:
        bg_new = (alg[0] == "#")
    return im_new,bg_new

bg = 0
for i in range(50):
    image,bg = enhance(image,bg)

print(image.count("#") , bg)
