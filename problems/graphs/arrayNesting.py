# https://leetcode.com/problems/array-nesting/submissions/1354720691/
# 565. Array Nesting



from math import inf

def arrayNesting(nums):
    n = len(nums)
    visited = [0]*n
    cycles = set()
    paths = [-inf]*n

    def dfs(u): 
        visited[u] = 1
        v = nums[u]
        if visited[v] == 1: 
            cycles.add(v)
        elif visited[v] == 0: 
            dfs(v)
        visited[u] = 2

    # visit all nodes, find the cycles
    for i in range(n):
        if visited[i] == 0: dfs(i)

    def countCycleLength(u):
        cyclePath.add(u)
        res = 1
        v = nums[u]
        if v not in cyclePath: 
            res += countCycleLength(v)
        return res

    for u in cycles: 
        cyclePath = set()
        cycleLength = countCycleLength(u)
        for x in cyclePath: 
            paths[x] = cycleLength

    return max(paths)    

# Union Find Solution








nums = [5,4,0,3,1,6,2]
print(arrayNesting(nums))