data = open("input4.txt")
lines = data.read().splitlines()

numbers = [int(x) for x in lines[0].split(",")]
n = len(lines)//6
boards = [[[int(x) for x in lines[j].split()] for j in range(6*i+2,6*i+7)] for i in range(n)]

def check(board):
    k,l = len(board),len(board[0])
    if (any([all([board[i][j]==-1 for j in range(l)]) for i in range(k)])
        or any([all([board[i][j]==-1 for i in range(k)])for j in range(l)])):
        #or all([board[i][i]==-1 for i in range(k)])
        #or all([board[k-i-1][i]==-1 for i in range(k)])):
        return sum([board[i][j] for i in range(k) for j in range(l) if board[i][j] >=0])
    else:
        return -1


wins = set()
for x in numbers:
    for h in range(n):
        b = boards[h]
        k,l = len(b),len(b[0])
        b[:] = [[-1 if b[i][j]==x else b[i][j] for j in range(l)] for i in range(k)]
        c = check(b)
        if c>=0:
            wins.add(h)
            if len(wins) == n:
                print(b , h , x , c , c*x)
                break
            
    else:
        continue
    break
