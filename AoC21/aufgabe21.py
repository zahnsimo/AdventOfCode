import numpy as np
data = open("input21.txt")
starts = [int(x[1]) for x in [line.split(":") for line in data.read().splitlines()]]
print(starts)

def round(space,dice):
    space_new = (space + 3*dice + 6) % 10
    if space_new == 0:
        space_new = 10
    dice_new = dice + 3
    return space_new,dice_new


score = [0,0] #starting score
dice = 0 #starting dice
position = starts.copy() #starting positions
player = 0 #starting player , 1->0,2->1

while all([x < 1000 for x in score]):
    position[player], dice = round(position[player],dice)
    score[player] += position[player]
    player = 1 - player

print(score,position,dice, min(score)*dice)

config = [starts[0],starts[1],0,0,0,1] #starting positions, scores,
                                       #current player, number of universes

s = [config] # stack of configurations, to be considered

wins = [0,0]

dirac = [[3,1],[4,3],[5,6],[6,7],[7,6],[8,3],[9,1]]
#dice rolls and counts
r = 0

while len(s)>0:
    print(r,len(s),wins)
    r+=1
    new_s = []
    for curr in s:
        player = curr[4]
        for p in dirac:
            new = curr.copy()
            dice, counts = p[0],p[1]
            new[player] = (new[player] + dice - 1)%10 + 1 #new position
            new[player + 2] += new[player] #new score
            new[-1] *= counts
            if new[player + 2] >= 21:
                wins[player] += new[-1]
            else:
                new[4] = 1-player #switch player
                new_s.append(new)
    s = new_s
print(wins)

"""
option: for each round (ca 20), save for each number of universes in matrix
of dim 21x21x10x10 (for every option of score and position)
problem : A might have lots of zeros, that still have to be considered (i think)
"""     
