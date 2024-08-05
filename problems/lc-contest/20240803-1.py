from collections import defaultdict, Counter

def winningPlayerCount(n, pick):
    res = [False]*n

    counter = [Counter() for x in range(n)]

    for player, ball in pick: 
        counter[player][ball] += 1
        if counter[player][ball] > player: 
            res[player] = True
    return sum([1 for x in res if x])

n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]

print(winningPlayerCount(n, pick))