# https://leetcode.com/problems/bulb-switcher-ii/description/
# 672. Bulb Switcher II


# You can do a dfs backtracking algo with visited. If you visited a state, don't dfs. 
# There are probably symmetric groups you can apply to reduce the space, but I was lazy to figure it out. 

def flipLights(n, presses):
    def all_f(state):
        res = [x for x in state]
        for i in range(len(res)):
            res[i] = not res[i]
        return tuple(res)

    def odd_f(state):
        res = [x for x in state]
        for i in range(len(res)):
            if i % 2 == 1: res[i] = not res[i]
        return tuple(res)

    def even_f(state):
        res = [x for x in state]
        for i in range(len(res)):
            if i % 2 == 0: res[i] = not res[i]
        return tuple(res)

    def thirds_f(state):
        res = [x for x in state]
        for i in range(0, len(res), 3):
            res[i] = not res[i]
        return tuple(res)

    state = tuple([False]*n)
    allStates, visited = set(), set()
    visited.add((presses, state))

    def dfs(presses, state):        
        if presses == 0: 
            allStates.add(state)
        else: 
            for f in [all_f, odd_f, even_f, thirds_f]:
                nextState = f(state)
                if (presses - 1, nextState) not in visited: 
                    visited.add((presses - 1, nextState))
                    dfs(presses - 1, nextState)

    dfs(presses, state)
    return len(allStates)


# n = 2
# presses = 1
# res = [0]*10
# for x in range(3, len(res), 3):
#     print(x)


# n = 3
# presses = 1

n = 1
presses = 2

print(flipLights(n, presses))